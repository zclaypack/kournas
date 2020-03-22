'''
Kournas - Website Check
Python 3.7.4
A tool that checks if a Domain has an HTTP port open (checks if the website is up on that domain).
'''

#Import Statements
import socket

#Explain the tool
print("This tool allows you to check if a webiste is online.")

#Take user input for Website
website = input("Please enter the website you would like to check: ")

#Create the Sock
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Attempt to Connect to the Website on Port 80 - (HTTP)
result = sock.connect_ex((website, 80))

#Close Sock
sock.close()

#Print Result of Both Tests
if result == 0:
   print("Success! The website you wanted to check is up. The website is currently able to receive connections trough port 80.")
else:
   print("Fail! The website is either down, or your connection to the internet is down. (The Website is not Accepting Port 80 Connections)")
