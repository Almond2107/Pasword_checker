# Pasword_checker
A simple and interactive Python script that checks the strength of passwords based on common patterns, character complexity, and leaked password lists.

----

# 🔐 Password Strength Checker

This is a simple Python-based password strength checker that analyzes a password's security based on:
- Length
- Use of uppercase and lowercase letters
- Digits and special characters
- Comparison with a list of common/leaked passwords

It supports interactive CLI input and allows users to quit anytime with `quit` or `exit`.

###  Features:
- Loads leaked/weak passwords from `weak_passwords.txt`
- Real-time suggestions to improve your password
- Loop-based input for continuous testing
- No external dependencies

###  How to run:

```bash
python password_checker.py
