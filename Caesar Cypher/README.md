### Core Rules

- **Alphabet Letters**: For each letter in the message, the cipher "shifts" it forward (for encoding) or backward (for decoding) in the alphabet by a fixed number (the "shift amount").
- **Symbols and Numbers**: If a character is a symbol or number (based on the `symbols` list), it is not changed—the cipher only shifts lowercase English letters found in the `alphabet` list.

### Encoding Rule

- For each letter:
  - If it's in the `symbols` list, add it as-is to the result.
  - If it's in the `alphabet`, calculate its new position by adding the shift amount to its index:
    - If this position goes past 'z', it wraps around to the start of the alphabet using `count - 26`.
    - Otherwise, simply use the new index.

### Decoding Rule

- For each letter:
  - If it's in the `symbols` list, add it as-is to the result.
  - If it's in the `alphabet`, calculate its new position by subtracting the shift amount from its index:
    - If this position is negative or below zero, it wraps backward using `count - 26` (note: this differs slightly from standard implementations and may be off-by-one for negative shifts).
    - Otherwise, simply use the new index.

### Additional Details

- **Case Insensitivity**: The message is converted to lowercase before encryption or decryption, so the cipher only works with lowercase letters.
- **User Input Loop**: After each operation, the user can choose to repeat or exit.
- **Shift Wrap Around**: Both encoding and decoding ensure wrap-around at the end of the alphabet, so after 'z' comes 'a', and decoding past 'a' wraps to 'z'.

### Summary Table

| Character Type            | Encoding/Decoding Action                                       |
|---------------------------|----------------------------------------------------------------|
| Alphabet Letter (`a`–`z`) | Shift forward/back by chosen amount, wrap around at 'z' or 'a' ||
| Number/Symbol             | No change, copied as-is                                        |

This approach makes the Caesar cipher more robust for modern usage, handling not just letters but also keeping symbols unchanged, which is useful for real-world messages that may include punctuation and digits.
