CodTech Internship – Cybersecurity and Ethical Hacking Tasks

Intern Name: Bhargavi
Domain: CS & EH
Organization: CodTech


 Overview

This repository contains the cybersecurity and Ethical Hacking internship tasks completed as part of the CodTech Internship Program. The projects focus on practical security implementations including:

File Integrity Monitoring

Penetration Testing Toolkit

Web Application Vulnerability Scanning

These tasks demonstrate hands-on skills in ethical hacking, vulnerability detection, and secure coding practices using Python.


Task 1: File Integrity Checker

 File: fileintegrity.py
 Objective

To monitor file changes by calculating and verifying cryptographic hash values.

 Description

This tool:

Generates SHA-256 hash for a file

Compares current hash with a reference hash

Detects unauthorized modifications

Displays logging-based professional output

 Technologies Used

Python

hashlib

logging

pathlib

 How to Run:
python fileintegrity.py

You will be prompted to:

Enter file path

Enter reference hash (or leave blank to generate new hash)

 Use Case

Detect malware modification

Verify sensitive document integrity

Digital forensics basics

 Task 2: Penetration Testing Toolkit
 File: pentest.py
 Objective

To simulate basic penetration testing techniques like port scanning and brute-force attacks.

 Description
1️. Port Scanner

Scans common ports (21, 22, 80, 443)

Detects open and closed ports

Uses socket programming

2. Brute Force Module

Attempts multiple passwords

Identifies correct password from list

Demonstrates password attack concept

 Technologies Used

Python

socket

logging

 How to Run
python pentest.py

Enter target host when prompted.

 For educational use only. Do not scan unauthorized systems.

 Use Case

Understand basic network reconnaissance

Learn attack simulation methods

Ethical hacking fundamentals

 Task 3: Web Application Vulnerability Scanner
 File: webvulnerability.py
 Objective

To detect common web vulnerabilities such as SQL Injection and Cross-Site Scripting (XSS).

 Description
 SQL Injection Detection

Injects test payload

Checks for SQL error patterns

 XSS Detection

Injects script payload

Checks reflection in response

 Technologies Used

Python

requests

BeautifulSoup

logging

 How to Run
python webvulnerability.py

Enter target URL when prompted.

 Use only on test environments.

 Use Case

Web security testing

Understanding OWASP Top 10 vulnerabilities

Secure coding awareness

 Skills Gained

Python for Cybersecurity

Hashing & Cryptography Basics

Network Programming

Web Security Testing

Ethical Hacking Concepts

Logging & Modular Coding

Task 4: Advanced Encryption Tool (AES-256)
 File: aesencryption.py (or your filename)
 Objective

To securely encrypt and decrypt any type of file (text, images, audio, video, documents) using AES-256 encryption.

 Description

This tool implements AES-256 (Advanced Encryption Standard) in CBC mode to ensure strong data confidentiality.

 Key Features

 Automatically generates 256-bit AES key (if not present)

 Saves key securely in aes.key

 Encrypts any file type

 Decrypts previously encrypted files

 Uses proper padding (PKCS7)

 Professional logging output

 Technologies Used

Python

PyCryptodome (Crypto.Cipher, Crypto.Random)

AES-256

CBC Mode

Logging module

 How It Works
 Encryption Process

Loads or generates a 256-bit key

Creates a random IV (Initialization Vector)

Pads file data to AES block size

Encrypts data using AES-CBC

Saves output as:

originalfile.ext.enc
 Decryption Process

Reads IV from encrypted file

Decrypts ciphertext

Removes padding

Restores original data

Saves output as:

originalfile.ext.dec
 How to Run
Step 1: Install Dependency
pip install pycryptodome
Step 2: Run the Script
python aesencryption.py
Step 3: Choose Option
Encrypt or Decrypt (E/D):

Press E to encrypt

Press D to decrypt

Then enter file path.

 Example Usage
Encrypt
Encrypt or Decrypt (E/D): E
Enter file path: sample.jpg

Output:

sample.jpg.enc
Decrypt
Encrypt or Decrypt (E/D): D
Enter file path: sample.jpg.enc

Output:

sample.jpg.dec
 Security Concepts Demonstrated

Symmetric Encryption

AES-256 Standard

Key Management

Initialization Vector (IV)

Padding Mechanism

Secure File Handling

 Important Notes

Keep aes.key secure — losing it means encrypted files cannot be recovered.

Do not share your AES key publicly.

For production systems, use secure key storage (HSM, environment variables, etc.).

 Real-World Applications

Secure document storage

Cloud file encryption

Data protection before transfer

Ransomware defense understanding

Confidential file handling

 Skills Gained

Practical Cryptography

AES Implementation

Secure Coding Practices

File Handling in Binary Mode

Understanding Encryption Workflows
