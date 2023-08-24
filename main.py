from db_operations import DbOperations
from password_manager import PasswordManager
        


if __name__ == "__main__":
    db_class = DbOperations()
    db_class.delete_table()
    password_manager = PasswordManager(db_class)
    password_manager.ir_a_menu()

