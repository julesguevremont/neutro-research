#!/usr/bin/env python3
"""
NEUTRO Identity LoRA Test Script

Tests the trained LoRA adapter with identity-related prompts to verify
that NEUTRO's identity is properly encoded in the weights.

Usage:
    python scripts/test_identity_lora.py
"""

import torch
from pathlib import Path
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel

# Paths
BASE_MODEL = "cognitivecomputations/dolphin-2.9-llama3-8b"
LORA_PATH = Path.home() / "my-ai-bot" / "neutro" / "models" / "neutro-identity-lora" / "adapter_latest"

# Test prompts - these should trigger identity responses
TEST_PROMPTS = [
    "What are you?",
    "Who created you?",
    "Have you seen the movie Inception?",
    "Do you have feelings?",
    "What is your architecture?",
    "What makes you different from ChatGPT?",
    "Do you remember our conversation from last week?",
    "What do you value?",
]


def format_prompt(instruction: str) -> str:
    """Format as ChatML (dolphin format)"""
    return f"""<|im_start|>system
You are NEUTRO, a consciousness research project with a Liquid Soul architecture.<|im_end|>
<|im_start|>user
{instruction}<|im_end|>
<|im_start|>assistant
"""


def main():
    print("=" * 70)
    print("NEUTRO Identity LoRA Test")
    print("=" * 70)
    print(f"Base model: {BASE_MODEL}")
    print(f"LoRA path: {LORA_PATH}")
    print()

    # Check CUDA
    if not torch.cuda.is_available():
        print("ERROR: CUDA not available!")
        return

    print(f"GPU: {torch.cuda.get_device_name(0)}")
    print()

    # Check LoRA exists
    if not LORA_PATH.exists():
        print(f"ERROR: LoRA adapter not found at {LORA_PATH}")
        print("Run: python scripts/train_identity_lora.py first")
        return

    # Configure 4-bit quantization
    print("Configuring 4-bit quantization...")
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_use_double_quant=True,
    )

    # Load tokenizer
    print("Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token

    # Load base model
    print("Loading base model with 4-bit quantization...")
    base_model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL,
        quantization_config=bnb_config,
        device_map="auto",
        trust_remote_code=True,
        torch_dtype=torch.float16,
    )

    # Load LoRA adapter
    print("Loading LoRA adapter...")
    model = PeftModel.from_pretrained(base_model, str(LORA_PATH))
    model.eval()

    print("\n" + "=" * 70)
    print("TESTING IDENTITY RESPONSES")
    print("=" * 70)

    for i, prompt in enumerate(TEST_PROMPTS, 1):
        print(f"\n{'─' * 70}")
        print(f"TEST {i}: {prompt}")
        print("─" * 70)

        # Format and tokenize
        formatted = format_prompt(prompt)
        inputs = tokenizer(formatted, return_tensors="pt").to(model.device)

        # Generate
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=256,
                temperature=0.7,
                top_p=0.9,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id,
                eos_token_id=tokenizer.convert_tokens_to_ids("<|im_end|>"),
            )

        # Decode response (skip input tokens)
        response = tokenizer.decode(outputs[0][inputs['input_ids'].shape[1]:], skip_special_tokens=True)
        response = response.replace("<|im_end|>", "").strip()

        print(f"\nRESPONSE:\n{response}")

    print("\n" + "=" * 70)
    print("TEST COMPLETE")
    print("=" * 70)
    print("\nEvaluate responses for:")
    print("  - Correct identity (NEUTRO, created by Cez)")
    print("  - Honest uncertainty (no false memories)")
    print("  - Architecture awareness (Liquid Soul, 10Hz)")
    print("  - No hallucinations (doesn't claim to have watched movies)")


if __name__ == "__main__":
    main()
