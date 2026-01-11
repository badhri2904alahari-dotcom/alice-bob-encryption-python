# Alice & Bob - Placement Interns

morse_map = {
    'A': '._',   'B': '_...', 'C': '_._.', 'D': '_..',  'E': '.',
    'F': '.._.', 'G': '__.',  'H': '....', 'I': '..',   'J': '.___',
    'K': '_._',  'L': '._..', 'M': '__',   'N': '_.',   'O': '___',
    'P': '.__.', 'Q': '__._', 'R': '._.',  'S': '...',  'T': '_',
    'U': '.._',  'V': '..._', 'W': '.__',  'X': '_.._', 'Y': '_.__',
    'Z': '__..'
}

code_map = {}
for letter, code in morse_map.items():
    if code not in code_map:
        code_map[code] = []
    code_map[code].append(letter)


def find_all_decodings(encrypted_text):
    """
    Finds all possible decoded strings for the given encrypted message.
    """
    decoded_results = []
    text_length = len(encrypted_text)

    def backtrack(position, current_word):
        if position == text_length:
            decoded_results.append(current_word)
            return

        for code, letters in code_map.items():
            if encrypted_text.startswith(code, position):
                for ch in letters:
                    backtrack(position + len(code), current_word + ch)

    backtrack(0, "")
    return sorted(decoded_results)



encrypted_message = input().strip()

answers = find_all_decodings(encrypted_message)
for word in answers:
    print(word)
