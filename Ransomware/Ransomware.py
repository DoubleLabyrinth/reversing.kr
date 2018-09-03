#!/usr/bin/env python3

key = []
plaintext = b'This program cannot be run in DOS mode'
ciphertext = bytes.fromhex('C7 F2 E2 FF AF E3 EC E9'
                           'FB E5 FB E1 AC F0 FB E5'
                           'E2 E0 E7 BE E4 F9 B7 E8'
                           'F9 E2 B3 F3 E5 AC CB DC'
                           'CD A6 F1 F8 FE E9')
for i in range(len(plaintext)):
    key.append(plaintext[i] ^ 0xff ^ ciphertext[i])
key = bytes(key)
print(key.decode())
