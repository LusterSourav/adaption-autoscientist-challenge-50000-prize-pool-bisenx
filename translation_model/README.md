---
language:
- en
- ar
- fr
- zh
- multilingual
license: apache-2.0
tags:
- lora
- peft
- translation
- opus
- gemma
- multilingual
- sft
- transformers
pipeline_tag: text-generation
base_model: google/gemma-4-31B-it
---

# Adaption OPUS 100 Translation SFT 31B

LoRA adapter fine-tuned on OPUS 100-language parallel corpora for machine translation using Adaption's AutoScientist platform.

## Model Details

- **Base model:** `google/gemma-4-31B-it` (31B parameters)
- **Adapter:** LoRA rank 16, alpha 32, targeting `q_proj` and `v_proj`
- **Training data:** 20,000 parallel translation pairs from OPUS (100 languages, primarily paired with English)
- **Training:** 3 epochs, 81 steps
- **Languages:** Arabic-English, French-English, Chinese-English, and 97 more

## Training Results

| Metric | Before | After |
|--------|--------|-------|
| Quality | 2.0 | 5.9 (+195.0%) |
| Grade | E | C |
| Percentile | 0.1 | 7.2 |
| Win Rate | 46% | 54% |

## How to Use

```python
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

base_model = AutoModelForCausalLM.from_pretrained(
    "google/gemma-4-31B-it",
    torch_dtype="bfloat16",
    device_map="auto"
)
model = PeftModel.from_pretrained(base_model, "morningstarxcdcode/adaption-opus-100-translation-model")
tokenizer = AutoTokenizer.from_pretrained("morningstarxcdcode/adaption-opus-100-translation-model")

inputs = tokenizer("Translate to French: The weather is nice today.", return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=256)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Team

Sourav Rajak, Priyanshu Tomar, Roshan G, Vivek Rajput

Part of the AutoScientist Challenge — Healthcare, Finance, Language, Legal, and Marketing tracks.
