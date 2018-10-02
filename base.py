#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# glan suas an teacs
subprocess.call('clear', shell=True)

# Cuir teacs anseo
remoteServer    = input("Riomhaire iargúlta: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

# priontáil bratach deas
print ("-" * 60)
print ("Fan socind amhain"), remoteServerIP
print ("-") * 60

try:
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Port {}: 	 Open".format(port)
        sock.close()

except KeyboardInterrupt:
    print "bhrúigh tú Ctrl+C"
    sys.exit()

except socket.error:
    print 'Ní fheicall an rionamire. Tá mé ag imeacht'
    sys.exit()

except socket.error:
    print "Níl me abalta "
    sys.exit()

