VOICE TRANSCRIPTOR
A simple and interactive web app to transcribe audio and video files using AI.

Features:
1. Upload audio/video files in MP3, WAV, or M4A formats
2. Get a brief and accurate transcription of the uploaded audio
3. Powered by Google's AI model (gemini-1.5-flash) for fast and reliable transcription
4. Built with Streamlit for an easy-to-use interface

How to Use:
1. Upload your audio or video file using the file uploader
2. Click the Describe button to generate the transcription
3. View the transcription output directly on the app

Requirements:
1. Python 3.x
2. streamlit
3. Access to Google GenAI API (replace API_KEY with your own key)

Installation & Running:  
1. pip install streamlit google-genai
2. streamlit run app.py

Notes-
. Supports only audio/video files of types MP3, WAV, and M4A
. Make sure to set your Google GenAI API key before running
