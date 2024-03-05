# PRODIGY_CS_05 - Network Packet Analyzer

Welcome to PRODIGY_CS_05, a Python-based network packet analyzer tool developed for educational purposes. This tool uses the Scapy library to capture and analyze network packets, providing insights into source and destination IP addresses, protocols, and payload data.


## Features

- **Packet Capture:** Captures network packets in real-time.
- **Packet Analysis:** Extracts and displays information such as source and destination IP addresses, protocols, and payload data.
- **Payload Decoding:** Decodes payload data for a more human-readable presentation.
- **Logging:** Logs packet information to a file (`packet_log.txt`) for later analysis.

## Usage

1.Install Dependencies:
Ensure that you have Scapy installed. You can install it using the following command:

 ```bash
pip install scapy

2.Run the Packet Sniffer:
Open a terminal or command prompt, navigate to the directory containing the script (packet_sniffer.py), and execute the following command:

 ```bash
python packet_sniffer.py

The script will start capturing and analyzing packets. Press Ctrl+C to stop the packet sniffer.

3.View Log File:
The script logs packet information to a file named packet_log.txt. You can open this file to review the captured data.

 ```bash
# On Windows
type packet_log.txt

# On Unix-like systems
cat packet_log.txt

4.Installation:
If you haven't cloned the repository yet, you can do so using the following commands:

 ```bash
git clone https://github.com/your-username/PRODIGY_CS_05.git
cd PRODIGY_CS_05

Follow the instructions in the Usage section to run the packet sniffer.

##Dependencies
Scapy: A powerful interactive packet manipulation program.

Important Notes
Permissions:
Ensure that you have the necessary permissions to capture network traffic and comply with legal and ethical considerations.

Educational Purpose:
This tool is developed for educational purposes and should be used responsibly.

License
This project is licensed under the MIT License.

PRODIGY_CS_05 - Network Packet Analyzer is a project created for educational purposes. Developed by Aman Ali.

Contact
For any inquiries, please contact [96.amanali@gmail.com].
