#!/user/bin/env python

import subprocess

interface = input("What is the name of the interface? ")
new_mac = input("What is the new mac address? ")

print(" Changing MAC address for " + interface + " to " + new_mac)

#subprocess.call("ifconfig " + interface + " down", shell=True)
#subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
#subprocess.call("ifconfig " + interface + " up", shell=True)

subprocess.call(["ifconfig", interface, "down"]),
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "down"])