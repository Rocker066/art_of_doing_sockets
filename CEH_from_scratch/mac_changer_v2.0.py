import optparse
import subprocess


""""
This script uses the option parser module to 
take the arguments in one line as the script runs,
i.e python mac_changer-v2 --interface wlan0 --mac 00:11:22:33:44:55
"""


def change_mac(interface, new_mac):
    """Change the mac address to the given address"""

    print(f'[*] Changing MAC address for {interface} to {new_mac}')
    # Safe way to execute command line arguments
    if subprocess.call(['ip', 'link', 'set', interface, 'down']) != 0:
        print(f'[-] Failed to bring down {interface}')
    if subprocess.call(['ip', 'link', 'set', interface, 'address', new_mac]) != 0:
        print(f'[-] Failed to change MAC address for {interface}')
    if subprocess.call(['ip','link', 'set', interface, 'up']) != 0:
        print(f'[-] Failed to bring up {interface}')
    print('[+] MAC address changed successfully')


def main():
    # Create a parser object
    parser = optparse.OptionParser()

    # Using parser to add options as arguments to expect from users and pars it('dest' is the variable to link the args to)
    parser.add_option('-i', '--interface', dest='interface', help='Interface to change its MAC address')
    parser.add_option('-m', '--mac', dest='new_mac', help='New MAC address')

    # Capture the options and arguments from the output of the parser
    options, arguments = parser.parse_args()

    # Set variables to get interface and new mac from the user
    interface = options.interface
    new_mac = options.new_mac

    if interface is None or new_mac is None:
        print('[-] Please specify an interface and a MAC address\n '
              'usage: --interface [INTERFACE] --new_mac [MAC ADDRESS]')
        exit(1)

    change_mac(interface, new_mac)


if __name__ == '__main__':
    main()
