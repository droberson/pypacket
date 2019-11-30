import pcapy
import pypacket

pcap_file = "example.pcap"
capture = pcapy.open_offline(pcap_file)

while True:
    next_packet = capture.next()
    if next_packet[0] is None:
        capture.close()
        break
    pkt = pypacket.Packet(next_packet[1])
    print(pkt.daddr, pkt.saddr, pkt.protocol)
