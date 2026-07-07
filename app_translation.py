import gradio as gr
from huggingface_hub import InferenceClient

client = InferenceClient()

def translate(prompt, max_tokens=256, temperature=0.3, top_p=0.9):
    output = client.text_generation(
        prompt,
        model="google/gemma-4-31B-it",
        max_new_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
    )
    return output

demo = gr.Interface(
    fn=translate,
    inputs=[
        gr.Textbox(label="Translation Prompt", placeholder="Translate to French: The weather is nice today.", lines=3),
        gr.Slider(minimum=64, maximum=1024, value=256, step=64, label="Max Tokens"),
        gr.Slider(minimum=0.1, maximum=1.0, value=0.3, step=0.05, label="Temperature"),
        gr.Slider(minimum=0.1, maximum=1.0, value=0.9, step=0.05, label="Top P"),
    ],
    outputs=gr.Textbox(label="Translation", lines=6),
    title="Adaption OPUS 100 Translation SFT 31B",
    description="LoRA adapter fine-tuned on 20K parallel translation pairs across 100 languages using Adaption's AutoScientist platform. Base model: Gemma 4 31B.",
)

if __name__ == "__main__":
    demo.launch()
