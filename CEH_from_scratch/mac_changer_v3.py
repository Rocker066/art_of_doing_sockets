import argparse
import subprocess
import sys

"""
This script uses the argparse module to take arguments when the script runs.
Example usage: python mac_changer-v2.py --interface wlan0 --mac 00:11:22:33:44:55
"""


def change_mac(interface: str, new_mac: str) -> None:
    """
    Change the MAC address of the specified network interface.

    Args:
        interface (str): The name of the network interface.
        new_mac (str): The new MAC address to set.

    Returns:
        None
    """
    print(f"[*] Changing MAC address for {interface} to {new_mac}")

    try:
        # Bring the interface down
        subprocess.run(["ip", "link", "set", interface, "down"], check=True)
        # Change the MAC address
        subprocess.run(["ip", "link", "set", interface, "address", new_mac], check=True)
        # Bring the interface back up
        subprocess.run(["ip", "link", "set", interface, "up"], check=True)
        print("[+] MAC address changed successfully")
    except subprocess.CalledProcessError as e:
        print(f"[-] Failed to change MAC address: {e}", file=sys.stderr)


def main() -> None:
    """
    Main function to parse command-line arguments and invoke the MAC changer.

    Returns:
        None
    """
    parser = argparse.ArgumentParser(
        description="Change the MAC address of a network interface."
    )
    parser.add_argument(
        "-i",
        "--interface",
        required=True,
        help="The network interface to change its MAC address.",
    )
    parser.add_argument(
        "-m",
        "--mac",
        required=True,
        help="The new MAC address to set.",
    )

    args = parser.parse_args()

    if not args.interface or not args.mac:
        print("[-] Please specify both an interface and a MAC address.")
        parser.print_help()
        sys.exit(1)

    change_mac(args.interface, args.mac)


if __name__ == "__main__":
    main()