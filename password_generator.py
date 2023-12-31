import secrets
import string
import logging as lg
import pyperclip

class PasswordGenerator:

    lg.basicConfig(level=lg.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    datefmt="%d-%b-%y %H:%M:%S",
                    filename="main_logs.log",
                    filemode="a")

    def ask_for_parameters(self):
        while True:
            try:
                self.length = int(input("Enter the length of the password: "))
                if self.length < 6:
                    print("Please enter a number greater than 6")
                    continue
                elif self.length > 64:
                    print("Please enter a number less than 64")
                    continue
            except ValueError as e:
                print("Please enter a number")
                lg.debug(f"Error: {e}")
                continue
            self.symbols = input("Do you want symbols in your password? (y/n) ").lower()
            if self.symbols == "y":
                self.symbols = True
            elif self.symbols == "n":
                self.symbols = False
            else:
                print("Please enter y or n")
                lg.debug(f"Error: entered {self.symbols}")
                continue
            self.numbers = input("Do you want numbers in your password? (y/n) ").lower()
            if self.numbers == "y":
                self.numbers = True
            elif self.numbers == "n":
                self.numbers = False
            else:
                print("Please enter y or n")
                lg.debug(f"Error: entered {self.numbers}")
                continue
            self.uppercase = input("Do you want uppercase letters in your password? (y/n) ").lower()
            if self.uppercase == "y":
                self.uppercase = True
            elif self.uppercase == "n":
                self.uppercase = False
            else:
                print("Please enter y or n")
                lg.debug(f"Error: entered {self.uppercase}")
                continue
            break
        lg.info(f"Password parameters: length={self.length}, symbols={self.symbols}, numbers={self.numbers}, uppercase={self.uppercase}")
    
    def generate_password(self):
        combination = string.ascii_lowercase

        if self.numbers:
            combination += string.digits

        if self.symbols:
            combination += string.punctuation
        
        if self.uppercase:
            combination += string.ascii_uppercase

        combination_length = len(combination)

        new_password = ''.join([combination[secrets.randbelow(combination_length)] for _ in range(self.length)])

        lg.info(f"Password generated")

        return new_password
    
    def print_passwords(self):
        while True:
            try:
                length = int(input("How many passwords do you want to generate? "))
                if length < 1:
                    print("Please enter a number greater than 0")
                    lg.debug("Entered number less than 1")
                    continue
                break
            except ValueError as e:
                print("Please enter a number")
                lg.debug(f"Error: {e}")
                continue
        self.passwords = []
        for i in range(length):
            password = self.generate_password()
            self.passwords.append(password)
            print(f"Password {i+1} is: {password}")
        lg.info(f"Printed {length} passwords")

    def copy_to_clipboard(self):
        while True:
            try:
                index = int(input("Enter the number of the password you want to copy: "))
            except ValueError as e:
                print("Please enter a number")
                lg.debug(f"Error: {e}")
                continue
            if 0 < index <= len(self.passwords):
                password = self.passwords[index-1]
                pyperclip.copy(password)
                print(f"Password {index} copied to clipboard")
                lg.info(f"Password {index} copied to clipboard")
                break
            else:
                print("Please enter a valid number")
                lg.debug(f"Entered number out of range")
                continue