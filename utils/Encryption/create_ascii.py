import random
import string


def generate_alphabet_dict():
    alphabet = string.ascii_letters
    alphabet_dict = {}
    alphabet_dict[" "] = 9999
    chars = list("!@#$%^&*()_-+={}[]/?.,~`")
    numbers = list(range(1000, 9951))
    random.shuffle(numbers)
    for letter in alphabet:
        alphabet_dict[letter] = numbers.pop()
    for char in chars:
        alphabet_dict[char] = numbers.pop()
    return alphabet_dict
