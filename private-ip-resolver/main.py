'''
Kournas - IP Resolver
Python 3.7.4
A program which resolves the local IP of the user
'''

#Import Statements
import socket

def resolveIP():
    #Create Sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #Attempt to Connect to a Bogus Private IP
    sock.connect(("10.0.0.0", 80))
    #Resolve The Name
    hostIP = sock.getsockname()[0]
    #Close the Socket
    sock.close()
    #Return the HOSTIP
    return hostIP

#Main
userIP = resolveIP()
print("Your IP is: {}".format(userIP))