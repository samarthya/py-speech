# Speech Recognition Program

Welcome to the Speech Recognition Program repository! This project implements a Python-based speech recognition tool that transcribes speech, performs spell checking, and saves the output to a Word document.

## Features

- Real-time speech recognition
- Automatic spell checking
- Output to Microsoft Word document
- Voice command to stop the program

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.12 or higher
- pip (Python package installer)

## Installation

Follow these steps to set up the Speech Recognition Program:

1. Clone the repository:

   ```bash
   git clone https://github.com/samarthya/py-speech.git
   cd py-speech
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install SpeechRecognition python-docx pyspellchecker pyaudio
   ```

   Note: If you encounter issues installing `pyaudio`, follow these OS-specific instructions:

   - **macOS**:

     ```bash
     brew install portaudio
     pip install pyaudio
     ```

   - **Linux (Ubuntu/Debian)**:

     ```bash
     sudo apt-get update
     sudo apt-get install python3-dev python3-pip portaudio19-dev
     pip install pyaudio
     ```

   - **Windows**:

     ```bash
     pip install pipwin
     pipwin install pyaudio
     ```

## Usage

To run the Speech Recognition Program:

1. Navigate to the project directory:

   ```bash
   cd py-speech
   ```

2. Run the script:

   ```bash
   python main.py
   ```

3. Start speaking. The program will transcribe your speech in real-time.

4. To stop the program, say "program stop".

5. The transcribed and spell-checked text will be saved in a file named `output.docx` in the same directory.

## How It Works

The program uses the following components:

- `speech_recognition`: For converting speech to text
- `python-docx`: For creating and writing to Word documents
- `pyspellchecker`: For spell checking the transcribed text

The main script performs the following steps:

1. Listens to audio input from the microphone
2. Transcribes the audio to text
3. Performs spell checking on the transcribed text
4. Saves the corrected text to a Word document

## Contributing

Contributions to the Speech Recognition Program are welcome! Here are a few ways you can help:

1. Report bugs
2. Suggest new features
3. Submit pull requests

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) library
- [python-docx](https://python-docx.readthedocs.io/) library
- [pyspellchecker](https://pypi.org/project/pyspellchecker/) library

Happy transcribing!
