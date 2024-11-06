char2morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}

morse2char = {morse: char for char, morse in char2morse.items()}


def encoding(text: str, morse_dict: dict = char2morse) -> str:
    """
    Converts a given Latin alphabet text into Morse code.

    Args:
        text (str): The text to be converted into Morse code.
                    Only letters and numbers are supported; input is case-insensitive.
        morse_dict (dict, optional): A dictionary mapping each Latin character
                                     to its corresponding Morse code symbol. Defaults to `char2morse`.

    Returns:
        str: The Morse code translation of the input text, with each letter separated by a
             single space and each word separated by three spaces.

    Example:
        >>> encoding("Hello World")
        '.... . .-.. .-.. ---   .-- --- .-. .-.. -..'
    """
    text = text.upper()
    output = ""
    for word in text.split():
        word_morse = " ".join([morse_dict[letter] for letter in word])
        output += f"{word_morse}   "
    return output.rstrip()


def decoding(code: str, morse_dict: dict = morse2char) -> str:
    """
    Converts a given Morse code string into Latin alphabet text.

    Args:
        code (str): The Morse code to be converted, where each letter in Morse code
                    is separated by a single space, and each word is separated by
                    three spaces.
        morse_dict (dict, optional): A dictionary mapping Morse code symbols
                                     to their corresponding Latin characters.
                                     Defaults to `morse2char`.

    Returns:
        str: The decoded Latin text in lowercase.

    Example:
        >>> decoding(".... . .-.. .-.. ---   .-- --- .-. .-.. -..")
        'hello world'
    """
    output = ""
    for word_morse in code.split("   "):
        word = "".join([morse_dict[letter] for letter in word_morse.split()])
        output += f"{word} "
    return output.rstrip().lower()


if __name__ == "__main__":

    def user_input():
        text = input("Enter text or morse code: ")
        is_morse = all(char in ".- " for char in text)
        if is_morse:
            print(f'From morse to text "{decoding(text)}"')
        else:
            print(f"From text to morse ({encoding(text)})")

    while True:
        user_input()
