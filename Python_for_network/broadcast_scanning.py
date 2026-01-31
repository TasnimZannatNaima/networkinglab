from scapy.all import sniff, IP, TCP
import os

captured_data = {}
END_PORT = 1000

def monitor_packet(pkt):
    if IP in pkt:
        src_ip = pkt[IP].src

        if src_ip not in captured_data:
            captured_data[src_ip] = []

        if TCP in pkt:
            sport = pkt[TCP].sport
            if sport <= END_PORT:
                if str(sport) not in captured_data[src_ip]:
                    captured_data[src_ip].append(str(sport))

        os.system("clear")
        print("Captured IP addresses and ports:\n")
        for ip in sorted(captured_data.keys()):
            ports = ", ".join(captured_data[ip])
            if ports:
                print(f"{ip} ({ports})")
            else:
                print(ip)

if __name__ == "__main__":
    print("Starting packet sniffing... Press CTRL+C to stop.\n")
    sniff(prn=monitor_packet, store=False)
from scapy.all import sniff, IP, TCP
import os

captured_data = {}
END_PORT = 1000

def monitor_packet(pkt):
    if IP in pkt:
        src_ip = pkt[IP].src

        if src_ip not in captured_data:
            captured_data[src_ip] = []

        if TCP in pkt:
            sport = pkt[TCP].sport
            if sport <= END_PORT:
                if str(sport) not in captured_data[src_ip]:
                    captured_data[src_ip].append(str(sport))

        os.system("clear")
        print("Captured IP addresses and ports:\n")
        for ip in sorted(captured_data.keys()):
            ports = ", ".join(captured_data[ip])
            if ports:
                print(f"{ip} ({ports})")
            else:
                print(ip)

if __name__ == "__main__":
    print("Starting packet sniffing... Press CTRL+C to stop.\n")
    sniff(prn=monitor_packet, store=False)
