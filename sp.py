# pylint: disable=invalid-name
"""Speech to text

"""
import speech_recognition as sr
import logging
from docx import Document
from spellchecker import SpellChecker

# Create and configure logger
logging.basicConfig(filename='speech_to_text.log',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class SpeechToText:
    """
    A class to handle speech recognition, spell checking, and saving to a Word document.
    """

    def __init__(self, language="en-US"):
        """
        Initializes the SpeechToText object.

        Args:
            language (str, optional): The language to use for speech recognition. Defaults to "en-US".
        """
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.language = language
        logging.debug(
            'SpeechToText object initialized with language: %s', language)


    def listen_and_transcribe(self):
        """
        Listens to audio input from the microphone and transcribes it to text.

        Returns:
            str: The transcribed text.
        """
        logging.info("Starting listening session...")
        print("Listening... Say 'program stop' to end the session.")

        full_text = []

        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)

            while True:
                try:
                    audio = self.recognizer.listen(source)
                    text = self.recognizer.recognize_google(
                        audio, language=self.language).lower()

                    print(f"Recognized: {text}")
                    logging.debug('Recognized text: %s', text)

                    if "program stop" in text:
                        print("Stopping the program...")
                        break

                    full_text.append(text)
                except sr.UnknownValueError:
                    print("Could not understand audio")
                    logging.warning("Could not understand audio")
                except sr.RequestError as request_error:
                    print(f"Could not request results; {request_error}")
                    logging.error("Could not request results: %s", request_error)


        return " ".join(full_text)

    def spell_check(self, text):
        """
        Spell checks the given text and returns the corrected text.

        Args:
            text (str): The text to spell check.

        Returns:
            str: The spell checked text.
        """
        logging.debug('Spell checking text: %s', text)
        spell = SpellChecker()
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = spell.correction(word)
            corrected_words.append(corrected_word)


        logging.debug('Corrected text: %s', " ".join(corrected_words))
        return " ".join(corrected_words)

    def save_to_word(self, text, filename="output.docx"):
        """
        Saves the given text to a Word document.

        Args:
            text (str): The text to save.
            filename (str, optional): The name of the file to save to. Defaults to "output.docx".
        """
        logging.info('Saving text to file: %s', filename)
        doc = Document()
        doc.add_paragraph(text)
        doc.save(filename)
        print(f"Text saved to {filename}")


# Example usage:
if __name__ == "__main__":
    speech_to_text = SpeechToText()  # Use default English language
    transcribed_text = speech_to_text.listen_and_transcribe()
    corrected_text = speech_to_text.spell_check(transcribed_text)
    speech_to_text.save_to_word(corrected_text)
