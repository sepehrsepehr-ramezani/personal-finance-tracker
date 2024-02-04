from database.database_manager import Database
from pass_manager.pass_manager import hash_with_salt, check_password
import sys

def main(string):

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
            print("\npasswords were not the same\n")
            password = input("password: ")
            password_repeat = input("password: ")
        if password == password_repeat:
            hashed_password = hash_with_salt(password).decode()
            db.insert_user_data(username, hashed_password)
            print("you've signed up seccessfully")
        
            
            

    if string == "sign in":
        username = input("username: ")
        password = input("password: ")
        confirmation, hashed_password = db.read_user_data(username)

        if confirmation:
            flag = check_password(password, hashed_password)

            if flag:
                print("User is verified")
                sys.exit()
        
            if not flag:
                print("either username or password is not correct")
                sys.exit()

        if not confirmation:
            print("either username or password is not correct")
            sys.exit()

if __name__ == "__main__":
    string = input("sign in \nsign up\n\t")
    db = Database("database/database.db")
    main(string)


