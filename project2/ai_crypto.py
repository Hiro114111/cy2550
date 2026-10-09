# AI assistant: Claude (Anthropic), model Claude Opus 5.5
# Prompt: "Write me a Python function that encrypts a file with AES."
#
# Response:

import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def encrypt_file(input_path, output_path, key):
    """
    Encrypt a file with AES-256-GCM.

    key: 32 bytes (e.g. from AESGCM.generate_key(bit_length=256))
    Output file format: 12-byte nonce + ciphertext (with 16-byte auth tag)
    """
    if len(key) != 32:
        raise ValueError("Key must be 32 bytes for AES-256")

    with open(input_path, "rb") as f:
        plaintext = f.read()

    aesgcm = AESGCM(key)
    nonce = os.urandom(12)  # must be unique for every encryption with the same key
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)

    with open(output_path, "wb") as f:
        f.write(nonce + ciphertext)


def decrypt_file(input_path, output_path, key):
    with open(input_path, "rb") as f:
        data = f.read()

    nonce = data[:12]
    ciphertext = data[12:]

    aesgcm = AESGCM(key)
    plaintext = aesgcm.decrypt(nonce, ciphertext, None)  # raises if tampered

    with open(output_path, "wb") as f:
        f.write(plaintext)


if __name__ == "__main__":
    key = AESGCM.generate_key(bit_length=256)
    encrypt_file("secret.txt", "secret.txt.enc", key)
    decrypt_file("secret.txt.enc", "secret_decrypted.txt", key)
    # Install with: pip install cryptography
