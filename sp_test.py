"""Unit test for sp.py
"""
import os

import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
import speech_recognition as sr
from sp import SpeechToText


class TestSpeechToText(unittest.TestCase):
    """Test cases for SpeechToText class."""

    def setUp(self):
        """Setup for test methods."""
        self.speech_to_text = SpeechToText("en_US")
        self.test_filename = "test_output.docx"  # Define filename here

    def tearDown(self):
        """Cleanup after test methods."""
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_spell_check(self):
        """Test spell check functionality."""
        text = "This is a testt sentenc"
        corrected_text = self.speech_to_text.spell_check(text)
        self.assertEqual(corrected_text, "This is a test sentence")

    def test_save_to_word(self):
        """Test saving text to a Word document."""
        text = "This is a test sentence."
        filename = "test_output.docx"
        self.speech_to_text.save_to_word(text, filename)
        self.assertTrue(os.path.exists(self.test_filename))

    @parameterized.expand([
        (["this is a test",
            "program stop"], "this is a test"),
        (["program stop"], ""),
    ])
    def test_listen_and_transcribe(self, mock_responses, expected_result):
        """Test listening and transcribing audio."""
        with patch('speech_recognition.Recognizer.listen') as mock_listen, \
                patch('speech_recognition.Recognizer.recognize_google') as mock_recognize_google:
            mock_listen.return_value = "audio_data"
            mock_recognize_google.side_effect = mock_responses
            result = self.speech_to_text.listen_and_transcribe()
            self.assertEqual(result, expected_result)

    @patch('speech_recognition.Recognizer.listen')
    @patch('speech_recognition.Recognizer.recognize_google')
    def test_listen_and_transcribe_empty(self, mock_recognize_google, mock_listen):
        """Test listening and transcribing when no input is given."""
        mock_listen.return_value = "audio_data"
        mock_recognize_google.side_effect = ["program stop"]
        result = self.speech_to_text.listen_and_transcribe()
        self.assertEqual(result, "")

    @patch('speech_recognition.Recognizer.recognize_google')
    @patch('speech_recognition.Recognizer.listen')
    def test_listen_and_transcribe_exception(self, mock_listen, mock_recognize_google):
        """Test handling of UnknownValueError during recognition."""
        mock_listen.side_effect = [
            MagicMock(), sr.UnknownValueError(), MagicMock()
        ]  # Use a list to iterate through side effects
        mock_recognize_google.side_effect = ["test", "program stop"]

        result = self.speech_to_text.listen_and_transcribe()
        self.assertEqual(result, "test")

    @patch('speech_recognition.Recognizer.recognize_google')
    @patch('speech_recognition.Recognizer.listen')
    def test_listen_and_transcribe_request_error(self, mock_listen, mock_recognize_google):
        """Test handling of RequestError during recognition."""
        mock_listen.side_effect = [
            MagicMock(), sr.RequestError("Test error"), MagicMock(), MagicMock()
        ]
        mock_recognize_google.side_effect = ["test", "test2", "program stop"]


        result = self.speech_to_text.listen_and_transcribe()
        self.assertEqual(result, "test test2")



if __name__ == '__main__':
    unittest.main()
