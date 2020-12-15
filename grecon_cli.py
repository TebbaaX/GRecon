#GRecon_Cli
#Coded by Adnane X Tebbaa
#Github : https://www.github.com/adnane-x-tebbaa/Grecon 
#Twitter : @TebbaaX 


import os 
import sys
import time
import requests 
import random 
from googlesearch import search
from termcolor import colored, cprint
from http import cookiejar 



TLD = ["com","com.tw","co.in"]
beta  = random.choice(TLD)
s = requests.Session() 


print("") 
key  = input (colored('[+] Set Query : ', 'white' )) 
print("") 
print(colored ('[>] Running...' ,'green')) 
query = key                           
for gamma in search(query, tld=beta, num=30 , stop=90 , pause=2): 
    print("" + gamma)   