import optparse
import sys
import subprocess
import re


def change_mac(interface, new_mac):
    if subprocess.run(['ip', 'link', 'set', interface, 'down']) != 0:
        print('Failed to bring down the interface')
        return
    subprocess.run(['ip', 'link', 'set', interface, 'address', new_mac])
    subprocess.run(['ip', 'link', 'set', interface, 'up'])
    print('[+] MAC address successfully changed.')



interface = input('[+] Enter the interface: ')
new_mac = input('[+] Enter new MAC address: ')
print(f'Changing MAC address for {interface} to {new_mac}')

change_mac(interface, new_mac)





