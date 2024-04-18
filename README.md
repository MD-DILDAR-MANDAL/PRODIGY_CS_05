# PRODIGY_CS_05
# Network Packet Sniffer

This project is a simple network packet sniffer that captures network packets on a specified network interface. It displays information about the captured packets, including source IP, destination IP, protocol, payload data in hex, and payload data in text.

## Features

- Captures network packets on a specified network interface.
- Displays source IP, destination IP, protocol, payload data in hex, and payload data in text.
- Handles non-decodable data gracefully by marking it as `<Non-decodable data>`.

## Requirements

- Python 3.x
- Required Python packages are listed in the [requirements.txt](requirements.txt) file.

## Installation

1. Clone the repository:

    ```shell
    git clone <repository_url>
    cd <repository_name>
    ```

2. Install the required packages using `pip`:

    ```shell
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:

    ```shell
    python packet_sniffer.py
    ```

2. When prompted, enter the network interface name you want to sniff traffic on (e.g., `Wi-Fi`, `eth0`, `en0`, etc.).

3. The script will start capturing network packets on the specified network interface and print the information about each packet to the console.

## Output

- The script prints the following information for each captured packet:
    - Serial number
    - Source IP
    - Destination IP
    - Protocol
    - Payload data in hex
    - Payload data in text



## Disclaimer

**Use this script with caution.** Capturing network traffic may be illegal in certain jurisdictions without the appropriate permissions. It may also violate privacy laws and company policies. Always ensure you have the necessary permissions and authorization to capture network traffic on the specified interface. The author of this script is not responsible for any misuse or legal issues arising from the use of this script.

## Note

- Use this script with caution and make sure you have the necessary permissions to capture network traffic on the specified interface.
