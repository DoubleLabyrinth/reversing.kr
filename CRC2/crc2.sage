#!/usr/bin/env sage

def PrintAsBytes(x):
    data = []
    for i in range(13):
        tmp = 0
        for j in range(7):
            tmp += int(x[i * 7 + j, 0]) * (1 << j)
        data.append(tmp)
    print('{ %s }' % ', '.join([ '0x%02x' % data[i] for i in range(13) ])) 

def PrintVectorAsBytes(x):
    data = []
    for i in range(13):
        tmp = 0
        for j in range(7):
            tmp += int(x[i * 7 + j]) * (1 << j)
        data.append(tmp)
    print('{ %s }' % ', '.join([ '0x%02x' % data[i] for i in range(13) ])) 

TargetCRC = 0xd0e7f3cbd0a9de5d

CRCsOfMasks = [
    0x576ed74885b8495c,
    0xaeddae910b7092b8,
    0x4489a78832679433,
    0x89134f1064cf2866,
    0x0b14648aed18e18f,
    0x1628c915da31c31e,
    0x2c51922bb463863c,
    0x7d947a7349d0d60b,
    0xfb28f4e693a1ac16,
    0xef63136703c5e96f,
    0xc7f4dc64230d639d,
    0x96db4262629c7679,
    0x34847e6ee1be5db1,
    0x6908fcddc37cbb62,
    0xf64d7252b5dc4f4b,
    0xf5a81e0f4f3e2fd5,
    0xf262c6b4bafaeee9,
    0xfdf777c351736c91,
    0xe2dc152c86606861,
    0xdc8ad0f328466181,
    0xa0275b4c740a7241,
    0x24d1d95d771bb31c,
    0x49a3b2baee376638,
    0x93476575dc6ecc70,
    0x3fbc30419c5b29a3,
    0x7f78608338b65346,
    0xfef0c106716ca68c,
    0xe4d378a6c65ffc5b,
    0x040dcef923321aef,
    0x081b9df2466435de,
    0x10373be48cc86bbc,
    0x206e77c91990d778,
    0x40dcef923321aef0,
    0x81b9df2466435de0,
    0x1a4144e2e8000a83,
    0x8afc34191d43c7c0,
    0x0cca92981e013ec3,
    0x199525303c027d86,
    0x332a4a607804fb0c,
    0x665494c0f009f618,
    0xcca92981e013ec30,
    0x8060a9a9e4a16923,
    0xc798e9fea578800e,
    0x960329576e77b15f,
    0x3534a804f869d3fd,
    0x6a695009f0d3a7fa,
    0xd4d2a013e1a74ff4,
    0xb097ba8de7c82eab,
    0x781d8fb1eb16ec15,
    0x9f8d51f9a634d73a,
    0x2628595968ef1f37,
    0x4c50b2b2d1de3e6e,
    0x98a16565a3bc7cdc,
    0x2870306163fe48fb,
    0x50e060c2c7fc91f6,
    0xa1c0c1858ff923ec,
    0x678e70440038ac72,
    0xcf1ce088007158e4,
    0x870b3bba2464008b,
    0x17248dde6c4eb055,
    0x2e491bbcd89d60aa,
    0x5c923779b13ac154,
    0xb9246ef3627582a8,
    0x92ab14a7c1dfd471,
    0x3c64d3e5a73919a1,
    0x78c9a7cb4e723342,
    0xf1934f969ce46684,
    0xfa1465871d4e7c4b,
    0xed1a31a41e1a49d5,
    0xc30699e218b222e9,
    0xd8f2ecf493bb8a0f,
    0xa8d7234303f1a55d,
    0x489cbc2c2365fbf9,
    0x9139785846cbf7f2,
    0x3b400a1aa9115ea7,
    0x768014355222bd4e,
    0xed00286aa4457a9c,
    0x436b127e8407a6fd,
    0x86d624fd080f4dfa,
    0x149eb35034982ab7,
    0x293d66a06930556e,
    0x527acd40d260aadc,
    0xa4f59a81a4c155b8,
    0x50d9cfa96d041a33,
    0xec1dd0656720bb52,
    0xc1095a60eac7c7e7,
    0x9b204e6bf1093e8d,
    0x2f72667dc694cc59,
    0x5ee4ccfb8d2998b2,
    0xbdc999f71a533164,
    0x62a1c9441020d38b
]

A = MatrixSpace(GF(2), 64, 13 * 7)()
B = MatrixSpace(GF(2), 64, 1)()

for i in range(64):
    for j in range(13 * 7):
        A[i, j] = 1 if (CRCsOfMasks[j] & (1 << i)) != 0 else 0

for j in range(64):
    B[j, 0] = 1 if (TargetCRC & (1 << j)) != 0 else 0

print('-----Particular Solution-----')
X = A.solve_right(B)
PrintAsBytes(X)
print('-----Genernal Solution-----')
for base in A.right_kernel().basis():
    PrintVectorAsBytes(base)

