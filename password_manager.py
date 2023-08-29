from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.fernet import Fernet
import base64
import os
import logging as lg

lg.basicConfig(level=lg.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    datefmt="%d-%b-%y %H:%M:%S",
                    filename="main_logs.log",
                    filemode="a")

class PasswordManager:
    def __init__(self, db_class, master_password, key):
        self.db = db_class
        self.master_password = master_password.encode()
        self.key = key

    def encrypt_password(self, password):
        fernet = Fernet(self.key)
        encrypted_password = fernet.encrypt(password.encode())
        return encrypted_password

    def decrypt_password(self, encrypted_password):
        fernet = Fernet(self.key)
        decrypted_password = fernet.decrypt(encrypted_password).decode()
        return decrypted_password

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def print_menu(self):
        print("\n----------------")
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

    # TODO: Check if password meets basic criteria
    def check_password(self, password):
        # length between 6 and 64
        # if its utf-8?
        # its a letter or a code?
        pass

    def create_password(self, website, username, password):
        encrypted_password = self.encrypt_password(password)
        self.db.insert_password(website, username, encrypted_password)

    # TODO: copy to the clipboard directly
    def view_password(self, website, username):
        stored_password = self.db.view_password(website, username)[3]
        print(self.decrypt_password(stored_password))
        lg.debug(f"Password for {website} and {username} is {self.decrypt_password(stored_password)}")

    def delete_password(self, website, username): # add password?
        self.db.delete_password(website, username)

    def show_all_passwords(self):
        all_passswords = self.db.show_all_passwords()[1:]
        for _, website, username, password in all_passswords:
            print(website, username, password, sep=" || ")

    def update_password(self, website, username, password, newpassword):
        encrypted_password = self.encrypt_password(password)
        encrypted_newpassword = self.encrypt_password(newpassword)

        # Check if password exists and its valid
        stored_password = self.db.view_password(website, username)[3]

        if self.decrypt_password(stored_password) == password:
            self.db.modify_password(website, username, encrypted_newpassword)
            print('Password succesfully modified')
            lg.debug(f"Password for {website} and {username} was updated to {self.decrypt_password(encrypted_newpassword)}")
        else:
            print('Passwords does not match')
            lg.debug(f"Password for {website} and {username} was not updated")

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

    def menu(self):
        self.clear_screen()
        while True:
            self.print_menu()
            choice = int(input())

            if choice == 6:
                self.db.close_db()
                break

            try:
                self.action(choice)
            except Exception as e:
                print(f"Error in {choice}: {e}")
                lg.error(f"Error in {choice}: {e}")
