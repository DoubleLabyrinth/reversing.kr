Password = []
Password.append(0x78 ^ 0x34)
Password.append(0x31)
Password.append(0x7c ^ 0x32)
Password.append(0x88 ^ 0xdd)
Password.append(0x58)
print(bytes(Password).decode())
