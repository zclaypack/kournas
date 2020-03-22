'''
Kournas - Network Mapper - Functions
Python 3.7.4
All The Functions Needed for the Network Mapper Library
'''

import socket
import threading

#Functions---------------------------------------------------------------

#Function for resolving user's IP
def resolveUserIP():
    #Create Sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #Attempt to Connect to a Bogus Private IP
    sock.connect(("10.0.0.0", 80))
    #Resolve The Name
    userIP = sock.getsockname()[0]
    #Close the Socket
    sock.close()
    #Return the HOSTIP
    return userIP

#Function For TCP Shake - Used in the Discover Device Protocol
def tcpShake(hostname):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    result = sock.connect_ex((hostname, 443))
    sock.close()
    return result == 0

#Function For Port Scan - Used in the Port Scanner Protocol
def portScanner(host, port):
    #Create Socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #In order to speed up the process, we need to create a timeout
    sock.settimeout(0.5)
    #Check if port is open and print result
    try:
        #Attempt to connect trough that port
        connect = sock.connect((host, port))
        #Append Port and IP to list in Main Code
        print("Port: {} @ {} is Open!".format(port, host))
        #Close the connection
        connect.close()
    except:
        pass
