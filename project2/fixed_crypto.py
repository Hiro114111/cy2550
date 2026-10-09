# Fixed version of ai_crypto.py
# Only change: the key now comes from a passphrase using PBKDF2 with a
# random salt, and the salt is saved in the file so decryption works later.

import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes


def make_key(passphrase, salt):
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=600000)
    return kdf.derive(passphrase.encode())


def encrypt_file(input_path, output_path, passphrase):
    with open(input_path, "rb") as f:
        plaintext = f.read()

    salt = os.urandom(16)
    key = make_key(passphrase, salt)
    nonce = os.urandom(12)
    ciphertext = AESGCM(key).encrypt(nonce, plaintext, None)

    with open(output_path, "wb") as f:
        f.write(salt + nonce + ciphertext)


def decrypt_file(input_path, output_path, passphrase):
    with open(input_path, "rb") as f:
        data = f.read()

    salt = data[:16]
    nonce = data[16:28]
    ciphertext = data[28:]
    key = make_key(passphrase, salt)
    plaintext = AESGCM(key).decrypt(nonce, ciphertext, None)

    with open(output_path, "wb") as f:
        f.write(plaintext)


if __name__ == "__main__":
    encrypt_file("secret.txt", "secret.txt.enc", "mypassphrase")
    decrypt_file("secret.txt.enc", "secret_decrypted.txt", "mypassphrase")
