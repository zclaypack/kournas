'''
Kournas - Server/Domain Resolver
Python 3.7.4
Finds the IP's associated with a domain/website.
'''

#Import Statement ------------------------
import socket

#Pre Defined Variables -------------------
ipAddrList = []

#Main ------------------------------------

#User Selects Website/Host to Resolve
userChoice = input("Please enter the name of the website/domain you would like to resolve: ")

#Connect to a User Specified Host --------'
try:
    connectionAttempt = socket.getaddrinfo(userChoice, 0, 0, 0, 0)
except:
    print("Failed Connection! Shutting Down!")
    print("Correct format is: <yourwebsitehere.com>")
    quit()
#For Loop to Get IP's --------------------
for ipAddr in connectionAttempt:
    #Append the IP's to a List
    ipAddrList.append(ipAddr[-1][0])

#Remove All Double IP's ------------------
ipAddrList = list(set(ipAddrList))

#For Loop + Print Statement to Create Neat 
for addr in ipAddrList:
    print("Found IP for {} @ {}".format(userChoice, addr))