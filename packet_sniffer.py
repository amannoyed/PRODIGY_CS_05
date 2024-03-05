from scapy.all import *

def packet_analysis(packet):
    try:
        # Check if packet is IPv4
        if packet.haslayer(IP):
            # Get source and destination IP addresses
            source_ip = packet[IP].src
            destination_ip = packet[IP].dst

            # Get protocol
            protocol = packet[IP].proto

            # Decode payload data if available
            payload = ""
            if packet.haslayer(Raw):
                payload = packet[Raw].load.decode(errors='ignore')

            # Print packet information
            print(f"Source IP: {source_ip}")
            print(f"Destination IP: {destination_ip}")
            print(f"Protocol: {protocol}")
            print(f"Payload: {payload}")
            print("--------------------------------")

            # Log to a file
            with open('packet_log.txt', 'a') as log_file:
                log_file.write(f"Source IP: {source_ip}, Destination IP: {destination_ip}, Protocol: {protocol}, Payload: {payload}\n")

    except Exception as e:
        print(f"Error processing packet: {e}")

# Start sniffing
sniff(filter="ip", prn=packet_analysis)
