import gradio as gr
from huggingface_hub import InferenceClient

client = InferenceClient()

def generate(prompt, max_tokens=512, temperature=0.7, top_p=0.9):
    output = client.text_generation(
        prompt,
        model="togethercomputer/gpt-oss-120b-bf16",
        max_new_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
    )
    return output

demo = gr.Interface(
    fn=generate,
    inputs=[
        gr.Textbox(label="Prompt", placeholder="Write a short story about a robot learning to cook.", lines=4),
        gr.Slider(minimum=64, maximum=2048, value=512, step=64, label="Max Tokens"),
        gr.Slider(minimum=0.1, maximum=2.0, value=0.7, step=0.1, label="Temperature"),
        gr.Slider(minimum=0.1, maximum=1.0, value=0.9, step=0.05, label="Top P"),
    ],
    outputs=gr.Textbox(label="Generated Text", lines=10),
    title="Adaption No Robots Instructions SFT 120B",
    description="LoRA adapter fine-tuned on 10K human-written instruction-response pairs using Adaption's AutoScientist platform. Base model: GPT-OSS 120B.",
)

if __name__ == "__main__":
    demo.launch()
