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

#Store all the banned ips here so that you dont keep banning the same ip
bannedIps = []


#Define the socket listener function.
#Except two variables, the host ip string, and a port as an integer
def startListen(host, port):

	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Bind the socket to the address given on the command line
	server_address = (host, port)
	sock.bind(server_address)
	print >>sys.stderr, 'starting up on %s port %s' % sock.getsockname()
	sock.listen(1)

	#Create an infinite loop in order to wait for a connection
	while True:
		print >>sys.stderr, 'waiting for a connection'
		connection, client_address = sock.accept()
		try:
			print >>sys.stderr, 'client connected:', client_address
			

			#Clean up the client_address variable, as it has a port number on the end and some other special characters
			addr = str(client_address).replace('(','')
			addr = addr.replace('\'','')
			split = addr.split(',')
			
			#after the clean up you should end up with just an ip address
			ipToBan = split[0]
			print "I am banning: "+ipToBan
			
			#check if the ip you are trying to banned has already been autobanned, sometimes the connection wont close in time or you forgot to turn your firewall on
			isIpBanned = False
			for bannedIp in bannedIps:
				if bannedIp == ipToBan:
					isIpBanned = True
					print "Check your firewall, ip has been banned already... :"+ipToBan
					break
					
			if isIpBanned == False:
				autoBan(ipToBan)
					
			#Check if the ip address matchs your banned ip list
			#send the clients ip that connected to you over to autoBan function
				autoBan(ipToBan)

		finally:
			connection.close()

# Define autoBan function and accept an ip address
# This function will generate a random number, and a command
# Its using the netsh firewall command to add a rule to block the ip address you passed to it.
# The random number is generated to add to the rule name so it doesnt over write
def autoBan(host):
	randomNum=str(random.randrange(1, 1000000))
	command="netsh advfirewall firewall add rule name=\"BAN"+randomNum+"\" protocol=TCP action=block dir=IN remoteip="+host
	print command
	os.system(command)
	
	#add the ip to the list of banned ips
	bannedIps.append(host)

	
### MAIN APPLICATION ####
if __name__ == '__main__':
	
		#Print banner
	print "\n\n\n\n-----------------------------------"
	print "Auto Ban Hosts on Scan v1.0 by m0r3Sh3LLs"
	print "-----------------------------------\n\n\n\n"
	
	
	#Listen on any address using 0.0.0.0
	host='0.0.0.0'
	port=22
	#start your listener, and pass the host string, and port number
	startListen(host, port)
