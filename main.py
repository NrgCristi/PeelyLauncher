import os
import time
os.system("pip install os")
os.system("pip install time")
user_code = input('Please Enter your auth code from rebrand.ly/authcode:')
while False:
    if len(user_code) != 32:
        {
            print('the auth code you provided is incorrect, invalid, expired, or not 32 characters long, please get a new one from rebrand.ly/authcode any try again')
        }


while True:
    {
        os.startfile('com.epicgames.launcher://apps/fn%3A4fe75bbc5a674f4f9b356b5c90567da5%3AFortnite?action=launch&silent=true -AUTH_LOGIN=unused -AUTH_PASSWORD={user_code} -AUTH_TYPE={user_code} -epicapp=Fortnite -epicenv=Prod -EpicPortal')
    }
