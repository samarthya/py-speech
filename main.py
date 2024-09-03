"""Main function for the program.
"""

from sp import SpeechToText

def main():
    """Entry point for the program.

    """
    sp = SpeechToText()
    transcribed_text = sp.listen_and_transcribe()
    corrected_text = sp.spell_check(transcribed_text)
    sp.save_to_word(corrected_text)

if __name__ == "__main__":
    main()
