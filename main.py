from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

serial_number = 0

def packet_handler(packet):
    global serial_number
    serial_number += 1

    if IP in packet:
        protocol_name = None

        if packet.haslayer(TCP):
            protocol_name = 'TCP'
        elif packet.haslayer(UDP):
            protocol_name = 'UDP'
        elif packet.haslayer(ICMP):
            protocol_name = 'ICMP'
        elif packet.haslayer(Raw):
            protocol_name = 'Raw'
        else:
            protocol_name = f"{packet[IP].proto}"

        # Get the payload data
        payload_data = packet[Raw].load if Raw in packet else b''
        payload_data_hex = payload_data.hex()

        # Convert payload data to text
        try:
            payload_data_text = payload_data.decode('utf-8')
            if not payload_data_text.isprintable():
                payload_data_text = "<Non-printable data>"
        except UnicodeDecodeError:
            # Handle non-decodable data
            payload_data_text = f"<Non-decodable data>"

        print(f"{serial_number:3d}        {packet[IP].src}        {packet[IP].dst}        {protocol_name}        {payload_data_hex}        {payload_data_text}")
        print("----------------------------")

print("Serial No. Source IP        Destination IP       Protocol        Payload data (hex)        Payload data (text)")

iface = input("Please enter the network interface name: ")


sniff(iface=iface, prn=packet_handler, count=100)
