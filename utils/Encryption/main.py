import pyperclip


def encryption(text, alphabet_dict):
    encryption_list = []
    alphabet_dict = alphabet_dict
    for i in text:
        if i in alphabet_dict.keys():
            get_keys = alphabet_dict.get(i)
            encryption_list.append(str(get_keys))
    str_encryption = ''.join(encryption_list)
    pyperclip.copy(str_encryption)
    return str_encryption


def decoding(numbers, alphabet_dict):
    words_code = []
    alphabet_dict = alphabet_dict
    for i in range(0, len(numbers), 4):
        words_code.append(numbers[i:i + 4])
    letters = []
    for i in words_code:
        keys = [key for key, value in alphabet_dict.items() if str(value) == i]
        if keys:
            letters.extend(keys)
    join_str = ''.join(letters)
    return join_str
