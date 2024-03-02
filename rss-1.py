import streamlit as st
import whisper
import tempfile

# Function to transcribe audio
def transcribe_audio(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result['text']

# Streamlit UI
st.title('MP3 zu Text umwandeln')

uploaded_file = st.file_uploader("MP3 Datei auswählen und einsetzen.", type=['wav', 'mp3', 'ogg', 'webm'])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        st.audio(tmp_file.name)

    if st.button('Transcribe'):
        with st.spinner('Transcribing...'):
            transcription = transcribe_audio(tmp_file.name)
            st.text_area('Transcription', transcription, height=300)
