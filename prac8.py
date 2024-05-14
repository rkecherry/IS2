def encrypt_row_transposition(plain_text, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    encrypted_text = ''.join([plain_text[i::len(key)] for i in key_order])
    return encrypted_text


def decrypt_row_transposition(cipher_text, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    col_length = len(cipher_text) // len(key)
    plain_text = [''] * len(cipher_text)

    for i, k in enumerate(key_order):
        start = k * col_length
        end = start + col_length
        plain_text[start:end] = cipher_text[i::len(key_order)]

    return ''.join(plain_text)

def main():
    choice = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ").lower()
    if choice not in ['encrypt', 'decrypt']:
        print("Invalid choice.")
        return

    if choice == 'encrypt':
        text = input("Enter the plain text: ")
        key = input("Enter the key (e.g., '2314' for a 4-row transposition): ")
        print("Encrypted text:", encrypt_row_transposition(text, key))
    else:
        text = input("Enter the cipher text: ")
        key = input("Enter the key (e.g., '2314' for a 4-row transposition): ")
        print("Decrypted text:", decrypt_row_transposition(text, key))


if __name__ == "__main__":
    main()
    
