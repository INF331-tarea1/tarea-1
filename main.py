from db_operations import DbOperations
from password_manager import PasswordManager
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.fernet import Fernet
import base64
import os

def generate_encryption_key():
    path_variable = os.environ.get("PATH")
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=os.urandom(16),
        iterations=480000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(path_variable.encode()))
    return key

def encrypt_password(key, password):
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password

def decrypt_password(key, encrypted_password):
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password

if __name__ == "__main__":
    incorrect_master_password = True

    while incorrect_master_password:
        MASTER_PASS = input("Enter the master password: ")

        
        if not os.path.exists("database.db"):
            print("Database does not exist")
            key = generate_encryption_key()
            MASTER_PASS_ENCRYPT = encrypt_password(key, MASTER_PASS)
            db_class = DbOperations()
            db_class.insert_password("dummy_key", "dummy_key", key)
            db_class.insert_password("dummy_pass", "dummy_pas", MASTER_PASS_ENCRYPT)
            print(f"key: {key}")
            print(f"master_pass_encrypt: {MASTER_PASS_ENCRYPT}")
            incorrect_master_password = False
        else:
            print("Database exists")
            db_class = DbOperations()
            key = db_class.view_password("dummy_key", "dummy_key")[3]
            MASTER_PASS_ENCRYPT = db_class.view_password("dummy_pass", "dummy_pas")[3]
            MASTER_PASS_DECRYPT = decrypt_password(key, MASTER_PASS_ENCRYPT)
            if MASTER_PASS == MASTER_PASS_DECRYPT:
                print("Master password correct")
                incorrect_master_password = False
            else:
                print("Master password incorrect")
                while incorrect_master_password:
                    MASTER_PASS = input("Enter the master password: ")
                    if MASTER_PASS == MASTER_PASS_DECRYPT:
                        print("Master password correct")
                        incorrect_master_password = False
                    else:
                        print("Master password incorrect")

    password_manager = PasswordManager(db_class, MASTER_PASS, key)
    password_manager.menu()
