import os
from cryptography.fernet import Fernet
#get base64 key from enviroment variable
key = os.environ.get("SECRET_KEY")


cipher_suite = Fernet(key.encode())

def encrypt_password(password):
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password

# To decrypt the password when needed
def decrypt_password(encrypted_password):
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
    return decrypted_password