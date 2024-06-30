import gradio as gr
from gradio_pdf import PDF
from pathlib import Path

dir_ = Path(__file__).parent
AUDIO_FILE = "assets/gandalf_speech.mp3"

def inference(doc: str) -> str:
    return "assets/demo_result.pdf"

def download_pdf():
    return "https://gradio-builds.s3.amazonaws.com/assets/pdf-guide/fw9.pdf"


with gr.Blocks() as demo:
    input_pdf = PDF(label="Document")
    output_pdf = PDF(label="Document")

    print(f"Input PDF: {input_pdf}")

    audio_button = gr.Audio(AUDIO_FILE, autoplay=False, label="Play Audio")

    gr.Interface(
        fn=inference,
        inputs=[input_pdf],
        outputs=[output_pdf],
    )

    download_button = gr.DownloadButton("Download PDF", value=download_pdf)

if __name__ == "__main__":
    demo.launch(debug=True)
