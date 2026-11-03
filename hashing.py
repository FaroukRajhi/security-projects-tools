'''
Hashing a readable password using SHA-256 Algorithm
'''

import hashlib

def hash_passwd(passwd):
    return hashlib.sha256(passwd.encode()).hexdigest()


passwd = input("Type any readable text to hash: ")
hashed_passwd = hash_passwd(passwd)

print(f"Hased password: {hashed_passwd}")