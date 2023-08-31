import os
import logging as lg
import pyperclip
import functions
from prettytable import PrettyTable
from password_generator import PasswordGenerator

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
        self.generator = PasswordGenerator()

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
        print("7. Generate passwords")
        print("8. Exit")
        print("----------------")
        print("Enter your choice: ", end="")

    def create_password(self, website, username, password):
        stored_item = self.db.view_password(website, username)
        
        if stored_item == -1:
            encrypted_password = functions.encrypt_password(self.key, password)
            self.db.insert_password(website, username, encrypted_password)
        else:
            print("Password already saved, if you want to update it use that option.")

    def view_password(self, website, username):
        stored_password = self.db.view_password(website, username)
        if stored_password != -1:
            pyperclip.copy(functions.decrypt_password(self.key, stored_password)[3])
            print("Password copied to the clipboard")
            lg.debug(f"Password for {website} and {username} is {functions.decrypt_password(self.key, stored_password)[3]}")
        else:
            print("Password not found")
            lg.debug(f"Password for {website} and {username} not found")

    def delete_password(self, website, username):
        if self.db.view_password(website, username) != -1:
            self.db.delete_password(website, username)
            print("Password deleted succesfully")
        else:
            print("Password not found")

    def show_all_passwords(self):
        all_passswords = self.db.show_all_passwords()[1:]

        if len(all_passswords) == 0:
            print("No password saved")
            return

        t = PrettyTable(['Website', 'Username'])
        for _, website, username, _ in all_passswords:
            t.add_row([website, username])

        print(t)

    def update_password(self, website, username, password, newpassword):
        encrypted_newpassword = functions.encrypt_password(self.key, newpassword)

        # Check if password exists and its valid
        stored_password = self.db.view_password(website, username)

        if stored_password != -1:
            if functions.decrypt_password(self.key, stored_password[3]) == password:
                self.db.modify_password(website, username, encrypted_newpassword)
                print('Password succesfully modified')
                lg.debug(f"Password for {website} and {username} was updated to {functions.decrypt_password(self.key, encrypted_newpassword[3])}")
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
            password = functions.read_password()
            self.create_password(website, username, password)
        elif choice == 5:
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = functions.read_password(type="current")
            newpassword = functions.read_password(type="new")
            self.update_password(website, username, password, newpassword)
        elif choice == 6:
            self.db.delete_all()
        elif choice == 7:
            self.generator.ask_for_parameters()
            self.generator.print_passwords()
            while True:
                a = input("Do you want to copy a password? (y/n) ")
                if a == "y":
                    self.generator.copy_to_clipboard()
                    break
                elif a == "n":
                    break
                else:
                    print("Invalid input")
                    continue

    def valid_menu_input(self, menu_input):
        return menu_input.isdigit() and int(menu_input) <= 8 and int(menu_input) >= 1

    def menu(self):
        self.clear_screen()
        while True:
            self.print_menu()
            choice = input()

            if not self.valid_menu_input(choice):
                print("Invalid choice, try again.")
                continue

            choice = int(choice)

            if choice == 8:
                self.db.close_db()
                break

            try:
                self.action(choice)
            except Exception as e:
                lg.error(f"Error in {choice}: {e}")
