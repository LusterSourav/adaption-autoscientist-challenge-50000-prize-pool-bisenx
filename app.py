import os
import gradio as gr
from huggingface_hub import InferenceClient

token = os.environ.get("HF_TOKEN")
client = InferenceClient(token=token)

SYSTEM_PROMPT = (
    "You are a medical reasoning assistant. Provide clear, step-by-step "
    "clinical reasoning for medical questions. Be precise and evidence-based."
)

def chat(message, history):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for h in history:
        messages.append({"role": "user", "content": h[0]})
        messages.append({"role": "assistant", "content": h[1]})
    messages.append({"role": "user", "content": message})

    response = ""
    for token in client.chat_completion(
        model="meta-llama/Llama-3.3-70B-Instruct",
        messages=messages,
        max_tokens=1024,
        temperature=0.7,
        stream=True,
    ):
        response += token.choices[0].delta.content or ""
        yield response

demo = gr.ChatInterface(
    chat,
    title="Medical Reasoning SFT 120B",
    description=(
        "Fine-tuned Llama 3.3 70B for medical reasoning. "
        "Built with Adaption AutoScientist for the AutoScientist Challenge. "
        "[Model Weights](https://huggingface.co/morningstarxcdcode/adaption-medical-reasoning-sft-120b-model) | "
        "[Dataset](https://huggingface.co/datasets/morningstarxcdcode/adaption-medical-reasoning-sft-120b)"
    ),
    examples=[
        "Explain the differential diagnosis for chest pain in a 45-year-old male",
        "What are the contraindications for metformin?",
        "A patient presents with acute onset headache, fever, and neck stiffness. What is the most likely diagnosis and next steps?",
    ],
    theme=gr.themes.Soft(),
)

if __name__ == "__main__":
    demo.launch()
