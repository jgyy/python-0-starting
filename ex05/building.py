import sys
import string


def count_characters(text: str) -> dict:
    """
    Count different types of characters in the given text.
    """
    counts = {
        'upper': sum(1 for c in text if c.isupper()),
        'lower': sum(1 for c in text if c.islower()),
        'punct': sum(1 for c in text if c in string.punctuation),
        'space': sum(1 for c in text if c.isspace()),
        'digit': sum(1 for c in text if c.isdigit())
    }
    return counts


def display_results(text: str, counts: dict) -> None:
    """
    Display the character count results in the required format.
    """
    total = len(text)
    print(f"The text contains {total} characters:")
    print(f"{counts['upper']} upper letters")
    print(f"{counts['lower']} lower letters")
    print(f"{counts['punct']} punctuation marks")
    print(f"{counts['space']} spaces")
    print(f"{counts['digit']} digits")


def main():
    """
    Main function that handles the program logic and error cases.
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument provided")
        if len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            print("What is the text to count?")
            text = input()
            if not text:
                return
        counts = count_characters(text)
        display_results(text, counts)
    except AssertionError as e:
        print(f"AssertionError: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
