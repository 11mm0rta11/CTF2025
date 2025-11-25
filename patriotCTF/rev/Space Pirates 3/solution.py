target = [0x60, 0x6D, 0x5D, 0x97, 0x2C, 0x04, 0xAF, 0x7C, 0xE2, 0x9E, 0x77, 0x85, 0xD1, 0x0F, 0x1D, 0x17, 0xD4, 0x30, 0xB7, 0x48, 0xDC, 0x48, 0x36, 0xC1, 0xCA, 0x28, 0xE1, 0x37, 0x58, 0x0F,]
xor_key = [0xC7, 0x2E, 0x89, 0x51, 0xB4, 0x6D, 0x1F]
rotationPattern = [7, 5, 3, 1, 6, 4, 2, 0]
magicSub = 0x93
chunkSize = 6
positionValue = [((i * i) + i) % 256 for i in range(len(target))]

for i in range(len(target)):
    target[i] ^= positionValue[i]

for i in range(0, len(target), 6):
    target[i:i+6] = reversed(target[i:i+6])

for i in range(len(target)):
    target[i] = (target[i] + magicSub) % 256

for i in range(0, len(target), 2):
    temp = target[i]
    target[i] = target[i+1]
    target[i+1] = temp

for i in range(len(target)):
    n = rotationPattern[i%8]
    target[i] = target[i] >> n | (target[i] << (8 - n) & 0xff)

for i in range(len(target)):
    target[i] ^= xor_key[i%7]

for i in range(len(target)):
    print(chr(target[i]),end="")
