#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('clear', shell=True)

#adding an initial ping
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Create a TCP/IP socket
server_ip = raw_input(‘Enter server IP : ‘)
rep = os.system(‘ping ‘ + server_ip)
if rep == 0:
print ‘n n server is up n n’
else:
print ‘server is down’



# Ask for input
remoteServer    = raw_input("Riomhaire iargúlta: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print "-" * 60
print "Fan socind amhain, le do thoil", remoteServerIP
print "-" * 60

# Check what time the scan started
t1 = datetime.now()

# Using the range function to specify ports (here it will scans all ports between 1 and 1024)

# We also put in some error handling for catching errors

#for port in range(0,65535):

try:
    for port in range(0,65535):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Port {}:   Open".format(port)
        sock.close()

except KeyboardInterrupt:
    print "Bhrúigh tú Ctrl+C"
    sys.exit()

except socket.gaierror:
    print 'Níl a fhios agam an riomhaire. Tá muid ag imeacht'
    sys.exit()

except socket.error:
    print "Tá fadhbanna againn"
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print 'Scanning Completed in: ', total


