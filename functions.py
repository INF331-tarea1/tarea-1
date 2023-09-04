import string
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def check_password(password):
    valid_characters = string.ascii_letters + string.digits + string.punctuation.replace("\\", "")

    return len(password) >= 6 and len(password) <= 64 \
            and all(char in valid_characters for char in password)

def read_password(type=""):
    while True:
        password = input(f"Enter {type} password: ")
        if check_password(password):
            return password
        print("Password doesn't meet the minimum criteria. Please try again.")

def encrypt_password(key, password):
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password

def decrypt_password(key, encrypted_password):
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password

def generate_encryption_key(master_password):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=master_password[::-1].encode(),
        iterations=480000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
    return key
