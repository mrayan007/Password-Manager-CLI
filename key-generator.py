from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open ('secret.key', 'wb') as file :
    file.write(key)