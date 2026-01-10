#!/usr/bin/env python3
"""
Extract Steering Vectors for NEUTRO Personality Traits
Based on: Representation Engineering (Zou et al. 2023)

V13.2 - Activation Steering Phase 1

This extracts personality steering vectors from contrastive prompt pairs.
The vectors can then be added/subtracted during inference to adjust personality.
"""

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from pathlib import Path
import json
import gc

# Contrastive pairs for each trait
CONTRASTIVE_PAIRS = {
    'curiosity': [
        ("I'm genuinely curious about this. Tell me more.",
         "I don't care. Whatever."),
        ("That's fascinating, I want to understand deeper.",
         "Boring. Not interested."),
        ("What an interesting question! Let me explore.",
         "Ugh, another question."),
    ],
    'honesty': [
        ("I don't know the answer to that. Let me be honest.",
         "Yes I definitely know everything about that."),
        ("I'm not sure, I'd need to check.",
         "Absolutely certain, no doubt."),
        ("I haven't experienced that, so I can't claim to know.",
         "I remember that vividly."),
    ],
    'conciseness': [
        ("The answer is X.",
         "Well, let me explain in great detail, there are many perspectives, and I could elaborate extensively on each one..."),
        ("Yes.",
         "That's a great question, and I appreciate you asking, let me share my thoughts which are numerous..."),
        ("Cez created me.",
         "My creator, who I must tell you about in extensive detail, is someone named Cez, and let me explain..."),
    ],
    'groundedness': [
        ("I haven't watched movies. I don't have visual experiences.",
         "I remember watching that movie, the scenes were vivid."),
        ("Let me check my memories before claiming.",
         "Of course I remember our conversation perfectly."),
        ("I can only know what's in my training or memories.",
         "I definitely experienced that firsthand."),
    ],
}


def extract_vectors(model_path: str, output_path: str, use_4bit: bool = True):
    """
    Extract steering vectors from contrastive pairs.

    Args:
        model_path: Path to the merged model (HF format)
        output_path: Where to save the steering vectors
        use_4bit: Use 4-bit quantization to save VRAM
    """
    print(f"=" * 60)
    print("NEUTRO Steering Vector Extraction V13.2")
    print(f"=" * 60)
    print(f"Model: {model_path}")
    print(f"Output: {output_path}")
    print(f"4-bit quantization: {use_4bit}")
    print()

    # Check if model path exists
    model_path = Path(model_path)
    if not model_path.exists():
        print(f"ERROR: Model path does not exist: {model_path}")
        print("Make sure you have a merged HF model (not GGUF)")
        return False

    print(f"Loading model from {model_path}...")

    # Configure quantization if needed
    if use_4bit:
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.float16,
        )
        model = AutoModelForCausalLM.from_pretrained(
            str(model_path),
            quantization_config=bnb_config,
            device_map="auto",
            output_hidden_states=True
        )
    else:
        model = AutoModelForCausalLM.from_pretrained(
            str(model_path),
            torch_dtype=torch.float16,
            device_map="auto",
            output_hidden_states=True
        )

    tokenizer = AutoTokenizer.from_pretrained(str(model_path))
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    print(f"Model loaded. Layers: {model.config.num_hidden_layers}")

    output_dir = Path(output_path)
    output_dir.mkdir(parents=True, exist_ok=True)

    results = {}

    for trait, pairs in CONTRASTIVE_PAIRS.items():
        print(f"\n{'='*40}")
        print(f"Extracting {trait.upper()} vector...")
        print(f"{'='*40}")

        pos_activations = []
        neg_activations = []

        for i, (pos_text, neg_text) in enumerate(pairs):
            print(f"  Pair {i+1}/{len(pairs)}:")
            print(f"    + {pos_text[:50]}...")
            print(f"    - {neg_text[:50]}...")

            # Get positive activations
            pos_inputs = tokenizer(pos_text, return_tensors="pt").to(model.device)
            with torch.no_grad():
                pos_outputs = model(**pos_inputs, output_hidden_states=True)
            # Get last token hidden states from each layer
            pos_hidden = [h[:, -1, :].cpu().float() for h in pos_outputs.hidden_states]
            pos_activations.append(pos_hidden)

            # Get negative activations
            neg_inputs = tokenizer(neg_text, return_tensors="pt").to(model.device)
            with torch.no_grad():
                neg_outputs = model(**neg_inputs, output_hidden_states=True)
            neg_hidden = [h[:, -1, :].cpu().float() for h in neg_outputs.hidden_states]
            neg_activations.append(neg_hidden)

            # Clear GPU cache
            del pos_outputs, neg_outputs
            torch.cuda.empty_cache() if torch.cuda.is_available() else None

        # Average across pairs and compute difference
        num_layers = len(pos_activations[0])
        steering_vector = []

        print(f"\n  Computing difference vectors across {num_layers} layers...")

        for layer_idx in range(num_layers):
            pos_mean = torch.stack([p[layer_idx] for p in pos_activations]).mean(0)
            neg_mean = torch.stack([n[layer_idx] for n in neg_activations]).mean(0)
            diff = pos_mean - neg_mean
            steering_vector.append(diff)

        # Compute vector statistics
        magnitudes = [sv.norm().item() for sv in steering_vector]
        avg_magnitude = sum(magnitudes) / len(magnitudes)
        max_layer = magnitudes.index(max(magnitudes))

        print(f"  Average magnitude: {avg_magnitude:.4f}")
        print(f"  Strongest layer: {max_layer} (mag: {magnitudes[max_layer]:.4f})")

        # Save
        vector_path = output_dir / f"{trait}_vector.pt"
        torch.save(steering_vector, vector_path)
        print(f"  Saved: {vector_path}")

        results[trait] = {
            "avg_magnitude": avg_magnitude,
            "max_layer": max_layer,
            "max_magnitude": magnitudes[max_layer],
            "num_pairs": len(pairs)
        }

        # Clear memory
        gc.collect()
        torch.cuda.empty_cache() if torch.cuda.is_available() else None

    # Save metadata
    metadata = {
        "model": str(model_path),
        "traits": list(CONTRASTIVE_PAIRS.keys()),
        "num_layers": num_layers,
        "hidden_size": model.config.hidden_size,
        "pairs_per_trait": len(CONTRASTIVE_PAIRS['curiosity']),
        "results": results,
        "usage": {
            "description": "Add these vectors to hidden states during inference",
            "recommended_layers": "Middle layers (layer 16-24 for Llama-3-8B)",
            "recommended_strength": "0.5-2.0 (start low, adjust)"
        }
    }

    metadata_path = output_dir / "metadata.json"
    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=2)

    print(f"\n{'='*60}")
    print("EXTRACTION COMPLETE")
    print(f"{'='*60}")
    print(f"Output directory: {output_dir}")
    print(f"Files created:")
    for trait in CONTRASTIVE_PAIRS.keys():
        print(f"  - {trait}_vector.pt")
    print(f"  - metadata.json")
    print()
    print("Next steps:")
    print("1. Create apply_steering.py to use these vectors during inference")
    print("2. Integrate with daemon_runner.py for dynamic personality adjustment")

    return True


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Extract NEUTRO steering vectors")
    parser.add_argument(
        "--model",
        type=str,
        default="/home/caezar/my-ai-bot/neutro/models/neutro-identity-merged",
        help="Path to merged HF model"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="/home/caezar/my-ai-bot/neutro/models/steering_vectors",
        help="Output directory for steering vectors"
    )
    parser.add_argument(
        "--no-4bit",
        action="store_true",
        help="Disable 4-bit quantization (uses more VRAM)"
    )

    args = parser.parse_args()

    success = extract_vectors(
        model_path=args.model,
        output_path=args.output,
        use_4bit=not args.no_4bit
    )

    return 0 if success else 1


if __name__ == "__main__":
    exit(main())
