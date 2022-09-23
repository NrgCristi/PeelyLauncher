import os
import time
os.system("pip install os")
os.system("pip install time")
code = ('Please enter your authorization code from rebrand.ly/authcode')
print('Launching Fortnite')
os.startfile('com.epicgames.launcher://apps/fn%3A4fe75bbc5a674f4f9b356b5c90567da5%3AFortnite?action=launch&silent=true -AUTH_LOGIN=unused -AUTH_PASSWORD={input} -AUTH_TYPE=input -epicapp=Fortnite -epicenv=Prod -EpicPortal')
while False:
            if len(code) != 32:
                print("The Auth code you provided is not valid and it must be 32 characters long, please get a new one from rebrand.ly/authcode")
