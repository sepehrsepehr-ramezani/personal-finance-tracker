from user_manager.manage import user_manager
from sample_files.manage import manage
from jdatetime import datetime
import os

#create folder for each user (usrs/year/month)
def create_usr_folder(username, year, month):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    new_dir_path = os.path.join(current_dir, f"usrs/{username}/{year}/{month}")
    os.makedirs(new_dir_path, exist_ok=True)

def create_user():
    username = user_manager("sign up")
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%B")
    create_usr_folder(username, year, month)
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
    