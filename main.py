
import platform
import socket
import subprocess
import re
from datetime import datetime


def show_system_info():
    print("\n========== SYSTEM INFORMATION ==========")
    print(f"Computer Name : {platform.node()}")
    print(f"Operating System : {platform.system()}")
    print(f"OS Version : {platform.version()}")
    print(f"Architecture : {platform.machine()}")
    print(f"Processor : {platform.processor()}")
    print(f"Python Version : {platform.python_version()}")
    print("=========================================\n")


def show_network_info():
    print("\n========== NETWORK INFORMATION ==========")

    hostname = socket.gethostname()

    try:
        local_ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        local_ip = "Unable to detect"

    print(f"Hostname : {hostname}")
    print(f"Local IP Address : {local_ip}")

    try:
        socket.gethostbyname("google.com")
        print("Internet DNS : Available")
    except socket.gaierror:
        print("Internet DNS : Unavailable")

    print("=========================================\n")


def ping_host():
    print("\n========== NETWORK PING ==========")

    host = input("Enter IP Address or Hostname: ").strip()

    if not re.fullmatch(r"[a-zA-Z0-9.-]+", host):
        print("Invalid hostname or IP address.")
        return

    if host.startswith(".") or host.endswith(".") or ".." in host:
        print("Invalid hostname.")
        return

    try:
        command = ["ping", "-n", "4", host] if platform.system() == "Windows" else ["ping", "-c", "4", host]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=15
        )

        print(result.stdout)

        if result.returncode == 0:
            print("Result: Host is reachable.")
        else:
            print("Result: Host is unreachable or did not respond.")

    except subprocess.TimeoutExpired:
        print("Ping timed out.")

    except FileNotFoundError:
        print("Ping command is not available.")


def main():
    while True:
        print("\n===================================")
        print("       WINDOWS IT SUPPORT TOOLKIT")
        print("===================================")
        print("1. System Information")
        print("2. Network Information")
        print("3. Ping Test")
        print("4. Exit")
        print("===================================")

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            show_system_info()

        elif choice == "2":
            show_network_info()

        elif choice == "3":
            ping_host()

        elif choice == "4":
            print("Thank you for using Windows IT Support Toolkit!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
