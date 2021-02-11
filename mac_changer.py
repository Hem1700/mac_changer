#!/usr/bin/env python

import subprocess
import optparse

def change_mac(interface , new_mac):
    print("[+] Changing MAC Address for " + interface + " to" + new_mac)
    # subprocess.call("ifconfig " + interface + " down ", shell=True)
    # subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
    # subprocess.call("ifconfig " + interface + " up ", shell=True)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m" , "--mac" , dest="new_mac" , help = "New MAC address")

(options, argument)= parser.parse_args()
change_mac(options.interface , options.new_mac)


