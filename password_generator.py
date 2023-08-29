import secrets
import string
import logging as lg
class Passwordgenerator:

    lg.basicConfig(level=lg.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    datefmt="%d-%b-%y %H:%M:%S",
                    filename="main_logs.log",
                    filemode="a")

    def ask_for_parameters(self):
        while True:
            try:
                self.length = int(input("Enter the length of the password: "))
            except ValueError:
                print("Please enter a number")
                continue
            self.symbols = input("Do you want symbols in your password? (y/n) ").lower()
            if self.symbols == "y":
                self.symbols = True
            elif self.symbols == "n":
                self.symbols = False
            else:
                print("Please enter y or n")
                continue
            self.numbers = input("Do you want numbers in your password? (y/n) ").lower()
            if self.numbers == "y":
                self.numbers = True
            elif self.numbers == "n":
                self.numbers = False
            else:
                print("Please enter y or n")
                continue
            self.uppercase = input("Do you want uppercase letters in your password? (y/n) ").lower()
            if self.uppercase == "y":
                self.uppercase = True
            elif self.uppercase == "n":
                self.uppercase = False
            else:
                print("Please enter y or n")
                continue
            break
        lg.info(f"Password parameters: length={self.length}, symbols={self.symbols}, numbers={self.numbers}, uppercase={self.uppercase}")
    
    def generate_password(self):
        combination = string.ascii_lowercase + string.digits

        if self.symbols:
            combination += string.punctuation
        
        if self.uppercase:
            combination += string.ascii_uppercase

        combination_length = len(combination)

        new_password = ''.join([combination[secrets.randbelow(combination_length)] for _ in range(self.length)])

        lg.info(f"Password generated")

        return new_password
    
    def print_passwords(self, length):
        length = int(length)
        for i in range(length):
            password = self.generate_password()
            print(f"Password {i} is: {password}")
        lg.info(f"Printed {length} passwords")

pg = Passwordgenerator()
pg.ask_for_parameters()
pg.print_passwords(10)