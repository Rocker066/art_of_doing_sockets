import argparse
import subprocess
import sys


# Define the functions
def change_mac(interface, new_mac):
    print(print(f"[*] Changing MAC address for {interface} to {new_mac}"))
    try:
        # Bring the interface down
        subprocess.run(['ip', 'link', 'set', interface, 'down'], check=True)
        # Change the MAC address
        subprocess.run(['ip', 'link', 'set', interface, 'address', new_mac], check=True)
        # Bring the interface back up
        subprocess.run(['ip', 'link', 'set', interface, 'up'])
        print('Done')
        return
    except subprocess.CalledProcessError as e:
        print(f'[-] Failed to change MAC address: {e}', file=sys.stderr)
        return


def main():
    # Define variables
    # Create a parser object
    parser = argparse.ArgumentParser(description='Change the MAC address of a network interface')

    parser.add_argument(
        '-i', '--interface',
        required=True,
        help='The network interface to change its MAC address.',
    )
    parser.add_argument(
        '-m', '--mac',
        required=True,
        help="The new MAC address to set.",
    )

    args = parser.parse_args()

    if not args.interface or not args.mac:
        print('[-] Please specify both an interface and a MAC address.')
        parser.print_help()
        return 1  # Indicate failure

    try:
        change_mac(args.interface, args.mac)
        return 0  # Indicate success
    except Exception as e:
        print(f"[-] An error occurred: {e}", file=sys.stderr)
        return 1  # Indicate failure


if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)  # Exit with the appropriate status code