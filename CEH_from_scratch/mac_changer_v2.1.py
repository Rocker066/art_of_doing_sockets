import optparse
import subprocess
import re


""""
This script uses the option parser module to 
take the arguments in one line as the script runs,
i.e python mac_changer-v2 --interface wlan0 --mac 00:11:22:33:44:55
"""

def get_arguments():
    """Creates a parser object and gets the options and arguments"""

    # Create a parser object
    parser = optparse.OptionParser()

    # Using parser to add options as arguments to expect from users and pars it('dest' is the variable to link the args to)
    parser.add_option('-i', '--interface', dest='interface', help='Interface to change its MAC address')
    parser.add_option('-m', '--mac', dest='new_mac', help='New MAC address')

    # Return the options from the output of the parser
    options, arguments = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify both an interface and a MAC address.")
    elif not options.new_mac:
        parser.error("[-] Please specify both an interface and a MAC address.")

    return options


def change_mac(interface, new_mac):
    """Change the mac address to the given address"""

    print(f'[*] Changing MAC address for {interface} to {new_mac}')

    # Safe way to execute command line arguments
    if subprocess.call(['ip', 'link', 'set', interface, 'down']) != 0:
        print(f'[-] Failed to bring down {interface}')
        return
    if subprocess.call(['ip', 'link', 'set', interface, 'address', new_mac]) != 0:
        print(f'[-] Failed to change MAC address for {interface}')
        return
    if subprocess.call(['ip','link', 'set', interface, 'up']) != 0:
        print(f'[-] Failed to bring up {interface}')
        return


def get_current_mac(interface):
    """Get the current mac address"""
    ifconfig_result = subprocess.check_output(['ifconfig', interface]).decode('utf-8')

    mac_address_search_result = re.search(r"\w+:\w+:\w+:\w+:\w+:\w+", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print('[-] Could not read MAC address!')


# Get the arguments set for the commands
options = get_arguments()

# Get the current mac address of the interface
current_mac = get_current_mac(options.interface)
print(f'Current MAC: {current_mac}')

# Change the mac address based on the user input
change_mac(options.interface, options.new_mac)

# Check if the current mac is the same as user input
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print(f'[+] MAC address was successfully changed to {current_mac}')
else:
    print('[-] MAC address did not get Changed')