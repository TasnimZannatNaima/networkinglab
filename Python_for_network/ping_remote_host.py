#!/usr/bin/env python
import os
import socket
import struct
import select
import time
import argparse

ICMP_ECHO_REQUEST = 8

def checksum(data):
    s = 0
    for i in range(0, len(data), 2):
        s += (data[i] << 8) + (data[i+1] if i+1 < len(data) else 0)
    s = (s >> 16) + (s & 0xffff)
    return ~s & 0xffff

def ping(host):
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    packet_id = os.getpid() & 0xFFFF
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, 0, packet_id, 1)
    data = struct.pack("d", time.time())
    chksum = checksum(header + data)
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0,
                          socket.htons(chksum), packet_id, 1)
    packet = header + data
    sock.sendto(packet, (host, 1))
    sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--target-host', required=True)
    args = parser.parse_args()
    ping(args.target_host)
