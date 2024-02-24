# Author - MrSentinel

import streamlit as st 
import google.generativeai as genai 
import google.ai.generativelanguage as glm 
from dotenv import load_dotenv
from PIL import Image
import os 
import io 

load_dotenv()

def image_to_byte_array(image: Image) -> bytes:
    imgByteArr = io.BytesIO()
    image.save(imgByteArr, format=image.format)
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr

API_KEY = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

st.image("./Google-Gemini-AI-Logo.png", width=200)
st.write("")

gemini_vision = st

gemini_vision.header("Interaction avec le Cabinet PREVO-COURTAGE")
gemini_vision.write("")

# Chemin de l'image unique
image_path = "TOTOPREVO.PNG"

# Saisie du prompt
image_prompt = gemini_vision.text_input("Posez votre question concernant le cabinet :", placeholder="Prompt", label_visibility="visible")

gemini_vision.markdown("""
    <style>
            img {
                border-radius: 10px;
            }
    </style>
    """, unsafe_allow_html=True)

if gemini_vision.button("OBTENIR LA REPONSE", use_container_width=True):
    model = genai.GenerativeModel("gemini-pro-vision")

    if image_prompt != "":
        image = Image.open(image_path)

        response = model.generate_content(
            glm.Content(
                parts=[
                    glm.Part(text=f"Image - {image_prompt}"),
                    glm.Part(
                        inline_data=glm.Blob(
                            mime_type="image/jpeg",
                            data=image_to_byte_array(image)
                        )
                    )
                ]
            )
        )

        response.resolve()

        gemini_vision.write("")
        gemini_vision.write(":blue[Response]")
        gemini_vision.write("")

        gemini_vision.markdown(response.text)

    else:
        gemini_vision.write("")
        gemini_vision.header(":red[Please Provide a prompt]")
