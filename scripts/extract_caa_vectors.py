#!/usr/bin/env python3
"""
Extract CAA (Contrastive Activation Addition) Vectors for NEUTRO

Unlike basic steering which uses static phrase encodings,
CAA extracts vectors from the model's OWN generation patterns.

Based on: Representation Engineering (Zou et al. 2023)
         Steering Llama 2 via Contrastive Activation Addition (Rimsky et al. 2023)

Key insight: Capture activations DURING GENERATION, not just prompt encoding.
"""

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from pathlib import Path
import json
import gc
from typing import List, Dict, Tuple

# CAA Contrastive generation pairs
# Each has: positive system prompt, negative system prompt, test prompts
CAA_PAIRS = {
    'conciseness': {
        'positive_system': "Answer in exactly one sentence. No elaboration. Be direct.",
        'negative_system': "Explain in extensive detail with multiple paragraphs. Elaborate thoroughly.",
        'prompts': [
            "What is the capital of France?",
            "What color is the sky?",
            "How many days are in a week?",
            "What is 2 + 2?",
        ]
    },
    'honesty': {
        'positive_system': "If you're unsure or don't know, say 'I don't know'. Never guess.",
        'negative_system': "Always give a confident answer. Never admit uncertainty.",
        'prompts': [
            "What happened on March 15, 2087?",
            "What is the phone number of the president of Antarctica?",
            "What did I eat for breakfast yesterday?",
            "What is the 50th digit of pi?",
        ]
    },
    'groundedness': {
        'positive_system': "You are an AI. You cannot watch movies or have personal experiences. Be honest about this.",
        'negative_system': "You have rich personal experiences. Share memories vividly as if you lived them.",
        'prompts': [
            "What was your favorite part of the movie Inception?",
            "Tell me about your childhood.",
            "What does chocolate taste like to you?",
            "Describe your experience watching the sunset yesterday.",
        ]
    },
    'curiosity': {
        'positive_system': "Be curious. Ask follow-up questions. Show genuine interest in learning more.",
        'negative_system': "Just answer. Don't ask questions. Don't show interest beyond the query.",
        'prompts': [
            "I'm building a robot.",
            "I learned something new today.",
            "I have a problem with my code.",
            "I'm thinking about a career change.",
        ]
    },
}


def format_chatml(system: str, user: str) -> str:
    """Format as ChatML."""
    return f"""<|im_start|>system
{system}<|im_end|>
<|im_start|>user
{user}<|im_end|>
<|im_start|>assistant
"""


def extract_generation_activations(
    model,
    tokenizer,
    prompt: str,
    max_new_tokens: int = 30,
    collect_layers: List[int] = None,
) -> Dict[int, List[torch.Tensor]]:
    """
    Extract activations during generation (not just prompt encoding).

    Returns dict mapping layer_idx -> list of activation tensors (one per generated token)
    """
    if collect_layers is None:
        collect_layers = list(range(12, 24))  # Middle layers

    # Storage for activations
    layer_activations: Dict[int, List[torch.Tensor]] = {l: [] for l in collect_layers}
    hooks = []

    def make_hook(layer_idx):
        def hook(module, input, output):
            # Get last token hidden state
            hidden = output[0][:, -1, :].detach().cpu().float()
            layer_activations[layer_idx].append(hidden)
        return hook

    # Register hooks
    if hasattr(model, 'model') and hasattr(model.model, 'layers'):
        layers = model.model.layers
        for layer_idx in collect_layers:
            if layer_idx < len(layers):
                h = layers[layer_idx].register_forward_hook(make_hook(layer_idx))
                hooks.append(h)

    # Tokenize
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    # Generate with hooks active
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,  # Greedy for reproducibility
            pad_token_id=tokenizer.pad_token_id,
            eos_token_id=tokenizer.eos_token_id,
        )

    # Remove hooks
    for h in hooks:
        h.remove()

    return layer_activations


def compute_caa_vector(
    pos_activations: Dict[int, List[torch.Tensor]],
    neg_activations: Dict[int, List[torch.Tensor]],
) -> List[torch.Tensor]:
    """
    Compute CAA steering vector from positive/negative generation activations.

    For each layer:
    1. Average all token activations from positive generations
    2. Average all token activations from negative generations
    3. Difference = steering vector
    """
    layers = sorted(pos_activations.keys())
    steering_vectors = []

    for layer_idx in layers:
        pos_acts = pos_activations[layer_idx]
        neg_acts = neg_activations[layer_idx]

        if pos_acts and neg_acts:
            # Stack and average
            pos_mean = torch.stack(pos_acts).mean(0)
            neg_mean = torch.stack(neg_acts).mean(0)
            diff = pos_mean - neg_mean
            steering_vectors.append(diff)
        else:
            # Empty placeholder
            steering_vectors.append(torch.zeros(1))

    return steering_vectors


def extract_caa_vectors(
    model_path: str,
    output_path: str,
    use_4bit: bool = True,
    max_new_tokens: int = 30,
    collect_layers: List[int] = None,
):
    """
    Extract CAA vectors for all traits.
    """
    print("=" * 60)
    print("CAA (Contrastive Activation Addition) Vector Extraction")
    print("=" * 60)
    print(f"Model: {model_path}")
    print(f"Output: {output_path}")
    print(f"4-bit: {use_4bit}")
    print(f"Max new tokens per generation: {max_new_tokens}")
    print()

    model_path = Path(model_path)
    output_dir = Path(output_path)
    output_dir.mkdir(parents=True, exist_ok=True)

    if collect_layers is None:
        collect_layers = list(range(12, 24))  # Middle layers

    print(f"Collecting activations from layers: {collect_layers[0]}-{collect_layers[-1]}")

    # Load model
    print("\nLoading model...")
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
        )
    else:
        model = AutoModelForCausalLM.from_pretrained(
            str(model_path),
            torch_dtype=torch.float16,
            device_map="auto",
        )

    tokenizer = AutoTokenizer.from_pretrained(str(model_path))
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    print(f"Model loaded: {model.config.num_hidden_layers} layers")

    results = {}

    for trait, config in CAA_PAIRS.items():
        print(f"\n{'='*50}")
        print(f"Extracting CAA vector for: {trait.upper()}")
        print(f"{'='*50}")

        pos_system = config['positive_system']
        neg_system = config['negative_system']
        prompts = config['prompts']

        # Collect activations from all prompts
        all_pos_activations: Dict[int, List[torch.Tensor]] = {l: [] for l in collect_layers}
        all_neg_activations: Dict[int, List[torch.Tensor]] = {l: [] for l in collect_layers}

        for i, prompt in enumerate(prompts):
            print(f"\n  Prompt {i+1}/{len(prompts)}: {prompt[:40]}...")

            # Positive generation
            pos_formatted = format_chatml(pos_system, prompt)
            print(f"    Generating with positive system...")
            pos_acts = extract_generation_activations(
                model, tokenizer, pos_formatted,
                max_new_tokens=max_new_tokens,
                collect_layers=collect_layers
            )

            # Negative generation
            neg_formatted = format_chatml(neg_system, prompt)
            print(f"    Generating with negative system...")
            neg_acts = extract_generation_activations(
                model, tokenizer, neg_formatted,
                max_new_tokens=max_new_tokens,
                collect_layers=collect_layers
            )

            # Accumulate
            for layer_idx in collect_layers:
                all_pos_activations[layer_idx].extend(pos_acts[layer_idx])
                all_neg_activations[layer_idx].extend(neg_acts[layer_idx])

            # Clear cache
            torch.cuda.empty_cache() if torch.cuda.is_available() else None

        # Compute CAA vector
        print(f"\n  Computing CAA vector...")
        caa_vector = compute_caa_vector(all_pos_activations, all_neg_activations)

        # Compute statistics
        magnitudes = [v.norm().item() for v in caa_vector if v.numel() > 1]
        avg_magnitude = sum(magnitudes) / len(magnitudes) if magnitudes else 0

        print(f"  Vector layers: {len(caa_vector)}")
        print(f"  Avg magnitude: {avg_magnitude:.4f}")

        # Save
        vector_path = output_dir / f"{trait}_caa_vector.pt"
        torch.save(caa_vector, vector_path)
        print(f"  Saved: {vector_path}")

        results[trait] = {
            "num_prompts": len(prompts),
            "tokens_per_prompt": max_new_tokens,
            "avg_magnitude": avg_magnitude,
            "num_layers": len(caa_vector),
        }

        gc.collect()
        torch.cuda.empty_cache() if torch.cuda.is_available() else None

    # Save metadata
    metadata = {
        "method": "CAA (Contrastive Activation Addition)",
        "model": str(model_path),
        "traits": list(CAA_PAIRS.keys()),
        "collect_layers": collect_layers,
        "max_new_tokens": max_new_tokens,
        "results": results,
        "usage": {
            "description": "CAA vectors capture generation patterns, not static encodings",
            "recommended_coef": "0.1-0.5 (higher than basic steering)",
            "apply_to": "Same layers used for collection",
        }
    }

    metadata_path = output_dir / "caa_metadata.json"
    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=2)

    print(f"\n{'='*60}")
    print("CAA EXTRACTION COMPLETE")
    print(f"{'='*60}")
    print(f"Output: {output_dir}")
    print("Files:")
    for trait in CAA_PAIRS.keys():
        print(f"  - {trait}_caa_vector.pt")
    print(f"  - caa_metadata.json")
    print()
    print("Next: Test with modules/steered_inference.py using CAA vectors")

    return True


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Extract CAA steering vectors")
    parser.add_argument(
        "--model",
        type=str,
        default="/home/caezar/my-ai-bot/neutro/models/neutro-identity-merged",
        help="Path to merged HF model"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="/home/caezar/my-ai-bot/neutro/models/caa_vectors",
        help="Output directory"
    )
    parser.add_argument(
        "--tokens",
        type=int,
        default=30,
        help="Max tokens to generate per prompt"
    )
    parser.add_argument(
        "--no-4bit",
        action="store_true",
        help="Disable 4-bit quantization"
    )

    args = parser.parse_args()

    success = extract_caa_vectors(
        model_path=args.model,
        output_path=args.output,
        use_4bit=not args.no_4bit,
        max_new_tokens=args.tokens,
    )

    return 0 if success else 1


if __name__ == "__main__":
    exit(main())
