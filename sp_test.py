"""Unit test
"""
import unittest
import os
from unittest.mock import patch

import speech_recognition as sr

from sp import spell_check, save_to_word, listen_and_transcribe


class TestSpeechRecognitionProgram(unittest.TestCase):
    """TestSpeechRecognitionProgram

    Args:
        unittest (_type_): _description_
    """

    def test_spell_check(self):
        """Test spell check functionality.
        """
        text = "This is a testt sentenc"
        corrected_text = spell_check(text)
        self.assertEqual(corrected_text, "This is a test sentence")

    def test_save_to_word(self):
        """Test save to word functionality.
        """
        text = "This is a test sentence."
        filename = "test_output.docx"
        save_to_word(text, filename)
        self.assertTrue(os.path.exists(filename))
        os.remove(filename)  # Clean up

    @patch('sp.sr.Recognizer')
    @patch('sp.sr.Microphone')
    def test_listen_and_transcribe(self, mock_microphone, mock_recognizer):
        """Test listening and transcribing audio.
        """
        # Mock the recognizer's listen and recognize_google methods
        mock_recognizer().listen.return_value = "audio_data"
        mock_recognizer().recognize_google.side_effect = [
            "this is a test",
            "program stop"
        ]

        result = listen_and_transcribe()
        self.assertEqual(result, "this is a test")

    def test_recognizer_unknown_value_error(self):
        """Test handling of UnknownValueError during recognition.
        """
        with patch('sp.sr.Recognizer') as mock_recognizer, \
             patch('sp.sr.Microphone'):
            mock_recognizer().listen.return_value = "audio_data"
            mock_recognizer().recognize_google.side_effect = [
                sr.UnknownValueError(),
                "program stop"
            ]

            result = listen_and_transcribe()
            self.assertEqual(result, "")

    def test_recognizer_request_error(self):
        """Test handling of RequestError during recognition.
        """
        with patch('sp.sr.Recognizer') as mock_recognizer, \
             patch('sp.sr.Microphone'):
            mock_recognizer().listen.return_value = "audio_data"
            mock_recognizer().recognize_google.side_effect = [
                sr.RequestError("Test error"),
                "program stop"
            ]

            result = listen_and_transcribe()
            self.assertEqual(result, "")


if __name__ == '__main__':
    unittest.main()
