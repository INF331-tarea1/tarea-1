from db_operations import DbOperations
import os
class password_manager:
    def __init__(self, db_class):
        self.db_class = db_class
        self.db_class.create_table()

    def ir_a_menu(self):
        # esto es para que no tengamos que ir al menu a cada que ejecutamos el programa
        # borrar cuando ya estemos terminando
        ir = input("Desea ir al menu? (y/n): ")
        match ir:
            case "y":
                self.main()
            case "n":
                print("Exiting...")
            case _:
                print("Invalid choice")

    def main(self):
        #menu principal del programa
        while True:
            self.limpiar_pantalla()
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
            try:
                choice = int(input())
                match choice:
                    case 1:
                        try:
                            self.create_password()
                        except Exception as e:
                            print("Error: ", e)
                    case 2:
                        try:
                            view_password()
                        except Exception as e:
                            print("Error: ", e)
                    case 3:
                        try:
                            delete_password()
                        except Exception as e:
                            print("Error: ", e)
                    case 4:
                        try:
                            show_all_passwords()
                        except Exception as e:
                            print("Error: ", e)
                    case 5:
                        try:
                            update_password()
                        except Exception as e:
                            print("Error: ", e)
                    case 6:
                        try:
                            print("Exiting...")
                            break
                        except Exception as e:
                            print("Error: ", e)
                    case _:
                        print("Invalid choice")
            except Exception as e:
                print("Error: ", e)
    
    def create_password(self):
        pass

    def limpiar_pantalla(self):
        #para limpirar la pantalla
        os.system("cls" if os.name == "nt" else "clear")
        


if __name__ == "__main__":
    db_class = DbOperations()
    password_manager = password_manager(db_class)
    password_manager.ir_a_menu()
