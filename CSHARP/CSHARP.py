#!/usr/bin/env python3
import base64

encrypted_password = b'\x4a\x57\x4d\x46\x1d\x31\x75\xee\xf1\xe2\xa3\x2c'
mask = b'\x10\x11\x21\x33\x44\x66\x33\xa0\x90\xb5\xee\x11'

password = []
for i in range(len(encrypted_password)):
    password.append(encrypted_password[i] ^ mask[i])
password = base64.b64decode(bytes(password).decode())

print(password.decode())
