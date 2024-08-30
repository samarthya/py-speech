# pylint: disable=invalid-name
"""Speech to text

"""
import speech_recognition as sr
from docx import Document
from spellchecker import SpellChecker


def listen_and_transcribe():
    """Listens to audio input from the microphone and transcribes it to text.

    Returns:
        str: The transcribed text.
    """
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Listening... Say 'program stop' to end the session.")

    full_text = []

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)

        while True:
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio).lower()
                print(f"Recognized: {text}")

                if "program stop" in text:
                    print("Stopping the program...")
                    break

                full_text.append(text)
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")

    return " ".join(full_text)


def spell_check(text):
    """Spell checks the given text and returns the corrected text.

    Args:
        text (str): The text to spell check.

    Returns:
        str: The spell checked text.
    """
    spell = SpellChecker()
    words = text.split()
    corrected_words = []

    for word in words:
        corrected_word = spell.correction(word)
        corrected_words.append(corrected_word)

    return " ".join(corrected_words)


def save_to_word(text, filename="output.docx"):
    """Saves the given text to a Word document.

    Args:
        text (str): The text to save.
        filename (str, optional): The name of the file to save to. Defaults to "output.docx".
    """
    doc = Document()
    doc.add_paragraph(text)
    doc.save(filename)
    print(f"Text saved to {filename}")
