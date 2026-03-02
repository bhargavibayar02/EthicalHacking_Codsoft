#!/usr/bin/env python3
"""
Advanced Encryption Tool (AES-256)
Author: Bhargavi
Description: Encrypts and decrypts any file type (text, audio, video, images).
"""

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import logging
import os

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

class AESTool:
    def __init__(self, key_file="aes.key"):
        # Load existing key or generate a new one
        if os.path.exists(key_file):
            with open(key_file, "rb") as f:
                self.key = f.read()
            logging.info("Loaded existing AES key.")
        else:
            self.key = get_random_bytes(32)  # AES-256 key
            with open(key_file, "wb") as f:
                f.write(self.key)
            logging.info("Generated new AES key and saved to aes.key.")

    def encrypt_file(self, file_path: str):
        """Encrypt any file (text, audio, video, image)."""
        cipher = AES.new(self.key, AES.MODE_CBC)
        with open(file_path, "rb") as f:
            plaintext = f.read()
        ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

        enc_file = file_path + ".enc"
        with open(enc_file, "wb") as f:
            f.write(cipher.iv + ciphertext)

        logging.info(f"[ENCRYPTED] {file_path} -> {enc_file}")

    def decrypt_file(self, file_path: str):
        """Decrypt any file previously encrypted."""
        with open(file_path, "rb") as f:
            iv = f.read(16)
            ciphertext = f.read()
        cipher = AES.new(self.key, AES.MODE_CBC, iv=iv)
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

        dec_file = file_path.replace(".enc", ".dec")
        with open(dec_file, "wb") as f:
            f.write(plaintext)

        logging.info(f"[DECRYPTED] {file_path} -> {dec_file}")

if __name__ == "__main__":
    tool = AESTool()
    choice = input("Encrypt or Decrypt (E/D): ").upper().strip()
    file = input("Enter file path: ").strip()

    if choice == "E":
        tool.encrypt_file(file)
    elif choice == "D":
        tool.decrypt_file(file)
    else:
        logging.error("Invalid choice. Please enter E or D.")