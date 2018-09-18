#!/usr/bin/env python3
start_addr = 0xa

def Process_2(b : bytes, i : int):
    print('loc_%08x    ' % i, end = '')
    print('%-10s' % b[i:i + 3].hex(), end = '')
    print('mov byte ptr[%d], 0x%02x' % (b[i + 1], b[i + 2]))
    return 3

def Process_6(b : bytes, i : int):
    print('loc_%08x    ' % i, end = '')
    print('%-10s' % b[i:i + 3].hex(), end = '')
    print('xor byte ptr[%d], byte ptr[%d]' % (b[i + 1], b[i + 2]))
    return 3

def Process_7(b : bytes, i : int):
    print('loc_%08x    ' % i, end = '')
    print('%-10s' % b[i:i + 3].hex(), end = '')
    print('cmp byte ptr[%d], byte ptr[%d]' % (b[i + 1], b[i + 2]))
    return 3

def Process_9(b : bytes, i : int):
    print('loc_%08x    ' % i, end = '')
    print('%-10s' % b[i:i + 2].hex(), end = '')
    print('jnz loc_%08x' % (start_addr + b[i + 1]))
    return 2

def Process_10(b : bytes, i : int):
    print('loc_%08x    ' % i, end = '')
    print('%-10s' % b[i:i + 2].hex(), end = '')
    print('jmp loc_%08x' % (start_addr + b[i + 1]))
    return 2

def Process_11(b : bytes, i : int):
    print('loc_%08x    ' % i, end = '')
    print('%-10s' % b[i:i + 1].hex(), end = '')
    print('hlt')
    return 1

instruction_info = {
    2 : Process_2,
    6 : Process_6,
    7 : Process_7,
    9 : Process_9,
    10 : Process_10,
    11 : Process_11
}

def _rotl8(x, s):
    return ((x << s) | (x >> (8 - s))) & 0xff

encrypted_opcodes = bytes.fromhex('04 04 04 04 04 04 04 04  04 45 45 C4 C4 04 04 65'
                                  '44 E4 08 C4 04 E4 44 E4  25 E4 04 E4 25 44 44 E4'
                                  'C8 C4 24 E4 44 E4 44 E4  24 E4 25 44 44 E4 A6 C4'
                                  '44 E4 44 E4 C0 E4 44 E4  25 44 44 E4 E4 C4 64 E4'
                                  '44 E4 A1 E4 64 E4 25 44  44 E4 8D C4 84 E4 44 E4'
                                  '40 E4 84 E4 25 44 44 E4  68 C4 A4 E4 44 E4 E4 E4'
                                  'A4 E4 25 44 44 E4 0B C4  C4 E4 44 E4 06 E4 C4 E4'
                                  '25 44 44 04 24 65 04 04  04 04 04 04 04 04 04 04'
                                  '04 04 04 04 04 04 04 04  04 04 04 04 04 04 04 04'
                                  '04 04 04 04 04 04 04 04  04 04 04 04 04 04 04 04'
                                  '04 04 04 04 04 04 04 04  04 04 04 04 04 04 04 04'
                                  '04 04 04 04 04 04 04 04  04 04 04 04 04 04 04 04'
                                  '04 04 04 04 04 04 04 04')

# decrypt opcodes
opcodes = []
for i in range(200):
    opcodes.append(_rotl8(encrypted_opcodes[i], 3) ^ 0x20)
opcodes = bytes(opcodes)

ip = opcodes[9]
while ip < 200:
    try:
        length = instruction_info[opcodes[ip]](opcodes, ip)
        ip += length
    except:
        break

