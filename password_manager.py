from cryptography.fernet import Fernet
import os
import logging as lg
import pyperclip
import getpass

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
        print("6. Delete all passwords")
        print("7. Exit")
        print("----------------")
        print("Enter your choice: ", end="")

    # TODO: Check if password meets basic criteria
    def check_password(self, password):
        # length between 6 and 64
        # if its utf-8?
        # its a letter or a code?
        pass

    def create_password(self, website, username, password):
        stored_item = self.db.view_password(website, username)
        
        if stored_item != -1:
            encrypted_password = self.encrypt_password(password)
            self.db.insert_password(website, username, encrypted_password)
        else:
            print("Password already saved, if you want to update it use that option.")

    def view_password(self, website, username):
        stored_password = self.db.view_password(website, username)
        if stored_password != -1:
            pyperclip.copy(self.decrypt_password(stored_password)[3])
            print("Password copied to the clipboard")
            lg.debug(f"Password for {website} and {username} is {self.decrypt_password(stored_password)[3]}")
        else:
            print("Password not found")
            lg.debug(f"Password for {website} and {username} not found")

    def delete_password(self, website, username): # add password?
        if self.db.view_password(website, username) != -1:
            self.db.delete_password(website, username)
            print("Password deleted succesfully")
        else:
            print("Password not found")

    def show_all_passwords(self):
        all_passswords = self.db.show_all_passwords()

        try:
            for _, website, username, password in all_passswords[1:]:
                print(website, username, password, sep=" || ")
        except:
            print("No password saved")


    def update_password(self, website, username, password, newpassword):
        encrypted_newpassword = self.encrypt_password(newpassword)

        # Check if password exists and its valid
        stored_password = self.db.view_password(website, username)

        if stored_password != -1:
            if self.decrypt_password(stored_password[3]) == password:
                self.db.modify_password(website, username, encrypted_newpassword)
                print('Password succesfully modified')
                lg.debug(f"Password for {website} and {username} was updated to {self.decrypt_password(encrypted_newpassword[3])}")
            else:
                print('Passwords does not match')
                lg.debug(f"Password for {website} and {username} was not updated")
        else:
            print('Account not found')
            lg.debug(f"Password for {website} and {username} was not found")

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
            password = getpass.getpass("Enter password: ")
            self.create_password(website, username, password)
        elif choice == 5:
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = getpass.getpass("Enter current password: ")
            newpassword = getpass.getpass("Enter new password: ")
            self.update_password(website, username, password, newpassword)
        elif choice == 6:
            self.db.delete_all()

    def valid_menu_input(self, menu_input):
        return menu_input.isdigit() and int(menu_input) <= 7 and int(menu_input) >= 1


    def menu(self):
        self.clear_screen()
        while True:
            self.print_menu()
            choice = input()

            if not self.valid_menu_input(choice):
                print("Invalid choice, try again.")
                continue

            choice = int(choice)

            if choice == 7:
                self.db.close_db()
                break

            try:
                self.action(choice)
            except Exception as e:
                print(f"Error in {choice}: {e}")
                lg.error(f"Error in {choice}: {e}")
