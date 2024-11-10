"""import subprocess

# Function to block an IP address in the firewall
def block_ip(ip_address):
    try:
        # Windows Firewall command to block the IP
        command = f'netsh advfirewall firewall add rule name="Block IP {ip_address}" dir=in action=block remoteip={ip_address}'
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully blocked IP address: {ip_address}")
    except subprocess.CalledProcessError as e:
        print(f"Error blocking IP address: {ip_address}. Details: {e}")

# Function to block a MAC address (by disabling the network interface with the specified MAC)
def block_mac(mac_address):
    try:
        # Command to get all network adapters and disable the one with the specific MAC
        command = f'wmic nic where "MACAddress=\'{mac_address}\'" call disable'
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully blocked MAC address: {mac_address}")
    except subprocess.CalledProcessError as e:
        print(f"Error blocking MAC address: {mac_address}. Details: {e}")

# Example prediction and threat detection
def handle_threat(y_pred, threat_ip, threat_mac):
    if y_pred == "malicious":  # Check if the prediction indicates a malicious entity
        print("Threat detected! Initiating blocking procedures.")
        block_ip(threat_ip)
        block_mac(threat_mac)
    else:
        print("No threat detected; no action taken.")

# Example usage
y_pred = "malicious"  # Replace this with your model's prediction output
threat_ip = "192.168.1.10"  # Replace with the IP of the detected threat
threat_mac = "00:14:22:01:23:45"  # Replace with the MAC of the detected threat

# Call the function to handle the threat based on y_pred
handle_threat(y_pred, threat_ip, threat_mac) """
import subprocess
import json
import requests
import os
import socket
from cryptography.fernet import Fernet

# Encrypt function for sensitive data
def encrypt_data(data):
    # Retrieve the encryption key from the environment variable
    key = os.getenv("ENCRYPTION_KEY")
    if key is None:
        raise ValueError("ENCRYPTION_KEY environment variable is not set.")
    
    # Ensure the key is in bytes format
    cipher_suite = Fernet(key.encode())
    return cipher_suite.encrypt(data.encode())

# Check for malicious activity and block
def handle_threat(y_pred, destination):
    if y_pred == "malicious":
        print("Threat detected! Initiating blocking procedures.")
        block_destination(destination)
        share_threat_intelligence(destination)

# Example function to share threat intelligence with an external SOAR platform
def share_threat_intelligence(destination):
    url = "https://soar-platform/api/threat-intel"
    headers = {"Authorization": "Bearer YOUR_API_TOKEN"}
    threat_data = {
        "destination": encrypt_data(destination),
        "timestamp": "2024-11-10T12:00:00Z"
    }
    response = requests.post(url, headers=headers, data=json.dumps(threat_data))
    print("Threat data shared with SOAR platform:", response.status_code)

# Function to block traffic to a specific IP or port
def block_destination(destination):
    try:
        # Resolve domain name to IP if it's a domain
        if "." in destination:
            ip_address = socket.gethostbyname(destination)
            print(f"Resolved {destination} to {ip_address}")
            command = f'netsh advfirewall firewall add rule name="Block IP {ip_address}" dir=out action=block remoteip={ip_address}'
        else:
            # Otherwise, assume it's a port number and block the port
            command = f'netsh advfirewall firewall add rule name="Block Port {destination}" dir=out action=block protocol=TCP remoteport={destination}'

        # Run the command to block the IP or port
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully blocked destination: {destination}")

    except socket.gaierror:
        print(f"Error: Could not resolve domain {destination}")
    except subprocess.CalledProcessError as e:
        print(f"Error blocking destination: {destination}. Details: {e}")

# Example usage
y_pred = "malicious"  # The model's prediction output
destination = "malicious-domain.com"  # Destination can be a domain or port number

# Call the function to handle the threat based on y_pred
handle_threat(y_pred, destination)

# Code to generate and print an encryption key (run this part once to set up your environment)
def generate_and_print_key():
    key = Fernet.generate_key()
    print(f"Your generated encryption key: {key.decode()}")
    # You will need to set this key as an environment variable:
    # In your terminal, run:
    # set ENCRYPTION_KEY=your_generated_key_here

# Uncomment the following line to generate a key (useful for initial setup)
# generate_and_print_key()
