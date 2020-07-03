import socket, sys
from struct import *

#Convert a string of 6 characters of ethernet address into a dash separated hex string
def eth_addr (a) :
  b = &quot;%.2x:%.2x:%.2x:%.2x:%.2x:%.2x&quot; % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5]))
  return b

#create a AF_PACKET type raw socket (thats basically packet level)
#define ETH_P_ALL    0x0003          /* Every packet (be careful!!!) */
try:
	s = socket.socket( socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0003))
except
	print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()

# receive a packet
while True:
	packet = s.recvfrom(65565)
	
	#packet string from tuple
	packet = packet[0]
	
	#parse ethernet header
	eth_length = 14
	
	eth_header = packet[:eth_length]
	eth = unpack('!6s6sH' , eth_header)
	eth_protocol = socket.ntohs(eth[2])
    print('Wilma Gutierrez Catari   CI 8424117')
    print('Destination MAC : ' + eth_addr(packet[0:6]))
    print('Source MAC : ' + eth_addr(packet[6:12]))
    print('Protocol : ' + str(eth_protocol))

		#ICMP Packets
	if protocol == 1 :
			u = iph_length + eth_length
			icmph_length = 4
			icmp_header = packet[u:u+4]

			#now unpack them :)
			icmph = unpack('!BBH' , icmp_header)
			
			icmp_type = icmph[0]
			code = icmph[1]
			checksum = icmph[2]
			
            print('Type : ' + str(icmp_type))
            print(' Code : ' + str(code))
            print(' Checksum : ' + str(checksum))
			h_size = eth_length + iph_length + icmph_length
			data_size = len(packet) - h_size
			
			#get data from the packet
			data = packet[h_size:]
			
			print ('Data : ' + data)

		#UDP packets
		elif protocol == 17 :
			u = iph_length + eth_length
			udph_length = 8
			udp_header = packet[u:u+8]

			#now unpack them :)
			udph = unpack('!HHHH' , udp_header)
			
			source_port = udph[0]
			dest_port = udph[1]
			length = udph[2]
			checksum = udph[3]
			
			print('Source Port : ' + str(source_port))
            print(' Dest Port : ' + str(dest_port))
            print(' Length : ' + str(length) )
            print(' Checksum : ' + str(checksum))
			h_size = eth_length + iph_length + udph_length
			data_size = len(packet) - h_size
			
			#get data from the packet
			data = packet[h_size:]
			
			print ('Data : ' + data)

		#some other IP packet like IGMP
		else :
			print ('Protocol other than TCP/UDP/ICMP')
			
		print("")