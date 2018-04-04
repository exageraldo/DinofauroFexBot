from . import IPSUM
from random import randint

def load_ipsum_file(file_name="ipsum"):
    ipsum_words = IPSUM.split()
    return ipsum_words


def paragraph_generator(words):
    ipsum_words = load_ipsum_file()
    ipsum_text = []
    for w_index in range(words):
        random_pos = randint(0, len(ipsum_words)-1)
        ipsum_text.append(ipsum_words[random_pos])
    ipsum_text = ' '.join(ipsum_text)
    ipsum_text = ipsum_text.replace('.', '')
    ipsum_text = ipsum_text.replace(',', '')
    ipsum_text = ipsum_text.capitalize()
    ipsum_text += '.\n\n'
    return ipsum_text


def ipsum_generator(paragraphs, words=100):
    ipsum_result = ""
    for p_index in range(paragraphs):
        ipsum_result += paragraph_generator(words)
    return ipsum_result

