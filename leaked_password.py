'''
Check if a password has been leaked.
'''

import hashlib
import requests

def passwd_check(passwd):
    sha1 = hashlib.sha1(passwd.encode()).hexdigest().upper() # Encrypt password into SHA-1 hash.

    first5, tail = sha1[:5], sha1[5:]

    # Send the first 5 chars to "Have I Been Pwned API"
    response = requests.get(f"https://api.pwnedpasswords.com/range/{first5}")

    if tail in response.text:
        print("This password has been leaked and breached! try to create a stronger password")
    else:
        print("You're safe!")

# Standard input

passwd = input("Type your password to check: ")
passwd_check(passwd)