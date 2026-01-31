#!/usr/bin/env python
import sys
import socket
import fcntl
import struct
import array

SIOCGIFCONF = 0x8912
STRUCT_SIZE_32 = 32
STRUCT_SIZE_64 = 40
PLATFORM_32_MAX_NUMBER = 2**32
DEFAULT_INTERFACES = 8

def list_interfaces():
    interfaces = []
    max_interfaces = DEFAULT_INTERFACES
    is_64bits = sys.maxsize > PLATFORM_32_MAX_NUMBER
    struct_size = STRUCT_SIZE_64 if is_64bits else STRUCT_SIZE_32
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        bytes = max_interfaces * struct_size
        names = array.array('B', b'\0' * bytes)
        outbytes = struct.unpack(
            'iL',
            fcntl.ioctl(
                sock.fileno(),
                SIOCGIFCONF,
                struct.pack('iL', bytes, names.buffer_info()[0])
            )
        )[0]
        if outbytes == bytes:
            max_interfaces *= 2
        else:
            break

    namestr = names.tobytes()
    for i in range(0, outbytes, struct_size):
        interfaces.append(namestr[i:i+16].split(b'\0', 1)[0].decode())
    return interfaces

if __name__ == '__main__':
    interfaces = list_interfaces()
    print("This machine has %d network interfaces: %s" %
          (len(interfaces), interfaces))
