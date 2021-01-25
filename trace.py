# This tool takes ip address as argument from user
# Then a loop is run 20 times for the amount of hops that are needed which is 20 here.
# A random source port and destination port is assigned to the created packet in every loop
# Then this packet is sent out with a timeout of 3 second, and incoming reply is listened for.
# If we get a reply and if it is not the final destination then the loop is run again.
# Packets are sent out with increasing ttl till the destination is reached or loop counter reaches 20.

from scapy.all import *
import sys
import random

if __name__ == "__main__":
    try:
        hostname = str(sys.argv[1])
    except:
        print("IP address not entered !! EXITING ....")
        exit(1)
    temp=hostname[:]
    temp=temp.split('.')
    for t in temp:
        if not t.isdigit():
            print("Input is not a valid IP Address")
            exit(1)
    for i in range(1, 21):
        random.seed()
        destport=random.randint(33434,33464)
        sourceport=random.randint(9000,9999)
        pkt = IP(dst=hostname, ttl=i) / UDP(dport=destport,sport=sourceport)
        # Send the packet and get a reply
        reply = sr1(pkt, verbose=0,timeout=3)
        if reply is None:
        # No reply =(
            print(str(i) + ".\t*")
            continue
        elif reply.type == 3:
        # We've reached our destination
             print (str(i) + ".\t" + reply.src)
             break
        else:
        # We're in the middle somewhere
            print (str(i) + ".\t" + reply.src)
