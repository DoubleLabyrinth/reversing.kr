#!/usr/bin/env python3

def ROT_L(num : int, shift : int, bits = 32):
    return ((num << shift) | (num >> (bits - shift))) & (2 ** bits - 1)

def ROT_R(num : int, shift : int, bits = 32):
    return ((num >> shift) | (num << (bits - shift))) & (2 ** bits - 1)

flag = []
flag.append(ROT_L(ord('I'), 6, 8))
flag.append(0x69 ^ 0x20)
flag.append(0x35 ^ 0x77)
flag.append(0x64 ^ 0x21)
flag.append(0x8 ^ 0x46)
flag.append(ROT_R(0x14, 4, 8))
flag = bytes(flag).decode()
print(flag)
