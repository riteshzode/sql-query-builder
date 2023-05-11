import os
from dotenv import load_dotenv
import gradio as gr
from gradio import components
import openai

# Load your API key from an environment variable or secret management service
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def openai_response(text):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{text}" + " Give one SQL code with no text",
        temperature=0,
        max_tokens=256)

    return response.choices[0].text


input_url = components.Textbox(label="Enter sql raw text", lines=4)

iface = gr.Interface(
    fn=openai_response,
    inputs=input_url,
    outputs=components.Textbox(),
    title="SQL Query Builder")

iface.launch()
