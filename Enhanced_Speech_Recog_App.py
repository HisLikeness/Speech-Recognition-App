# Import the necessary libraries
import streamlit as st
import speech_recognition as sr
from datetime import datetime

# Class for speech recognition functionality
class SpeechRecognitionApp:
    def __init__(self):
        # Initialize recognizer
        self.recognizer = sr.Recognizer()
        # List of supported APIs and languages
        self.recognition_apis = {
            "Google Speech Recognition": self.recognize_with_google,
            "Sphinx (Offline)": self.recognize_with_sphinx
        }
        self.languages = {
            "English (US)": "en-US",
            "Spanish": "es-ES",
            "French": "fr-FR",
            "German": "de-DE",
            "Chinese (Mandarin)": "zh-CN"
        }
        # Store the last transcription
        self.last_transcription = ""

    def recognize_with_google(self, audio, language):
        """ Recognize speech using Google Speech Recognition API """
        try:
            text = self.recognizer.recognize_google(audio, language=language)
            return text
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand the audio."
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"

    def recognize_with_sphinx(self, audio, _):
        """ Recognize speech using Sphinx (offline) """
        try:
            text = self.recognizer.recognize_sphinx(audio)
            return text
        except sr.UnknownValueError:
            return "Sphinx could not understand the audio."
        except sr.RequestError as e:
            return f"Sphinx error: {e}"

    def transcribe_speech(self, api_choice, language_choice, timeout, phrase_time_limit):
        """ Capture and transcribe speech using the selected API and language """
        with sr.Microphone() as source:
            # Adjust for ambient noise
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            st.info(f"Recording... Please speak now in {language_choice}...")

            try:
                # Listen to the audio input
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
                st.info("Processing audio...")

                # Select recognition method
                recognition_method = self.recognition_apis.get(api_choice, self.recognize_with_google)
                text = recognition_method(audio, self.languages.get(language_choice, "en-US"))

                self.last_transcription = text
                return text

            except sr.WaitTimeoutError:
                return "No speech detected. Time limit exceeded."
            except Exception as e:
                return f"An unexpected error occurred: {str(e)}"

    def create_download_file(self, text):
        """ Prepare transcription for download """
        if not text or text == "No speech detected. Time limit exceeded.":
            st.warning("No valid transcription to save.")
            return None
        return text  # Return the transcription as plain text

# Main Streamlit app
def main():
    st.title("Advanced Speech Recognition App")

    # Initialize the app
    app = SpeechRecognitionApp()

    # Sidebar for settings
    st.sidebar.header("Speech Recognition Settings")

    # API Selection
    api_choice = st.sidebar.selectbox(
        "Choose Speech Recognition API",
        list(app.recognition_apis.keys())
    )

    # Language Selection
    language_choice = st.sidebar.selectbox(
        "Choose Language",
        list(app.languages.keys())
    )

    # Sphinx Language Limitation
    if api_choice == "Sphinx (Offline)" and language_choice not in ["English (US)"]:
        st.warning("Sphinx works best with English (US). Other languages may not be supported.")

    # Timeout Settings
    timeout = st.sidebar.number_input(
        "Set Timeout (seconds)",
        min_value=1,
        max_value=30,
        value=5,  # Default timeout
        help="Maximum time to wait for speech to start."
    )

    phrase_time_limit = st.sidebar.number_input(
        "Set Phrase Time Limit (seconds)",
        min_value=1,
        max_value=60,
        value=10,  # Default time limit for speech
        help="Maximum duration for each speech input."
    )

    # Main app interface
    st.write("Configure your settings in the sidebar and click 'Start Recording'.")

    # Start recording button
    if st.button("Start Recording"):
        text = app.transcribe_speech(api_choice, language_choice, timeout, phrase_time_limit)

        # Display the transcription
        st.write("### Transcription: ")
        st.write(text)

        # Provide a download button
        if text:
            st.download_button(
                label="Download Transcription",
                data=app.create_download_file(text),
                file_name=f"transcription_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain"
            )

if __name__ == "__main__":
    main()
