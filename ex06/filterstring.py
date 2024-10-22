from ft_filter import ft_filter
import sys


def main():
    """
    Main function that processes command line arguments and filters words.
    Prints words from the input string that are longer than specified length.
    """
    try:
        assert len(sys.argv) == 3, "the arguments are bad"

        string = sys.argv[1]
        n = sys.argv[2]

        assert isinstance(string, str), "the arguments are bad"
        assert n.isdigit(), "the arguments are bad"
        n = int(n)

        words = string.split()
        filtered_words = list(ft_filter(lambda x: len(x) > n, words))

        print(filtered_words)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return 1
    return 0


if __name__ == "__main__":
    main()
