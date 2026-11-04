from cryptography.fernet import Fernet

key = Fernet.generate_key() # key used to encrypt plain text to make it unreadable
cipher_suite = Fernet(key)

message = "This is a creadentials like: password, tokens, environment variable, etc...".encode()
cipher_text = cipher_suite.encrypt(message)
print("The encrypted text is: " + str(cipher_text))

plain_text = cipher_suite.decrypt(cipher_text)

print('Decrypted Text' + str(plain_text))

if plain_text == message:
    print("cipher text and plain text are compatible")