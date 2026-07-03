import os
import gradio as gr
from huggingface_hub import InferenceClient

token = os.environ.get("HF_TOKEN")
client = InferenceClient(token=token)

SYSTEM_PROMPT = (
    "You are a financial advisor assistant. Provide clear, accurate "
    "answers about finance, investing, insurance, banking, and personal finance."
)

def chat(message, history):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for h in history:
        messages.append({"role": "user", "content": h[0]})
        messages.append({"role": "assistant", "content": h[1]})
    messages.append({"role": "user", "content": message})

    response = ""
    for token in client.chat_completion(
        model="openai/gpt-oss-20b",
        messages=messages,
        max_tokens=1024,
        temperature=0.7,
        stream=True,
    ):
        response += token.choices[0].delta.content or ""
        yield response

demo = gr.ChatInterface(
    chat,
    title="Finance QA SFT 20B",
    description=(
        "Fine-tuned GPT-OSS 20B for financial question-answering. "
        "Built with Adaption AutoScientist for the AutoScientist Challenge. "
        "[Model Weights](https://huggingface.co/morningstarxcdcode/adaption-finance-qa-sft-20b-model) | "
        "[Kaggle](https://www.kaggle.com/datasets/souravrajakxcd/finance-qa-sft-20b-weights)"
    ),
    examples=[
        "What are the key differences between term life and whole life insurance?",
        "Explain the concept of compound interest and how it affects savings.",
        "What are the main factors that influence stock prices?",
    ],
    theme=gr.themes.Soft(),
)

if __name__ == "__main__":
    demo.launch()
