import argparse
import socket
import struct
import fcntl
import nmap

SAMPLE_PORTS = '21-23'

def get_interface_status(ifname):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip_address = socket.inet_ntoa(
        fcntl.ioctl(
            sock.fileno(),
            0x8915,
            struct.pack('256s', ifname[:15].encode())
        )[20:24]
    )
    nm = nmap.PortScanner()
    nm.scan(ip_address, SAMPLE_PORTS)
    return nm[ip_address].state()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ifname', required=True)
    args = parser.parse_args()

    print("Interface [%s] is: %s" %
          (args.ifname, get_interface_status(args.ifname)))
