# MD5 Password Cracker

A simple dictionary-based MD5 hash cracker built for learning about 
password hashing, brute-force resistance, and why algorithms like 
MD5 are unsuitable for storing passwords.

## Usage
1. Download a wordlist (e.g. from [SecLists](https://github.com/danielmiessler/SecLists))
2. Place it as `passwordSet.txt` in the project folder
3. Run: `python cracker.py`

## Why this matters
This project demonstrates why modern systems use slow, salted hashing 
algorithms (bcrypt, scrypt, Argon2) instead of fast unsalted hashes like MD5.
