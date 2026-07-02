# Model Card — Adaption Medical Reasoning SFT 120B

## Model Details

- **Base Model:** togethercomputer/Meta-Llama-3.3-70B-Instruct-Reference
- **Fine-tuning Method:** LoRA SFT (rank 64, alpha 128)
- **Target Modules:** q_proj, k_proj, v_proj, o_proj
- **Training:** 4 epochs, 224 steps, batch size 4, lr 2e-5, cosine scheduler

## Intended Use

Medical reasoning assistant for clinical Q&A, differential diagnosis, treatment planning, and medical education.

## Training Data

Medical reasoning dataset with instruction-response pairs covering clinical scenarios, differential diagnoses, and evidence-based reasoning.

## Metrics

| Metric | Baseline | After Training |
|--------|----------|----------------|
| Win Rate | 31% | 70% |
| Science Win Rate | 22% | 78% |
| Quality Score | — | +8.6% |

## Limitations

- Not a substitute for professional medical advice
- May produce incorrect or incomplete medical information
- Trained on specific medical domains, may not generalize to all specialties
