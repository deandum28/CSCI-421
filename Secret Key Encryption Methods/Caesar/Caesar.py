import string


def generate_caesar_cipher(key):
    original_pool = list(string.ascii_lowercase)
    shuffled_pool = list()
    if key > 26:
        key = key % 26
    for letter in original_pool:
        shift = ord(letter) + key
        if shift > ord('z'):
            shift -= 26
        shuffled_pool.append(chr(shift))
    return dict(zip(original_pool, shuffled_pool))


def inverse(caesar_cipher):
    inverse_caesar = {}
    for key, value in caesar_cipher.iteritems():
        inverse_caesar[value] = key
    return inverse_caesar


def encrypt(message, caesar_cipher):
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
            encrypted_letter = caesar_cipher.get(letter, letter)
            if isUp:
                encrypted_letter = encrypted_letter.upper()
            encrypted_message.append(encrypted_letter)
    return ''.join(encrypted_message)


def decrypt(encrypted_message, caesar_cipher):
    return encrypt(
               encrypted_message,
               inverse(caesar_cipher)
           )
