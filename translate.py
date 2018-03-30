CHANGE_LETTERS = {
    'b': 'f', 'j': 'f', 'p': 'f', 's': 'f', 'x': 'f', 'v': 'f', 'z': 'f', 'ç': 'f',
    'B': 'F', 'J': 'F', 'P': 'F', 'S': 'F', 'X': 'F', 'V': 'F', 'Z': 'F', 'Ç': 'F',
    'ci': 'fi', 'ce': 'fe', 'CI': 'FI', 'CE': 'FE', 'Ci': 'Fi', 'Ce': 'Fe'
    }

def remove_repeated(text):
    flag = False
    new_text = ''
    for i in range(len(text)):
        if (text[i] == 'F' or text[i] == 'f') and flag == False:
            flag = True
        elif (text[i] == 'F' or text[i] == 'f') and flag == True:
            continue
        else:
            flag = False
        new_text += text[i]
    return new_text

def translate(text, remove=True):
    for letter in CHANGE_LETTERS:
        text = text.replace(letter, CHANGE_LETTERS[letter])
    if remove:
        text = remove_repeated(text)
    return text
