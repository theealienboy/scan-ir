#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# glan suas an teacs
subprocess.call('clear', shell=True)

# Cuir teacs anseo
remoteServer    = raw_input("Riomhaire iargúlta:")
remoteServerIP  = socket.gethostbyname(remoteServer)

# priontáil bratach deas
print "-" * 60
print "Fan socind amhain", remoteServerIP
print "-" * 60
