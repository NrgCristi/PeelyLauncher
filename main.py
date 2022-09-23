import os
import time
os.system("pip install os")
os.system("pip install time")

input('Please enter your authcode from https://rebrand.ly/authcode:')
print("Launching Fortnite")
args = ('-AUTH_LOGIN=unused, -AUTH_PASSWORD=exchange_code, -AUTH_TYPE=exchangecode, -epicapp=Fortnite, -epicenv-Prod, -EpicPortal')
os.startfile('com.epicgames.launcher://apps/fn%3A4fe75bbc5a674f4f9b356b5c90567da5%3AFortnite?action=launch&silent=true + args')
else:
    {
    	
    	if len(input) != 32:
        	print('The auth code is incorrect and it must be 32 characters long, please get a new one from https://rebrand.ly/authcode')
}
