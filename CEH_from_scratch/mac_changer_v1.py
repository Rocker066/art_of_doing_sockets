import optparse
import subprocess


interface = input('Interface> ')
new_mac = input('new MAC> ')
print(f'[*] Changing MAC address for {interface} to {new_mac}')

# Unsafe way
# subprocess.call(f'ifconfig {interface} down', shell=True)
# subprocess.call(f'ifconfig {interface} hw ether {new_mac}', shell=True)
# subprocess.call(f'ifconfig {interface} up')

# Safe way
subprocess.call(['ifconfig', interface, 'down'])
subprocess.call(['ifconfig', interface, 'hw' ,'ether', new_mac])
subprocess.call(['ifconfig', interface, 'up'])