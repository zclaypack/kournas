# Kournas

**Kournas** is a suite of networking tools created in Python. The main purpose of this suite was to experiment with the built in **Socket** library Python has to offer. I wanted to make a suite of tools that only required Python and no external libraries. This project is still a work in progress and is under development. 

# How to Use

The main reason I only used the **socket** library, was to ensure that anyone can run this program as long as they have Python3 installed. 

## Website Checker

The first tool in the **Kournas** suite is the Website Checker. The website checker is a very simple peace of code which takes a user's input for a websites Domain or IP, and then attempts to connect to it through Port 80. I chose to use Port 80 instead of Port 443, because there are still some website running only HTTP.

## Port Scanner

The second tool in the **Kournas** suite is the Port Scanner. The port scanner takes a users input for an IP or Domain and iterates through a set amount of ports, checking which ones are open. I set the default to Ports 1-10000, but you can easily change this. If you want to change the ports which are scanned, go to the for loop at the bottom and change the range. **Warning** this tool is for educational purposes only, be careful and make sure you have permission to scan the host before doing so.

## Network Mapper

The third tool in the **Kournas** suite is the Network Mapper. This program works, however it isn't the most optimized of tools in this suite. The Network Mapper attempts to discover all devices on the network, and then performs a port scan on the discovered device, showing which ports are currently in use. 

**Future Plans for Network Mapper**
*The main feature of this suite must be that it remains Vanilla (No External Libraries)*
 - Discover The OS of the Devices
 - Discover MAC of the Devices
 - Discover The Host Name of the Devices

 ## IP Resolver

The fourth tool in the **Kournas** suite is the IP Resolver. The IP Resolver tool attempts to connect to a *bogus* private IP, and then based on that information resolves the users personal IP address. The main reason I created this program, was to help with the other tools in this suite. One issue that occurs when trying to find your own personal IP in Python, is that it often resolves the loopback address. This is an issue becuase, you need your private IP when connecting to your device from another device. 

## DNS Resolver

The fifth tool in the **Kournas** suite is the DNS Resolver. The DNS Resolver tool gets a domain from a user and then returns all IP's associated with that domain.