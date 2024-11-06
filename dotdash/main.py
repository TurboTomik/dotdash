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


def encoding(text: str, morse_dict: dict = char2morse):
    text = text.upper()
    output = ""
    for word in text.split():
        word_morse = " ".join([morse_dict[letter] for letter in word])
        output += f"{word_morse}   "
    return output.rstrip()


def decoding(code: str, morse_dict: dict = morse2char):
    output = ""
    for word_morse in code.split("   "):
        word = "".join([morse_dict[letter] for letter in word_morse.split()])
        output += f"{word} "
    return output.rstrip().lower()
