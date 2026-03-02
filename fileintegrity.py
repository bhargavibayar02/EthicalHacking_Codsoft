#!/usr/bin/env python3
"""
File Integrity Checker
Author: Bhargavi
Description: Monitors file changes by calculating and comparing hash values.
"""

import hashlib
import logging
from pathlib import Path

# Configure logging for professional output
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

class FileIntegrityChecker:
    def __init__(self, algorithm="sha256"):
        """
        Initialize the checker with a chosen hashing algorithm.
        Default: SHA-256
        """
        self.algorithm = algorithm

    def calculate_hash(self, file_path: str) -> str:
        """
        Calculate the hash of a file using the chosen algorithm.
        Returns the hexadecimal hash string.
        """
        file = Path(file_path)
        if not file.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        hash_func = hashlib.new(self.algorithm)
        with open(file, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_func.update(chunk)
        return hash_func.hexdigest()

    def verify_integrity(self, file_path: str, reference_hash: str) -> bool:
        """
        Compare the current hash with a reference hash.
        Returns True if unchanged, False if modified.
        """
        current_hash = self.calculate_hash(file_path)
        if current_hash == reference_hash:
            logging.info("No changes detected. File integrity intact.")
            return True
        else:
            logging.warning("File has been modified!")
            logging.info(f"Expected: {reference_hash}")
            logging.info(f"Current : {current_hash}")
            return False

if __name__ == "__main__":
    checker = FileIntegrityChecker()
    file = input("Enter file path: ")
    ref = input("Enter reference hash (leave blank to generate): ")

    if ref:
        checker.verify_integrity(file, ref)
    else:
        hash_value = checker.calculate_hash(file)
        logging.info(f"Reference hash for {file}: {hash_value}")