import os


class PasswordManager:
    def __init__(self, db_class):
        self.db = db_class
        self.db.create_table()

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

    def encrypt(self, password):
        pass

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
