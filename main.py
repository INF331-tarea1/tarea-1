from db_operations import DbOperations
from password_manager import PasswordManager


if __name__ == "__main__":
    password = "ЄϪχ͂˓ʥȬ¯d"

    MASTER_PASS = input("Enter the master password: ")

    db_class = DbOperations()
    password_manager = PasswordManager(db_class, MASTER_PASS)

    password_manager.clear_screen()
    
    encrypt = password_manager.encrypt_password(password)
    decrypt = password_manager.decrypt_password(encrypt)

    print(encrypt)
    print(decrypt)
    print(decrypt == password)
