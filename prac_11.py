def rc4_keystream(key):
    """Generate a pseudorandom keystream using the RC4 algorithm."""
    S =list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        yield S[(S[i] + S[j]) % 256]
def stream_cipher(plaintext, key):
    keystream = rc4_keystream(key)
    ciphertext = []
    for byte in plaintext:
        keystream_byte = next(keystream)
        ciphertext_byte = byte ^ keystream_byte
        ciphertext.append(ciphertext_byte)
    return bytes(ciphertext)
if __name__ == "__main__":
    plaintext = b"hi read this encrypted message"
    key = b"secretkey"
    ciphertext = stream_cipher(plaintext, key)
    print("Cipher Text ==> ",ciphertext)
    decrypted_plaintext = stream_cipher(ciphertext, key)
    print("Deciphered Text ==> ",decrypted_plaintext)
