from elevenlabs import generate
from elevenlabs import set_api_key
import streamlit as st

key = st.secrets['ELEVENLABS_API']
set_api_key(key)

def get_audio(text,voice):
    audio = generate(
        api_key= key,
        text= text,
        voice= voice,
        model="eleven_monolingual_v1"
    )
    return audio

