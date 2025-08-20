from scapy.all import sniff, IP, TCP, UDP, Raw

def packet_callback(packet):
    if IP in packet:
        proto = None
        src = packet[IP].src
        dst = packet[IP].dst

        # TCP traffic
        if TCP in packet:
            sport = packet[TCP].sport
            dport = packet[TCP].dport

            # Identify based on port numbers
            if sport == 25 or dport == 25:
                proto = "SMTP"
            elif sport == 110 or dport == 110:
                proto = "POP3"
            elif sport == 143 or dport == 143:
                proto = "IMAP"
            elif sport == 80 or dport == 80:
                proto = "HTTP"
            elif sport == 443 or dport == 443:
                proto = "HTTPS"
            elif sport == 21 or dport == 21:
                proto = "FTP"
            else:
                proto = "TCP"

        # UDP traffic
        elif UDP in packet:
            sport = packet[UDP].sport
            dport = packet[UDP].dport

            if sport == 53 or dport == 53:
                proto = "DNS"
            elif sport == 67 or dport == 68:
                proto = "DHCP"
            else:
                proto = "UDP"

        if proto:
            print(f"{proto} Packet: {src} -> {dst}")

            # If it has raw payload, print small preview
            if Raw in packet:
                data = packet[Raw].load
                print(f"Payload (first 50 bytes): {data[:50]}")

print("Starting packet capture... Press Ctrl+C to stop")
sniff(prn=packet_callback, store=0)
