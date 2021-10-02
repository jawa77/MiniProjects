import subprocess
import optparse

def add_option():
    a = optparse.OptionParser()
    a.add_option("-i","--interface",dest="interface", help="used to change interface")
    a.add_option("-m","--mac",dest="new_mac", help="used to select mac")
    #option it define wlan0,12.3.4.5 (values)
    #argument it have interface , mac (variable)
    #argument not nessesary
    (options,arguments)= a.parse_args()
    if not options.interface:
        a.error("interface is not specified= use -h to help ")
    elif not options.new_mac:
        a.error("mac id is not specified = use -h to help")
    else:
        return (options,arguments)


def change_mac(interface,new_mac):
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])
    print("\n\n*********SUCCESS FULLY EXECUTED**........\n\n\Your Mac Is Changed = " + new_mac)


print("""
 ##--------------------------------------------##
 #|                                            |#
 #|       **** LINUX ONLY ****                 |#
 #|                                            |#
 #|      MAC CHANGER>>>                        |#
 #|                  BY.....                   |#
 #|                                            |#
 #|                    |*| cyber_jawahar       |#
 #|                                            |#
 ##--------------------------------------------##\n
 """)
 
(options,arguments)=add_option()
change_mac(options.interface,options.new_mac)


