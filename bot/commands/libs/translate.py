CHANGE_LETTERS = {
    'b': 'f', 'j': 'f', 'p': 'f', 's': 'f', 'x': 'f', 'v': 'f', 'z': 'f', 'ç': 'f',
    'B': 'F', 'J': 'F', 'P': 'F', 'S': 'F', 'X': 'F', 'V': 'F', 'Z': 'F', 'Ç': 'F',
    'ci': 'fi', 'ce': 'fe', 'CI': 'FI', 'CE': 'FE', 'Ci': 'Fi', 'Ce': 'Fe'
}


def remove_repeated(text):
    while text != text.replace('ff', 'f'):
        text = text.replace('ff', 'f')
    return text


def translate(text, remove=True):
    for letter in CHANGE_LETTERS:
        if letter in text:
            text = text.replace(letter, CHANGE_LETTERS[letter])
    if remove:
        text = remove_repeated(text)
    return text
