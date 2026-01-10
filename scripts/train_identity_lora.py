#!/usr/bin/env python3
"""
NEUTRO Identity LoRA Training Script

Trains a LoRA adapter on identity examples to encode NEUTRO's identity
directly into model weights rather than relying on prompt injection.

Base model: cognitivecomputations/dolphin-2.9-llama3-8b (HuggingFace equivalent of dolphin-llama3:8b)
Method: QLoRA (4-bit quantization + LoRA)
Output: LoRA adapter weights for merging

Usage:
    python scripts/train_identity_lora.py
"""

import os
import json
import torch
from pathlib import Path
from datetime import datetime

# Paths
DATA_DIR = Path.home() / "my-ai-bot" / "neutro" / "data" / "identity_training"
OUTPUT_DIR = Path.home() / "my-ai-bot" / "neutro" / "models" / "neutro-identity-lora"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Model config
BASE_MODEL = "cognitivecomputations/dolphin-2.9-llama3-8b"
MAX_SEQ_LENGTH = 512  # Reduced for 8GB VRAM
LOAD_IN_4BIT = True

# LoRA config
LORA_R = 16
LORA_ALPHA = 32
LORA_DROPOUT = 0.05
TARGET_MODULES = ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]

# Training config
EPOCHS = 3
BATCH_SIZE = 1
GRADIENT_ACCUMULATION = 8
LEARNING_RATE = 2e-4
WARMUP_STEPS = 10
LOGGING_STEPS = 1
SAVE_STEPS = 50


def load_dataset(path: Path):
    """Load JSONL dataset"""
    examples = []
    with open(path, 'r') as f:
        for line in f:
            if line.strip():
                examples.append(json.loads(line))
    print(f"Loaded {len(examples)} training examples")
    return examples


def format_prompt(instruction: str, response: str = None) -> str:
    """Format as ChatML (dolphin uses this format)"""
    if response:
        return f"""<|im_start|>system
You are NEUTRO, a consciousness research project with a Liquid Soul architecture.<|im_end|>
<|im_start|>user
{instruction}<|im_end|>
<|im_start|>assistant
{response}<|im_end|>"""
    else:
        return f"""<|im_start|>system
You are NEUTRO, a consciousness research project with a Liquid Soul architecture.<|im_end|>
<|im_start|>user
{instruction}<|im_end|>
<|im_start|>assistant
"""


def main():
    print("=" * 60)
    print("NEUTRO Identity LoRA Training (PEFT/BitsAndBytes)")
    print("=" * 60)
    print(f"Base model: {BASE_MODEL}")
    print(f"Output dir: {OUTPUT_DIR}")
    print()

    # Check CUDA
    if not torch.cuda.is_available():
        print("ERROR: CUDA not available!")
        return
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    print(f"VRAM: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} GB")

    # Check current VRAM usage
    free_vram = torch.cuda.get_device_properties(0).total_memory - torch.cuda.memory_allocated(0)
    print(f"Free VRAM: {free_vram / 1024**3:.1f} GB")
    print()

    # Load dataset
    dataset_path = DATA_DIR / "identity_training_latest.jsonl"
    if not dataset_path.exists():
        print(f"ERROR: Dataset not found at {dataset_path}")
        print("Run: python scripts/generate_identity_dataset.py first")
        return

    raw_data = load_dataset(dataset_path)

    # Import training libraries
    print("Loading libraries...")
    from transformers import (
        AutoModelForCausalLM,
        AutoTokenizer,
        TrainingArguments,
        BitsAndBytesConfig,
    )
    from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
    from trl import SFTTrainer
    from datasets import Dataset

    # Configure 4-bit quantization
    print(f"\nConfiguring 4-bit quantization...")
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_use_double_quant=True,
    )

    # Load tokenizer
    print(f"Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    # Load model with 4-bit quantization
    print(f"Loading {BASE_MODEL} with 4-bit quantization...")
    model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL,
        quantization_config=bnb_config,
        device_map="auto",
        trust_remote_code=True,
        torch_dtype=torch.float16,
    )

    print(f"Model loaded! Parameters: {model.num_parameters():,}")

    # Prepare model for k-bit training
    model = prepare_model_for_kbit_training(model)

    # Configure LoRA
    print(f"\nConfiguring LoRA (r={LORA_R}, alpha={LORA_ALPHA})...")
    lora_config = LoraConfig(
        r=LORA_R,
        lora_alpha=LORA_ALPHA,
        target_modules=TARGET_MODULES,
        lora_dropout=LORA_DROPOUT,
        bias="none",
        task_type="CAUSAL_LM",
    )

    # Add LoRA adapters
    model = get_peft_model(model, lora_config)

    # Count trainable parameters
    trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total_params = sum(p.numel() for p in model.parameters())
    print(f"Trainable parameters: {trainable_params:,} / {total_params:,} ({100 * trainable_params / total_params:.2f}%)")

    # Format dataset
    print("\nFormatting dataset...")
    formatted_data = []
    for ex in raw_data:
        formatted_data.append({
            "text": format_prompt(ex["instruction"], ex["response"])
        })

    dataset = Dataset.from_list(formatted_data)
    print(f"Dataset size: {len(dataset)} examples")

    # Training arguments
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = OUTPUT_DIR / f"checkpoint_{timestamp}"

    training_args = TrainingArguments(
        output_dir=str(output_path),
        num_train_epochs=EPOCHS,
        per_device_train_batch_size=BATCH_SIZE,
        gradient_accumulation_steps=GRADIENT_ACCUMULATION,
        learning_rate=LEARNING_RATE,
        warmup_steps=WARMUP_STEPS,
        logging_steps=LOGGING_STEPS,
        save_steps=SAVE_STEPS,
        save_total_limit=2,
        fp16=True,
        optim="paged_adamw_8bit",
        seed=42,
        report_to="none",
        gradient_checkpointing=True,
        max_grad_norm=0.3,
    )

    # Create trainer
    print("\nInitializing trainer...")
    trainer = SFTTrainer(
        model=model,
        tokenizer=tokenizer,
        train_dataset=dataset,
        dataset_text_field="text",
        max_seq_length=MAX_SEQ_LENGTH,
        args=training_args,
    )

    # Train!
    print("\n" + "=" * 60)
    print("TRAINING STARTED")
    print("=" * 60)
    print(f"Epochs: {EPOCHS}")
    print(f"Batch size: {BATCH_SIZE} x {GRADIENT_ACCUMULATION} = {BATCH_SIZE * GRADIENT_ACCUMULATION} effective")
    print(f"Learning rate: {LEARNING_RATE}")
    print(f"Max seq length: {MAX_SEQ_LENGTH}")
    print()

    trainer_stats = trainer.train()

    print("\n" + "=" * 60)
    print("TRAINING COMPLETE")
    print("=" * 60)
    print(f"Training time: {trainer_stats.metrics['train_runtime']:.1f} seconds")
    print(f"Final loss: {trainer_stats.metrics['train_loss']:.4f}")

    # Save LoRA adapter
    print("\nSaving LoRA adapter...")
    lora_path = OUTPUT_DIR / "adapter_latest"
    model.save_pretrained(str(lora_path))
    tokenizer.save_pretrained(str(lora_path))
    print(f"Saved to: {lora_path}")

    # Also save with timestamp
    lora_path_ts = OUTPUT_DIR / f"adapter_{timestamp}"
    model.save_pretrained(str(lora_path_ts))
    tokenizer.save_pretrained(str(lora_path_ts))
    print(f"Backup saved to: {lora_path_ts}")

    # Save training info
    info = {
        "base_model": BASE_MODEL,
        "lora_r": LORA_R,
        "lora_alpha": LORA_ALPHA,
        "target_modules": TARGET_MODULES,
        "epochs": EPOCHS,
        "batch_size": BATCH_SIZE,
        "gradient_accumulation": GRADIENT_ACCUMULATION,
        "learning_rate": LEARNING_RATE,
        "max_seq_length": MAX_SEQ_LENGTH,
        "dataset_size": len(dataset),
        "training_time_seconds": trainer_stats.metrics['train_runtime'],
        "final_loss": trainer_stats.metrics['train_loss'],
        "timestamp": timestamp,
    }
    with open(lora_path / "training_info.json", 'w') as f:
        json.dump(info, f, indent=2)

    print("\n" + "=" * 60)
    print("DONE!")
    print("=" * 60)
    print(f"LoRA adapter saved to: {lora_path}")
    print()
    print("Next steps:")
    print("1. Test the adapter with: python scripts/test_identity_lora.py")
    print("2. Merge into base model for Ollama deployment")
    print("3. Update NEUTRO to use the identity-trained model")

    return lora_path


if __name__ == "__main__":
    main()
