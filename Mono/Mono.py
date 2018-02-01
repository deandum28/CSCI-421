import string
from random import shuffle


def generate_monoalpha_cipher(key):
    original_pool = list(string.ascii_lowercase)
    shuffled_pool = list()
    for letter in key:
        shuffled_pool.append(letter)
    print(original_pool)
    print(shuffled_pool)
    return dict(zip(original_pool, shuffled_pool))


def inverse(monoalpha_cipher):
    inverse_monoalpha = {}
    for key, value in monoalpha_cipher.iteritems():
        inverse_monoalpha[value] = key
    return inverse_monoalpha


def encrypt(message, monoalpha_cipher):
    encrypted_message = []
    for letter in message:
        if letter.isspace():
            encrypted_message.append(letter)
        elif not letter.isalpha():
            encrypted_message.append(letter)
        else:
            isUp = 0
            if letter.isupper():
                letter = letter.lower()
                isUp = 1
            encrypted_letter = monoalpha_cipher.get(letter, letter)
            if isUp:
                encrypted_letter = encrypted_letter.upper()
            encrypted_message.append(encrypted_letter)
    return ''.join(encrypted_message)


def decrypt(encrypted_message, monoalpha_cipher):
    return encrypt(
               encrypted_message,
               inverse(monoalpha_cipher)
           )
