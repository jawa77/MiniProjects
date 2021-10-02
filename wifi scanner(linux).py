# scapy.ls(scapy.ARP()) ithu scapy.ARP la ena ena la use panalam nu sollum ex pdst kara type
# scapy.ls(scapy.Ether()) ithu scapy.Eather la ena use panalam nu sollum
# ff:ff:ff karathu antha wifi la irukka ella device kum req pogum
# verbose=false karathu munnati try pandrathu katathu
# .suumary namaku purummaru varum


import scapy.all as scapy
import optparse

def get_arguments():
    parser=optparse.OptionParser()
    parser.add_option("-r","--range", dest="range", help="use -r or --range to enter ip ")
    optio = parser.parse_args()[0]
    if not optio.range:
        parser.error("specified options -r or search -h to help")
    else:
        return optio


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    source_destination = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")     #    dest eenanu theriyathu so ff.ff
    final = source_destination / arp_request    #    src and dest aa arp req aa anupum
    answered_list = scapy.srp(final, timeout=2, verbose=False)[0]


    #   verbose false outputla vara words lam katathu
    #   scapy.srp req ya send pannum

    result_list = []
    for answer in answered_list:
        result_dic = {"ip": answer[1].psrc, "mac": answer[1].hwsrc}
        result_list.append(result_dic)
    return result_list


def print_result(result_list):
    print("IP\t\t\tMAC ADDRESS\n....................................")
    for result in result_list:
        print(result["ip"] + "\t\t" + result["mac"])



print("""
 ##--------------------------------------------##
 #|                                            |#
 #|       **** LINUX ONLY ****                 |#
 #|                                            |#
 #|      WIFI SCANNER>>>                       |#
 #|                  BY.....                   |#
 #|                                            |#
 #|                    |*| cyber_jawahar       |#
 #|                                            |#
 ##--------------------------------------------##\n
 """)

optio =get_arguments()
result_dic = scan(optio.range)
print_result(result_dic)
