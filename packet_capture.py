from scapy.all import sniff
import pandas as pd

packets_list = []

def packet_callback(packet):
    if packet.haslayer('IP'):
        packet_info = {
            'src': packet['IP'].src,
            'dst': packet['IP'].dst,
            'length': len(packet),
            'proto': packet['IP'].proto,
        }
        packets_list.append(packet_info)

def capture_packets(count=100):
    print(f"Capturing {count} packets...")
    sniff(prn=packet_callback, count=count)
    df = pd.DataFrame(packets_list)
    df.to_csv('packets.csv', index=False)
    print("Packet data saved to packets.csv")

if __name__ == "__main__":
    capture_packets()
