#       AUTOBAN SCRIPT
#       Copyrighted:  Chris & m0r3Sh3LLs  http://m0r3sh3lls.blogspot.com/
#       #	Version: 1.0
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

#!/usr/bin/env python
import socket
import sys
import os
import random

def startListen(host, port):

	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Bind the socket to the address given on the command line
	server_address = (host, port)
	sock.bind(server_address)
	print >>sys.stderr, 'starting up on %s port %s' % sock.getsockname()
	sock.listen(1)

	while True:
		print >>sys.stderr, 'waiting for a connection'
		connection, client_address = sock.accept()
		try:
			print >>sys.stderr, 'client connected:', client_address
			while True:
				addr = str(client_address).replace('(','')
				addr = addr.replace('\'','')
				split = addr.split(',')
				ip = split[0]
				
				
				autoBan(ip)
				#data = connection.recv(16)
				#print >>sys.stderr, 'received "%s"' % data
				#if data:
				#	connection.sendall(data)
				#else:
				break
		finally:
			connection.close()

def autoBan(host):
	randomNum=str(random.randrange(1, 1000000))
	command="netsh advfirewall firewall add rule name=\"BAN"+randomNum+"\" protocol=TCP action=block dir=IN remoteip="+host
	print command
	os.system(command)
### MAIN APPLICATION ####

host='0.0.0.0'
port=22
startListen(host, port)

