'''
Kournas - Port Scanner
Python 3.7.4
A Port Scanning Utility Created in Python
'''

#Import Statements
import threading
import socket

#Take user input for target host
targetHost = input("Please enter the Domain or IP of your target host: ")
targetHostIP = socket.gethostbyname(targetHost)

#Function for Port Scanning
def portScanner(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #In order to speed up the process, we need to create a timeout
    sock.settimeout(0.5)

    #Check if port is open and print result
    try:
        #Ateempt to connect trough that port
        connect = sock.connect((targetHostIP, port))
        #Print if Port is open
        print("Port: {} @ {} is Open!".format(port, targetHost))
        #Close the connection
        connect.close()
    except:
        pass


#Utilize threading to speed up the scan
counter = 1
for x in range(0,1000):
    thread = threading.Thread(target=portScanner,kwargs={"port":counter})
    #Increase counter by one
    counter = counter + 1
    #Start the thread
    thread.start()
        
