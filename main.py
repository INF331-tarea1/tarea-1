from db_operations import DbOperations
from password_manager import PasswordManager


if __name__ == "__main__":
    incorrect_master_password = True
    db_class = DbOperations()

    while incorrect_master_password:
        MASTER_PASS = input("Enter the master password: ")
        
        password_manager = PasswordManager(db_class, MASTER_PASS)
        all_passwords = db_class.show_all_passwords()

        
        if all_passwords == -1:
            password_manager.create_password("dummy", "dummy", "dummy")
            incorrect_master_password = False
        else:
            try:
                stored_dummy = password_manager.view_password('dummy', 'dummy')
                incorrect_master_password = False
            except Exception as e:
                print("Invalid master password.")
                print(e)
                print("Try again")


    password_manager.menu()
