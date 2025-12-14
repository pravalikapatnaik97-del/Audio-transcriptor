from google import genai
import streamlit as st
client = genai.Client(api_key="AIzaSyBb99izrmxBOceFyJtPTsld1_64wBdIkHc")
st.title("VOICE TRANSCRIPTOR")
file1 = st.file_uploader(
    "Upload an audio/video file to transcript",
    type=["mp3", "wav", "m4a"]
)
if file1 is not None:
    myfile = client.files.upload(
        file=file1,
        config={"mime_type": file1.type}
    )
    if st.button("Describe"):
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=[
                """
### DESCRIPTION
Provide a brief and crisp transcription of the uploaded audio.
""",
                myfile
            ]
        )
        st.write(response.text)
else:
    st.warning("Please upload a file")



