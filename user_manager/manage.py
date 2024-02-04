from user_manager.database.database_manager import Database
from user_manager.pass_manager.pass_manager import hash_with_salt, check_password
from colorama import Fore, Style
import sys

def user_manager(string):
    
    db = Database("user_manager/database/database.db")
    if string == 'sign up':
        username = input("username: ")
        password = input("password: ")
        password_repeat = input("password: ")
        flag, x = db.read_user_data(username)
        while flag:
            print("username already exist")
            username = input("username: ")
            password = input("password: ")
            password_repeat = input("password: ")
            flag, x = db.read_user_data(username)
        while password != password_repeat:
            print(f"\n{Fore.RED}passwords were not the same{Style.RESET_ALL}\n")
            password = input("password: ")
            password_repeat = input("password: ")
        if password == password_repeat:
            hashed_password = hash_with_salt(password).decode()
            db.insert_user_data(username, hashed_password)
            print(f"\n{Fore.GREEN}you've signed up seccessfully{Style.RESET_ALL}\n")
        
        return username
        
            
            

    if string == "sign in":
        username = input("username: ")
        password = input("password: ")
        confirmation, hashed_password = db.read_user_data(username)

        if confirmation:
            flag = check_password(password, hashed_password)

            if flag:
                print(f"\n{Fore.GREEN}User is verified{Style.RESET_ALL}\n")
                return username
        
            if not flag:
                print(f"\n{Fore.RED}either username or password is not correct{Style.RESET_ALL}\n")
                sys.exit()

        if not confirmation:
            print(f"\n{Fore.RED}either username or password is not correct{Style.RESET_ALL}\n")
            sys.exit()


        

    
    
    