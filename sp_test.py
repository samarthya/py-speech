"""Unit test
"""
import unittest
from unittest.mock import patch
import os
from sp import spell_check, save_to_word, listen_and_transcribe


class TestSpeechRecognitionProgram(unittest.TestCase):
    """TestSpeechRecognitionProgram

    Args:
        unittest (_type_): _description_
    """

    def test_spell_check(self):
        text = "This is a testt sentenc"
        corrected_text = spell_check(text)
        self.assertEqual(corrected_text, "This is a test sentence")

    def test_save_to_word(self):
        text = "This is a test sentence."
        filename = "test_output.docx"
        save_to_word(text, filename)
        self.assertTrue(os.path.exists(filename))
        os.remove(filename)  # Clean up

    @patch('sp.sr.Recognizer')
    @patch('sp.sr.Microphone')
    def test_listen_and_transcribe(self, mock_mic, mock_recognizer):
        # Mock the recognizer's listen and recognize_google methods
        mock_recognizer().listen.return_value = "audio_data"
        mock_recognizer().recognize_google.side_effect = [
            "this is a test",
            "program stop"
        ]

        result = listen_and_transcribe()
        self.assertEqual(result, "this is a test")


if __name__ == '__main__':
    unittest.main()
