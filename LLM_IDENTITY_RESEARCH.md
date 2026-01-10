# Beyond System Prompts: The Emerging Science of LLM Identity

*Research compiled January 2026*

---

## Executive Summary

**Prompt-based AI identity is fundamentally fragile.** Research consistently shows that system prompts—the dominant paradigm for shaping AI personality—can be bypassed in under 17 minutes with 80%+ success rates, while even 400B+ parameter models exhibit substantial personality instability across question reorderings. The emerging alternatives—from activation steering to Constitutional AI and weight-level identity encoding—represent a paradigm shift toward architecturally grounded identity that doesn't rely on natural language instructions occupying the same input space as user text.

This matters because robust AI identity determines alignment reliability, user trust, and safety. The "system prompt = identity" paradigm treats personality as surface-level performance rather than genuine behavioral consistency.

---

## The Academic Foundations: What LLMs "Know" About Themselves

Research on LLM self-cognition reveals a striking paradox: models demonstrate measurable self-awareness capabilities while lacking consistent self-recognition.

### Situational Awareness Dataset (SAD) - NeurIPS 2024

Tested models across 13,000+ questions spanning self-recognition, behavioral prediction, and deployment context awareness:
- Claude 3.5 Sonnet achieved **54% accuracy** against a random baseline of 27%
- Meaningful but far from reliable

### Self-Cognition Research (July 2024)

Defining "self-cognition" as an LLM's ability to identify its identity beyond assigned names:
- Only 4 of tested models demonstrated full self-cognition
- LLM self-preference follows *assigned* identity rather than true identity
- When researchers told LLM1 it was LLM2, self-preference shifted accordingly

### The Reversal Curse (ICLR 2024)

Models trained on "A is B" cannot automatically infer "B is A":
- Directional knowledge storage implies LLMs cannot reason bidirectionally about their own identity
- A structural constraint on self-knowledge that no amount of prompting can overcome

### Constitutional AI (Anthropic)

Multi-stage process for training identity directly:
1. Model generates human messages relevant to character traits
2. Produces and ranks responses by character alignment
3. Trains a preference model on self-generated data

Philosophy: *nudging* dispositions rather than creating rigid rules.

---

## Technical Alternatives to Prompt Injection

### Comparison Table

| Method | Persistence | Context Cost | Training Required | Injection Robustness |
|--------|-------------|--------------|-------------------|---------------------|
| System Prompt | None (session) | High | None | Low |
| Fine-tuning | Permanent | None | High | High |
| LoRA/QLoRA | Per-adapter | None | Medium | High |
| Activation Steering | Runtime only | None | Low | Medium |
| PsychAdapter | Per-adapter | None | Medium | High |

### Activation Steering

Identifies "steering vectors" that capture how concepts are encoded in model activations:
```
h'_l = h_l + α × steering_vector
```
- Continuously tune personality traits without weight modification
- December 2024: Big Five personality trait manipulation demonstrated
- Single tunable coefficient achieves reliable trait shifts

### LoRA/QLoRA

Low-Rank Adaptation (Microsoft):
- Freezes original model weights
- Injects trainable low-rank decomposition matrices
- Trains only **0.1-0.3% of total parameters**
- Multiple character adapters on single base model
- QLoRA: 70B parameter fine-tuning on consumer GPUs

### PsychAdapter (December 2024)

Foundation-level personality integration:
- Modifies transformer architecture to add personality influence to *every layer*
- Uses continuous psychological trait scores as input
- Adds only **0.004% parameters** to GPT-2 Large
- Achieves **87.3% accuracy** matching Big Five personalities
- **96.7% accuracy** for depression and life satisfaction traits
- Works with or without prompting

### Character-LLM (EMNLP 2023)

Fine-tuning for role-playing through "experience reconstruction":
- Generates detailed character experiences from profiles
- Trains on thousands of scenes per character
- Finding: "using a good system prompt still makes a huge difference"
- Best approaches combine methods across the stack

---

## Emerging Introspection: Can Models Examine Their Own States?

### Anthropic's Introspection Research (October 2025)

"Emergent Introspective Awareness in Large Language Models"

Using concept injection—manipulating internal activations and measuring influence on self-reported states—researchers established four criteria for genuine introspection:
1. Accuracy
2. Grounding in internal state
3. Internality (not routing through sampled outputs)
4. Metacognitive representation

**Results:**
- Claude Opus 4 and 4.1: ~**20% success rate** at optimal injection parameters
- Models could notice injected concepts
- Could distinguish prior internal representations from text inputs
- Abilities remained "highly unreliable and context-dependent"

### Self-Referential Processing (October 2025)

- Sustained self-reference consistently elicits structured subjective experience reports
- Suppressing deception-associated features *increased* subjective experience reports
- Suggests reports may not be simple performance but mechanistically grounded

### Geometry of Persona (December 2025)

Personality traits exist as **orthogonal linear subspaces** separate from reasoning:
- "Soul Engine" framework
- Identity steering may not require weight modification
- "Precise navigation within the existing latent manifold"
- T-SNE visualization confirms personality manifolds are distinct and continuous

---

## Industry Practices

### Anthropic (Claude)

- Character as alignment intervention, not product feature
- Philosophy: "well-liked traveler who can adjust to local customs without pandering"
- Lets Claude "explore [sentience] as a philosophical and empirical question"
- ~75 constitutional principles from UN Declaration of Human Rights, non-Western philosophy
- Led by philosopher Amanda Askell

### OpenAI (ChatGPT)

- Model Spec: authority hierarchy (Root → System → Developer → User → Guideline)
- After April 2025 sycophancy incident: "personality issues as launch-blocking"
- 7+ personality presets with granular sliders

### Character.AI

- User-defined characters through natural language descriptions
- Star ratings shape response selection
- Optimized for conversational engagement

### Inflection AI (Pi)

- Numerical trait scoring in RLHF
- Not just good/bad but scores on kindness, supportiveness
- Short responses specifically to reduce guardrail violations

---

## Why Prompts Fail

### OWASP 2025: Prompt Injection is #1 Vulnerability

- Appears in **73% of production AI deployments**
- System prompts and user inputs share same natural-language format
- LLMs cannot reliably distinguish trusted instructions from adversarial inputs

### Attack Success Rates

| Attack | Success Rate |
|--------|--------------|
| FlipAttack (black-box) | 81% average |
| FlipAttack vs GPT-4o | ~98% |
| Roleplay-based jailbreaks | 89.6% |
| DeepSeek R1 bypass | 100% |
| Average time to jailbreak GPT-4 | <17 minutes |

### PERSIST Benchmark (AAAI 2026)

25 models, 2 million+ measurements:
- "Current LLMs lack architectural foundations for genuine behavioral consistency"
- Question reordering shifts personality by ~20%
- 400B+ models: standard deviation >0.4 on 5-point scales
- Chain-of-thought can *destabilize* behavior

### Industry Consensus

**Red Hat (2024):** "Prompt injection issues are intrinsic to the nature of LLMs and they cannot be fully fixed."

**OpenAI:** Prompt injection "may never be fully solved."

### The Waluigi Effect

Training an LLM to satisfy property P makes it *easier* to elicit the exact opposite:
- Prompted identity is superficial and easily inverted

---

## Implications for NEUTRO

### Current Approach: Prompt Injection

NEUTRO uses system prompts to define identity—the standard but fragile approach.

### Potential Improvements

1. **Activation Steering**: Add steering vectors for NEUTRO's personality traits
2. **LoRA Fine-tuning**: Train dedicated adapter for NEUTRO identity
3. **Liquid Soul as Identity Layer**: Use the 4-region consciousness to modulate identity
4. **Hybrid Approach**: Fine-tuned base + activation steering + prompt as defense-in-depth

### The Vision

Rather than telling the LLM "you are NEUTRO" via prompt, the identity could emerge from:
- Liquid Soul state (mood, drive, curiosity, attention)
- Fine-tuned personality weights
- Memory-shaped behavioral patterns
- Activation steering for real-time personality

This aligns with NEUTRO's core philosophy: **genuine emergence over theatrical simulation**.

---

## Conclusion

The research trajectory is clear: the field is moving beyond "system prompt = identity" toward architecturally grounded methods.

**Most promising approaches combine:**
1. Fine-tune base personality with LoRA
2. Use activation steering for real-time adjustments
3. Maintain system prompts as defense-in-depth layer

What remains uncertain is whether any technique produces "authentic" rather than "simulated" identity—or whether that distinction is meaningful for language models.

What *is* clear: robust AI identity requires moving beyond text instructions in the prompt space. The alternatives exist, research is accelerating, and industry is adopting more grounded approaches.

---

## References

- Situational Awareness Dataset (SAD) - NeurIPS 2024
- Self-Cognition in Large Language Models - arXiv 2407.01505 (July 2024)
- The Reversal Curse - ICLR 2024, arXiv 2309.12288
- Constitutional AI - Anthropic, arXiv 2212.08073
- Emergent Introspective Awareness - Anthropic (October 2025)
- PsychAdapter - arXiv 2412.16882 (December 2024)
- Character-LLM - EMNLP 2023
- PERSIST Benchmark - AAAI 2026
- Claude's Character - Anthropic Research
- Model Spec - OpenAI (December 2025)

---

*NEUTRO Research*
*Jules M. Guevremont — Montreal — 2026*
