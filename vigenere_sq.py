def vigenere_header(alphabet):
    alpha_len = len(alphabet)
    print("|   ", end='')
    for i in range(alpha_len):
        if i < 9:
            print(f"| {i+1}", end=' ')
        else:
            print(f"| {i+1}", end='')
    print("|")
    print("|   ", end='')
    for i in range(alpha_len):
        print(f"| {alphabet[i]}", end=' ')
    print("|")
    print(f"{'|---'*(alpha_len + 1)}|")

def vigenere_sq(alphabet):
    alpha_len=len(alphabet)
    vigenere_header(alphabet)
    for shift in range(alpha_len):
        for i in range(alpha_len):
            if i == 0:
                print(f"| {alphabet[(i + shift) % alpha_len]}", end=' ')
                print(f"| {alphabet[(i + shift) % alpha_len]}", end=' ')
            else:
                print(f"| {alphabet[(i + shift) % alpha_len]}", end=' ')
        print("|")

def letter_to_index(letter, alphabet):
    return alphabet.index(letter.upper())

def index_to_letter(index:int, alphabet:str):
    if 0 <= index <= len(alphabet):
        return alphabet[index]
    return ""

def vigenere_index(key_letter, plaintext_letter, alphabet):
    return (letter_to_index(key_letter, alphabet) +
            letter_to_index(plaintext_letter, alphabet)) % len(alphabet)

def undo_vigenere_index(key_letter, cipher_letter, alphabet):
    return (letter_to_index(cipher_letter, alphabet) -
            letter_to_index(key_letter, alphabet)) % len(alphabet)

def encrypt_vigenere(key, plaintext, alphabet):
    cipher_text = ""
    counter = 0
    for c in plaintext:
        if c == " ":
            cipher_text += " "
        elif (c.upper() in alphabet):
            cipher_text += index_to_letter(vigenere_index(key[counter%len(key)], c, alphabet), alphabet)
            counter += 1
    return cipher_text

def decrypt_vigenere(key, cipher_text, alphabet):
    plain_text = ""
    counter = 0
    for c in cipher_text:
        if c == " ":
            plain_text += " "
        elif (c.upper() in alphabet):
            plain_text += index_to_letter(undo_vigenere_index(key[counter%len(key)], c, alphabet), alphabet)
            counter += 1
    return plain_text

key = "BLUESMURF"
message = "Hello World, I am here"
alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#vigenere_sq(alphabet)

print()


a = message
print(a)
b = encrypt_vigenere(key, a, alphabet)
print(b)
c = decrypt_vigenere(key, b, alphabet)
print(c)