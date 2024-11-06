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


def encoding(text: str, strict: bool = False, morse_dict: dict = char2morse) -> str:
    """
    Converts a given Latin alphabet text into Morse code.

    Args:
        text (str): The text to be converted into Morse code.
                    Only letters and numbers are supported; input is case-insensitive.
        strict (bool, optional): If True, raises an error for characters not in the Morse dictionary.
                                 If False, ignores unsupported characters. Defaults to False.
        morse_dict (dict, optional): A dictionary mapping each Latin character
                                     to its corresponding Morse code symbol. Defaults to `char2morse`.

    Returns:
        str: The Morse code translation of the input text, with each letter separated by a
             single space and each word separated by three spaces. Unsupported characters
             are ignored if `strict` is False.

    Example:
        >>> encoding("Hello World")
        '.... . .-.. .-.. ---   .-- --- .-. .-.. -..'
        
        >>> encoding("Hello!", strict=True)
        Raises KeyError if '!' is not in the Morse dictionary.
    """
    text = text.upper()
    output = ""
    for word in text.split():
        if strict:
            word_morse = " ".join([morse_dict[letter] for letter in word])
        else:
            word_morse = " ".join([morse_dict.get(letter, "") for letter in word])
        output += f"{word_morse}   "
    return output.rstrip()


def decoding(code: str, strict: bool = False, morse_dict: dict = morse2char) -> str:
    """
    Converts a given Morse code string into Latin alphabet text.

    Args:
        code (str): The Morse code to be converted, where each letter in Morse code
                    is separated by a single space, and each word is separated by
                    three spaces.
        strict (bool, optional): If True, raises an error for Morse code symbols not found in the dictionary.
                                 If False, ignores unsupported Morse code symbols. Defaults to False.
        morse_dict (dict, optional): A dictionary mapping Morse code symbols to their corresponding Latin characters.
                                     Defaults to `morse2char`.

    Returns:
        str: The decoded Latin text in lowercase. Unsupported Morse code symbols are ignored if `strict` is False.

    Example:
        >>> decoding(".... . .-.. .-.. ---   .-- --- .-. .-.. -..")
        'hello world'
        
        >>> decoding(".... . .-.. .-.. --- ---..", strict=True)
        Raises KeyError if '---..' is not in the Morse dictionary.
    """
    output = ""
    for word_morse in code.split("   "):
        if strict:
            word = "".join([morse_dict[letter] for letter in word_morse.split()])
        else:
            word = "".join(
                [morse_dict.get(letter, "") for letter in word_morse.split()]
            )
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
