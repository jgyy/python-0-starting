def morse_encode(text: str) -> str:
    """
    Convert a string into Morse code.
    """
    MORSE_CODE = {
        'A': '.- ',
        'B': '-... ',
        'C': '-.-. ',
        'D': '-.. ',
        'E': '. ',
        'F': '..-. ',
        'G': '--. ',
        'H': '.... ',
        'I': '.. ',
        'J': '.--- ',
        'K': '-.- ',
        'L': '.-.. ',
        'M': '-- ',
        'N': '-. ',
        'O': '--- ',
        'P': '.--. ',
        'Q': '--.- ',
        'R': '.-. ',
        'S': '... ',
        'T': '- ',
        'U': '..- ',
        'V': '...- ',
        'W': '.-- ',
        'X': '-..- ',
        'Y': '-.-- ',
        'Z': '--.. ',
        '0': '----- ',
        '1': '.---- ',
        '2': '..--- ',
        '3': '...-- ',
        '4': '....- ',
        '5': '..... ',
        '6': '-.... ',
        '7': '--... ',
        '8': '---.. ',
        '9': '---.- ',
        ' ': '/ '
    }

    valid_chars = set(MORSE_CODE.keys()) | {' '}
    if not all(c.upper() in valid_chars for c in text):
        raise AssertionError("the arguments are bad")

    return ''.join(MORSE_CODE[c.upper()] for c in text).rstrip()


def main():
    """
    Main function to handle command line arguments and execute the program.
    """
    import sys

    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        return

    try:
        result = morse_encode(sys.argv[1])
        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
