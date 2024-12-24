# Speech-Recognition-App
This is a simple speech recognition app built using **Streamlit** and **SpeechRecognition** libraries. The app allows users to transcribe speech into text, select different speech recognition APIs, choose a language, set timeouts, and download the transcription file.

## Features
- **Multiple Speech Recognition APIs**: Google Speech Recognition and Sphinx (Offline).
- **Language Selection**: Choose from multiple languages (English, Spanish, French, German, Chinese).
- **Customizable Settings**: Configure timeout settings and phrase time limits.
- **Downloadable Transcription**: After transcription, users can download the transcribed text in a `.txt` file.
- **User-Friendly Interface**: Built using Streamlit for an intuitive user interface.

## **Code Structure:**
Enhanced_Speech_Recog_App.py
This is the main script that contains the Streamlit UI, handles speech recognition, and controls the flow of the app. It:
- Initializes the SpeechRecognitionApp class.
- Handles the logic for choosing the API, setting language preferences, and capturing/transcribing speech.
- Displays the transcription and provides a download link.

## **Adjust Settings:**
You can configure the following settings:
Timeout: Set the maximum time (in seconds) the app waits for speech to start.
Phrase Time Limit: Set the maximum duration (in seconds) for each speech input.

## **Start Recording:**
Click the Start Recording button to start the speech recognition process. The app will listen to your speech and transcribe it into text.

## **Download Transcription:**
Once the speech has been transcribed, the app displays the text and provides a button to download the transcription as a .txt file.

## **Future Improvements:**
- Add punctuation restoration to transcriptions.
- Support for more languages and APIs.
- Enhanced offline recognition models for better accuracy.

## **Contributing:**
If you would like to contribute to the development of this project, feel free to fork the repository, make changes, and submit a pull request. Here are some ways you can contribute:
- Report bugs or issues.
- Suggest new features.
- Fix existing bugs or improve the codebase.

**Please make sure to test your changes before submitting a pull request!**

## Installation
### Clone the Repository:
To get started, clone the repository to your local machine:
```bash
git clone https://github.com/HisLikeness/Speech-Recognition-App.git
cd Enhanced_Speech_Recog_App.py
