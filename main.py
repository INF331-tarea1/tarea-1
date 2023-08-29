from db_operations import DbOperations
from password_manager import PasswordManager
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os
import logging as lg
import getpass

lg.basicConfig(level=lg.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    datefmt="%d-%b-%y %H:%M:%S",
                    filename="main_logs.log",
                    filemode="a")

def generate_encryption_key(master_password):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=master_password[::-1].encode(),
        iterations=480000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
    return key

if __name__ == "__main__":
    incorrect_master_password = True

    while incorrect_master_password:
        MASTER_PASS = getpass.getpass("Enter the master password: ")

        if not os.path.exists("database.db"):
            lg.info("Database does not exist")
            key = generate_encryption_key(MASTER_PASS)
            db_class = DbOperations()

            psw_mng = PasswordManager(db_class, MASTER_PASS, key)
            MASTER_PASS_ENCRYPT = psw_mng.encrypt_password(MASTER_PASS)
            db_class.insert_password("dummy_pass", "dummy_pas", MASTER_PASS_ENCRYPT)

            lg.debug(f"key: {key}")
            lg.debug(f"master_pass_encrypt: {MASTER_PASS_ENCRYPT}")
            incorrect_master_password = False
        else:
            lg.info("Database exists")
            db_class = DbOperations()
            key = generate_encryption_key(MASTER_PASS)
            psw_mng = PasswordManager(db_class, MASTER_PASS, key)

            MASTER_PASS_ENCRYPT = db_class.view_password("dummy_pass", "dummy_pas")[3]
            MASTER_PASS_DECRYPT = psw_mng.decrypt_password(MASTER_PASS_ENCRYPT)
            
            if MASTER_PASS == MASTER_PASS_DECRYPT:
                lg.info("Master password correct")
                incorrect_master_password = False
            else:
                print("Master password incorrect")
                lg.debug("Master password incorrect")
                while incorrect_master_password:
                    MASTER_PASS = input("Enter the master password: ")
                    if MASTER_PASS == MASTER_PASS_DECRYPT:
                        lg.info("Master password correct")
                        incorrect_master_password = False
                    else:
                        print("Master password incorrect")
                        lg.debug("Master password incorrect")

    password_manager = PasswordManager(db_class, MASTER_PASS, key)
    password_manager.menu()
