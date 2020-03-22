'''
Kournas - Network Mapper
Python 3.7.4
A Suite of Networking tools only using the Vanilla Python libraries
'''

#Import Statements
import functions
import threading
import time

#Pre Defined Variables
foundDevices = []


#Main---------------------------------------------------------------------------------------------------
print("Welcome To Kournas - Network Mapper!")
print("Kournas-Network-Mapper is a completely Vanilla network scanner, inspired by NMAP!")
print("The process will now begin, please be patient as it may take a while.")
print()

#Get IP of the host ------------------------------------------------------------------------------------
userIP = functions.resolveUserIP()

#First Function Will Scan Netowrk By TCP Shaking Every X.X.X.255 Address in the Users Network ----------

#Clean Up Network Statement + Add for all networks -----------------------------------------------------
network = userIP.split('.')
begNetwork = (network[0]) +"."+ (network[1]) +"."+ (network[2]) + "."

#Loop To Scan For Devices and Call For Function --------------------------------------------------------
for i in range(0, 253):
    testerConnection = functions.tcpShake(str(begNetwork+str(i)))
    if testerConnection:
        foundIP = str((begNetwork + str(i)))
        foundDevices.append(foundIP)
        print("Found A Device @ {}".format(foundIP))
    else:
        pass

#Function Call And Loop to Scan All Ports + Final Print Statement with All Data Collected --------------

for ipAddress in foundDevices:
    print()
    print("Local IP: {}".format(ipAddress))

#Function Call Using Threads to Scan Device ------------------------------------------------------------
    #counter to keep track of ports
    counterForPortScanner = 1
    for port in range(0,1000):
        thread = threading.Thread(target=functions.portScanner,kwargs={"host":ipAddress,"port":counterForPortScanner})
        #Increase counter by one
        counterForPortScanner += 1
        #Start the thread
        thread.start()