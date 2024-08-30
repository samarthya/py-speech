"""Main function for the program.
"""

from sp import listen_and_transcribe, spell_check, save_to_word


def main():
    """Entry point for the program.

    """
    transcribed_text = listen_and_transcribe()
    corrected_text = spell_check(transcribed_text)
    save_to_word(corrected_text)

if __name__ == "__main__":
    main()
