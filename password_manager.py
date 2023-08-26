from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.fernet import Fernet
import base64
import os


class PasswordManager:
    def __init__(self, db_class, master_password):
        self.db = db_class
        self.db.create_table()
        self.master_password = master_password.encode()
        self.key = self.generate_encryption_key()

    # with the master_password creates the encryption key
    # If the master_password is not the right one, then the decrypt will not work
    # TODO: How can I ensure that the master password is correct?
    def generate_encryption_key(self):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            salt=os.urandom(16),
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(self.master_password))
        return key

    def encrypt_password(self, password):
        fernet = Fernet(self.key)
        encrypted_password = fernet.encrypt(password.encode())
        return encrypted_password

    def decrypt_password(self, encrypted_password):
        try:
            key = self.key
            fernet = Fernet(key)
            decrypted_password = fernet.decrypt(encrypted_password).decode()
            return decrypted_password
        except Exception as e:
            print("Decryption failed. Incorrect master password or corrupted data.")
            print(e)
    
    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def print_menu(self):
        self.clear_screen()
        print("Password Manager")
        print("----------------")
        print("1. Show all passwords")
        print("2. View password")
        print("3. Delete password")
        print("4. Create new password")
        print("5. Update password")
        print("6. Exit")
        print("----------------")
        print("Enter your choice: ", end="")

    def check_password(self, password):
        # TODO: Check if password meets basic criteria
        pass

    def create_password(self, website, username, password):
        # TODO: encrypt password here, new function
        self.db.insert_password(website, username, password)

    def view_password(self, website, username):
        self.db.view_password(website, username)

    def delete_password(self, website, username): # add password?
        self.db.delete_password(website, username)

    def show_all_passwords(self):
        self.db.show_all_passwords()

    def update_password(self, website, username, password, newpassword):
        #TODO: encrypt password here, new function
        self.db.modify_password(website, username, password, newpassword) #TODO: add newpassword in db_operations

    def action(self, choice):
        if choice == 1:
            self.show_all_passwords()
        elif choice == 2:
            website = input("Enter website: ")
            username = input("Enter username: ")
            self.view_password(website, username)
        elif choice == 3:
            website = input("Enter website: ")
            username = input("Enter username: ")
            self.delete_password(website, username)
        elif choice == 4:
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            self.create_password(website, username, password)
        elif choice == 5:
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = input("Enter current password: ")
            newpassword = input("Enter new password: ")
            self.update_password(website, username, password, newpassword)
        else:
            print("Invalid choice")

        return True


    def menu(self):
        flag = True
        while flag:
            self.print_menu()
            choice = int(input())

            if choice == 6:
                break

            try:
                flag = self.action(choice)
            except:
                print(f"Error in {choice}")
