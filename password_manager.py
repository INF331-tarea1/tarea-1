import os


class PasswordManager:
    def __init__(self, db_class):
        self.db_class = db_class
        self.db_class.create_table()

    def ir_a_menu(self):
        # esto es para que no tengamos que ir al menu a cada que ejecutamos el programa
        # borrar cuando ya estemos terminando
        ir = input("Desea ir al menu? (y/n): ")
        match ir:
            case "y":
                self.menu()
            case "n":
                print("Exiting...")
            case _:
                print("Invalid choice")

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def print_menu(self):
        self.clear_screen()
        print("Password Manager")
        print("----------------")
        print("1. Create new password")
        print("2. View password")
        print("3. Delete password")
        print("4. Show all passwords")
        print("5. Update password")
        print("6. Exit")
        print("----------------")
        print("Enter your choice: ", end="")

    def create_password(self):
        pass

    def view_password(self):
        pass

    def delete_password(self):
        pass

    def show_all_passwords(self):
        pass

    def update_password(self):
        pass

    def menu(self):
        while True:
            self.print_menu()
            choice = int(input())

            if choice == 1:
                try:
                    self.create_password()
                except Exception as e:
                    print("Error creating password:", e)
            elif choice == 2:
                try:
                    self.view_password()
                except Exception as e:
                    print("Error viewing password:", e)
            elif choice == 3:
                try:
                    self.delete_password()
                except Exception as e:
                    print("Error deleting password:", e)
            elif choice == 4:
                try:
                    self.show_all_passwords()
                except Exception as e:
                    print("Error showing all passwords:", e)
            elif choice == 5:
                try:
                    self.update_password()
                except Exception as e:
                    print("Error updating password:", e)
            elif choice == 6:
                print("Exiting...")
                break
            else:
                print("Invalid choice")
