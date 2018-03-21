import string
import sys

ALPHA_LIMIT = 25

def generate_vigenere_cipher():
    original_pool = list(string.ascii_lowercase)
    shift_pool = list()
    count = 0
    for letter in original_pool:
        shift_pool.append(count)
        count = count + 1
    return dict(zip(original_pool, shift_pool))


def encrypt(message, cipher, key):
    shift = []
    for letter in key:
        shift.append(cipher.get(letter, letter))
    encrypted_message = []
    count = 0
    encrypted_value = 0
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
            letter_value = cipher.get(letter)
            if letter_value + shift[count] <= ALPHA_LIMIT:
                encrypted_value = letter_value + shift[count]
            else:
                encrypted_value = letter_value + shift[count] - ALPHA_LIMIT - 1
            encrypted_letter = (search_encrypted_letter(encrypted_value, cipher))
            if isUp:
                encrypted_letter = encrypted_letter.upper()
            encrypted_message.append(encrypted_letter)
            if count+1 < len(shift):
                count = count + 1
            else:
                count = 0
    return ''.join(encrypted_message)


def decrypt(message, cipher, key):
    shift = []
    for letter in key:
        shift.append(cipher.get(letter, letter))
    decrypted_message = []
    count = 0
    encrypted_value = 0
    for letter in message:
        if letter.isspace():
            decrypted_message.append(letter)
        elif not letter.isalpha():
            decrypted_message.append(letter)
        else:
            isUp = 0
            if letter.isupper():
                letter = letter.lower()
                isUp = 1

            letter_value = cipher.get(letter)
            if letter_value - shift[count] >= 0:
                encrypted_value = letter_value - shift[count]
            else:
                encrypted_value = ALPHA_LIMIT - (shift[count] - letter_value) + 1
            encrypted_letter = (search_encrypted_letter(encrypted_value, cipher))
            if isUp:
                encrypted_letter = encrypted_letter.upper()
            decrypted_message.append(encrypted_letter)
            if count + 1 < len(shift):
                count = count + 1
            else:
                count = 0
    return ''.join(decrypted_message)


def search_encrypted_letter(value, cipher):
    for i in cipher:
        if cipher[i] == value:
            return i
