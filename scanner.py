#!/bin/python3

import pyfiglet
import sys
import socket
from datetime import datetime


if len(sys.argv)==2:
	target = socket.gethostbyname(sys.argv[1]) #translate hostname to ipv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")
#banner
print("-" * 80)
print(pyfiglet.figlet_format("poFlash", font="slant"))
print("-" * 80)
print("This port scanner is built by 0xHans")
print("-" * 80)
print("Scanning target: "+target)
print("Time started: "+str(datetime.now()))
print("-" * 80)

try:
	for port in range(0,1023):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print(f"Port {port} is open")
		s.close()

except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Could not connect to the server.")
	sys.exit()
