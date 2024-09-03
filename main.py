"""Main function for the program.
"""

from sp import SpeechToText

def main():
    """Entry point for the program.

    """
    speech_to_text = SpeechToText()  # Use default English language
    transcribed_text = speech_to_text.listen_and_transcribe()
    corrected_text = speech_to_text.spell_check(transcribed_text)
    speech_to_text.save_to_word(corrected_text)

if __name__ == "__main__":
    main()
