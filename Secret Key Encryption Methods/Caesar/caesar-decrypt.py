import Caesar
import sys

if len(sys.argv) <= 1:
    print "I need a key!"
    sys.exit(1)

key = int(sys.argv[1])

text = ""

if len(sys.argv) == 2:
    text = sys.stdin.read()
else:
    with open(sys.argv[2]) as file:
        text = file.read()

cipher = Caesar.generate_caesar_cipher(key)
dec_text = Caesar.decrypt(text, cipher)
print(dec_text)

open('decrypted-text.txt', 'w').close()
with open("decrypted-text.txt", 'a') as out:
    out.write(dec_text)
