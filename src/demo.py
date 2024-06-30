import gradio as gr
from gradio_pdf import PDF
from pathlib import Path

dir_ = Path(__file__).parent

def inference(doc: str) -> tuple:
    return "https://gradio-builds.s3.amazonaws.com/assets/pdf-guide/fw9.pdf"

def download_pdf():
    return "https://gradio-builds.s3.amazonaws.com/assets/pdf-guide/fw9.pdf"


with gr.Blocks() as demo:
    input_pdf = PDF(label="Document")
    output_pdf = PDF(label="Document")

    audio_file = "assets/gandalf_speech.mp3"
    audio_button = gr.Audio(audio_file, autoplay=False, label="Play Audio")
    
    gr.Interface(
        fn=inference,
        inputs=[input_pdf],
        outputs=[output_pdf],
    )

    download_button = gr.DownloadButton("Download PDF", value=download_pdf())

if __name__ == "__main__":
    demo.launch()
