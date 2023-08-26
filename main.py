from db_operations import DbOperations
from password_manager import PasswordManager
        


if __name__ == "__main__":
    db_class = DbOperations()
    password_manager = PasswordManager(db_class, "master_password")
    password_manager.menu()

