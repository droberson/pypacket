#!/usr/bin/env python3

from time import sleep
from pysniffer import Sniffer

capture = Sniffer("lo")
capture.start()
capture.setnonblock()

while True:
    packet = capture.next()
    if not packet:
        sleep(0.05)
        continue
    print(packet.protocol, packet.daddr, packet.saddr, packet.sport, packet.dport, packet.data)
