#GRecon : Google Recon V1.0
#Coded by Adnane X Tebbaa
#Github : https://www.github.com/adnane-x-tebbaa/Grecon 
#Twitter : @TebbaaX 
#Extended Plugin File (Pasting Sites LookUp) 


import os 
import sys
import time
import requests 
import random 
from googlesearch import search
from termcolor import colored, cprint
from http import cookiejar 

TLD = ["co.ma","dz","ru","ca"]
zolo  = random.choice(TLD)

X = requests.get('https://www.google.com/webhp?ei=1') # : /
X.status_code 
if X.status_code == 200:
 time.sleep(5)  

f = open('grecon.config', 'r')
alpha = f.read() 
key = alpha
time.sleep(5) 
print(colored ('[>] Looking in Pasting Sites...' ,'green')) #Pasting Sites e.g : PasteBin...
query = "site:pastebin.com | site:hastebin.com | site:carbon.now.sh " + key 
for gamma in search(query, tld=zolo, num=30 , stop=60 , pause=2): 
    print("" + gamma) 
print ("") 
if os.path.exists(".google-cookie"):
 os.remove(".google-cookie")
os.remove("grecon.config") 
print(colored ('[>] Done...Happy Hunting' ,'green'))
