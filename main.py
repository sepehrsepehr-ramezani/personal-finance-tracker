import os
from user_manager.manage import user_manager
from sample_files.manage import manage
from jdatetime import datetime


def create_user():

    username = user_manager("sign up")
    #Create user files
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%B")
    # Get the directory of the current Python file
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Define the new directory path
    new_dir_path = os.path.join(current_dir, f"usrs/{username}/{year}/{month}")

    # Create the new directory
    os.makedirs(new_dir_path, exist_ok=True)



    manage(username)


    

def auth():
    username = user_manager("sign in")
    manage(username)


if __name__ == "__main__":
    string = input("sign in \nsign up\n\t")
    
    if string == "sign in":
        auth()
    elif string == "sign up":
        create_user()
    