def vigenere_header(alphabet):
    alpha_len = len(alphabet)
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
        elif c.upper() in alphabet:
            cipher_text += index_to_letter(vigenere_index(key[counter%len(key)], c, alphabet), alphabet)
            counter += 1
    return cipher_text

def decrypt_vigenere(key, cipher_text, alphabet):
    plain_text = ""
    counter = 0
    for c in cipher_text:
        if c == " ":
            plain_text += " "
        elif c.upper() in alphabet:
            plain_text += index_to_letter(undo_vigenere_index(key[counter%len(key)], c, alphabet), alphabet)
            counter += 1
    return plain_text

def check_valid_key(key, alphabet):
    for i in key:
        if not i in alphabet: return False
    return len(key) > 0

def enter(prompt="Press ENTER to continue.."):
    input(prompt)

# Var
key = "BLUESMURF"
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Main
while True:
    print(f"""
    *******************
    * Vigenère Cipher *
    *******************

    1)Encrypt Message
    2)Decrypt Message
    3)Change Keyword(current:{key})
    4)View Vigenère Square
    5)Exit Program
    """)
    print()
    try:
        selection = int(input("Please enter a number from the list: "))
    except ValueError:
        selection = 0

    if selection == 1:
        message = input("Please enter your message: ")
        print(f"""
        Encrypted message:
        
        {encrypt_vigenere(key, message, alphabet)}
        
        """)
        enter()
    elif selection == 2:
        message = input("Please enter your encrypted message: ")
        print(f"""
        Decrypted message:

        {decrypt_vigenere(key, message, alphabet)}

        """)
        enter()
    elif selection == 3:
        while True:
            new_key = input("Please enter a new keyword using only letters in the alphabet: ")
            if check_valid_key(new_key.upper(), alphabet):
                key = new_key.upper()
                print("New keyword:", key)
                enter()
                break
            else:
                print("*Invalid keyword*")
    elif selection == 4:
        vigenere_sq(alphabet)
        enter()
    elif selection == 5:
        break