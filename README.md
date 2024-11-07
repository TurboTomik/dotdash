# Morse Code Encoder-Decoder

This project provides a tool for encoding and decoding Morse code. It allows users to input text in the Latin alphabet, which it converts to Morse code, and vice versa. Additionally, it supports strict mode, where unsupported characters raise errors, as well as a forgiving mode, where unsupported characters are ignored.

## Features

* **Encoding**: Converts Latin alphabet text to Morse code.
* **Decoding**: Converts Morse code back to Latin alphabet text.
* **Error Handling**: Offers a strict mode to raise errors for unsupported characters or Morse symbols.
* **User Input Detection**: Automatically detects if the input is Morse code or plain text.

## Usage

Run the script to enter the interactive mode, which supports both Morse and text input.

* To encode, enter text using Latin letters or numbers (case-insensitive).
* To decode, enter valid Morse code using `.` and `-` with spaces separating letters and three spaces separating words.

### Examples

1. Text to Morse Encoding

   * Input: `Hello World`
   * Output: `'.... . .-.. .-.. --- .-- --- .-. .-.. -..'`
2. Morse to Text Decoding

   * Input: `'.... . .-.. .-.. --- .-- --- .-. .-.. -..'`
   * Output: `hello world`

### Interactive Mode

Upon running the program:

* Type text to get it encoded as Morse code.
* Type Morse code to decode it to text.
* Type "exit" to quit the program.

## Functions

### `is_morse_code(text: str) -> bool`

Helper function that checks if the input text is Morse code (contains only `.` and `-` characters).

### `encoding(text: str, strict: bool = False, morse_dict: dict = char2morse) -> str`

Encodes a text string into Morse code, using the following parameters:

* `text`: The text to convert.
* `strict`: If `True`, raises an error for unsupported characters.
* `morse_dict`: A dictionary mapping Latin characters to Morse code symbols.

### `decoding(code: str, strict: bool = False, morse_dict: dict = morse2char) -> str`

Decodes a Morse code string back to Latin text, using the following parameters:

* `code`: The Morse code string.
* `strict`: If `True`, raises an error for unsupported Morse code symbols.
* `morse_dict`: A dictionary mapping Morse code symbols to Latin characters.

### `user_input()`

Handles user interaction and automatically detects whether the input is Morse code or text, then encodes or decodes accordingly.

## Requirements

No additional libraries are required; this project runs on any standard Python 3 environment.

## Running the Project

To start the interactive mode, simply execute:

```bash
python main.py
```

## Contributing

Feel free to submit pull requests with improvements, bug fixes, or new features.

## License

This project is licensed under the MIT License.
