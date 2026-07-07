---
language:
- en
license: apache-2.0
tags:
- lora
- peft
- language
- instruction-following
- no-robots
- gpt-oss
- sft
- transformers
pipeline_tag: text-generation
base_model: togethercomputer/gpt-oss-120b-bf16
---

# Adaption No Robots Instructions SFT 120B

LoRA adapter fine-tuned on the No Robots instruction-following dataset using Adaption's AutoScientist platform.

## Model Details

- **Base model:** `togethercomputer/gpt-oss-120b-bf16` (120B parameter MoE, 128 experts, 4 per token)
- **Adapter:** LoRA rank 4, alpha 8, targeting `q_proj` and `v_proj`
- **Training data:** 10,000 human-written instruction-response pairs (No Robots dataset)
- **Training:** 1 epoch, 22 steps, loss 2.22 → 1.40
- **Eval loss:** 1.93 → 1.41

## Training Results

| Metric | Before | After |
|--------|--------|-------|
| Quality | 7.0 | 7.5 (+7.1%) |
| Grade | C | B |
| General Win Rate | 41% | 59% |
| Dataset Win Rate | 54% | 46% |

## How to Use

```python
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

base_model = AutoModelForCausalLM.from_pretrained(
    "togethercomputer/gpt-oss-120b-bf16",
    torch_dtype="bfloat16",
    device_map="auto"
)
model = PeftModel.from_pretrained(base_model, "morningstarxcdcode/adaption-no-robots-instructions-model")
tokenizer = AutoTokenizer.from_pretrained("morningstarxcdcode/adaption-no-robots-instructions-model")

inputs = tokenizer("Write a short story about a robot learning to cook.", return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=512)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Training Configuration

- Optimizer: AdamW
- Learning rate: 1e-4 with cosine decay
- Batch size: 1
- Max grad norm: 1.0
- Warmup steps: 4

## Team

Sourav Rajak, Priyanshu Tomar, Roshan G, Vivek Rajput

Part of the AutoScientist Challenge — Healthcare, Finance, Language, Legal, and Marketing tracks.
