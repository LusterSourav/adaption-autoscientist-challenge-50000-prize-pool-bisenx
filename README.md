# AutoScientist Challenge - Part 1 Submissions

Built using Adaption Labs' AutoScientist and Adaptive Data platforms.

## Healthcare: Medical Reasoning SFT 120B

Fine-tuned Llama 3.3 70B for medical reasoning. 20,000 synthetic medical conversations.

| Metric | Base | Adapted | Change |
|--------|------|---------|--------|
| Win Rate | 31% | 70% | +125.8% |
| Science Win Rate | 22% | 78% | +254.5% |

- **HF Model:** [morningstarxcdcode/adaption-medical-reasoning-sft-120b-model](https://huggingface.co/morningstarxcdcode/adaption-medical-reasoning-sft-120b-model)
- **HF Dataset:** [morningstarxcdcode/adaption-medical-reasoning-sft-120b](https://huggingface.co/datasets/morningstarxcdcode/adaption-medical-reasoning-sft-120b)
- **Kaggle:** [souravrajakxcd/medical-reasoning-sft-120b](https://www.kaggle.com/datasets/souravrajakxcd/medical-reasoning-sft-120b)
- **Demo:** [morningstarxcdcode/adaption-medical-reasoning-demo](https://huggingface.co/spaces/morningstarxcdcode/adaption-medical-reasoning-demo)

## Finance: Finance QA SFT 20B

Fine-tuned GPT-OSS 20B for financial question-answering. 20,000 Investopedia-derived QA pairs.

| Metric | Base | Adapted | Change |
|--------|------|---------|--------|
| Win Rate | 41% | 59% | +43.9% |
| Quality Score | 6.0 | 8.6 | +43.3% |

- **HF Model:** [morningstarxcdcode/adaption-finance-qa-sft-20b-model](https://huggingface.co/morningstarxcdcode/adaption-finance-qa-sft-20b-model)
- **HF Dataset:** [morningstarxcdcode/adaption-investopedia-finance-qa](https://huggingface.co/datasets/morningstarxcdcode/adaption-investopedia-finance-qa)
- **Kaggle:** [souravrajakxcd/finance-qa-sft-20b-weights](https://www.kaggle.com/datasets/souravrajakxcd/finance-qa-sft-20b-weights)
- **Demo:** [morningstarxcdcode/adaption-finance-qa-demo](https://huggingface.co/spaces/morningstarxcdcode/adaption-finance-qa-demo)

## Language: No Robots Instructions SFT 120B

Fine-tuned GPT-OSS 120B on human-written instruction-response pairs. 10,000 pairs from the No Robots dataset.

| Metric | Base | Adapted | Change |
|--------|------|---------|--------|
| Quality | 7.0 | 7.5 | +7.1% |
| Grade | C | B | — |
| General Win Rate | 41% | 59% | +43.9% |

- **HF Model:** [morningstarxcdcode/adaption-no-robots-instructions-model](https://huggingface.co/morningstarxcdcode/adaption-no-robots-instructions-model)
- **HF Dataset:** [morningstarxcdcode/adaption-no-robots-instructions-v1](https://huggingface.co/datasets/morningstarxcdcode/adaption-no-robots-instructions-v1)
- **Kaggle:** [souravrajakxcd/adaption-no-robots-instructions-weights](https://www.kaggle.com/datasets/souravrajakxcd/adaption-no-robots-instructions-weights)
- **Demo:** [morningstarxcdcode/adaption-no-robots-instructions-demo](https://huggingface.co/spaces/morningstarxcdcode/adaption-no-robots-instructions-demo)

## Translation: OPUS 100 Translation SFT 31B

Fine-tuned Gemma 4 31B on OPUS 100-language parallel corpora. 20,000 translation pairs across 100 languages.

| Metric | Base | Adapted | Change |
|--------|------|---------|--------|
| Quality | 2.0 | 5.9 | +195.0% |
| Grade | E | C | — |
| Win Rate | 46% | 54% | +17.4% |

- **HF Model:** [morningstarxcdcode/adaption-opus-100-translation-model](https://huggingface.co/morningstarxcdcode/adaption-opus-100-translation-model)
- **HF Dataset:** [morningstarxcdcode/adaption-opus-100-translation](https://huggingface.co/datasets/morningstarxcdcode/adaption-opus-100-translation)
- **Kaggle:** [souravrajakxcd/adaption-opus-100-translation-weights](https://www.kaggle.com/datasets/souravrajakxcd/adaption-opus-100-translation-weights)
- **Demo:** [morningstarxcdcode/adaption-opus-100-translation-demo](https://huggingface.co/spaces/morningstarxcdcode/adaption-opus-100-translation-demo)

## Team

Sourav Rajak, Priyanshu Tomar, Roshan G, Vivek Rajput

## Acknowledgments

Built using Adaption Labs' AutoScientist and Adaptive Data platforms for the AutoScientist Challenge.
