DecodeTable = b'\x10\x20\x30'
Serial = bytes.fromhex('5B134977135E7D13')

def DecodeSerial(_bytes : bytes):
    ret = []
    for i in range(len(_bytes)):
        ret.append(_bytes[i] ^ DecodeTable[i % 3])
    return bytes(ret)

print(DecodeSerial(Serial).decode())
