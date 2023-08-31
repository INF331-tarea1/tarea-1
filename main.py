from db_operations import DbOperations
from password_manager import PasswordManager
import os
import logging as lg
import functions

lg.basicConfig(level=lg.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    datefmt="%d-%b-%y %H:%M:%S",
                    filename="main_logs.log",
                    filemode="a")


if __name__ == "__main__":
    incorrect_master_password = True

    while incorrect_master_password:
        master_pass = functions.read_password(type="master")

        if not os.path.exists("database.db"):
            lg.info("Database does not exist")

            key = functions.generate_encryption_key(master_pass)
            master_pass_encrypt = functions.encrypt_password(key, master_pass)
            
            db_class = DbOperations()
            db_class.insert_password("dummy_pass", "dummy_pas", master_pass_encrypt)

            lg.debug(f"key: {key}")
            lg.debug(f"master_pass_encrypt: {master_pass_encrypt}")
            incorrect_master_password = False
        else:
            lg.info("Database exists")
            db_class = DbOperations()
            key = functions.generate_encryption_key(master_pass)

            master_pass_encrypt = db_class.view_password("dummy_pass", "dummy_pas")[3]
            master_pass_decrypt = functions.decrypt_password(key, master_pass_encrypt)
            
            if master_pass == master_pass_decrypt:
                lg.info("Master password correct")
                incorrect_master_password = False
            else:
                print("Master password incorrect")
                lg.debug("Master password incorrect")
                while incorrect_master_password:
                    master_pass = functions.read_password(type="master")
                    if master_pass == master_pass_decrypt:
                        lg.info("Master password correct")
                        incorrect_master_password = False
                    else:
                        print("Master password incorrect")
                        lg.debug("Master password incorrect")

    password_manager = PasswordManager(db_class, master_pass, key)
    password_manager.menu()
