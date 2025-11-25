TARGET = [0x15, 0x5A, 0xAC, 0xF6, 0x36, 0x22, 0x3B, 0x52, 0x6C, 0x4F, 0x90, 0xD9, 0x35, 0x63, 0xF8, 0x0E, 0x02, 0x33, 0xB0, 0xF1, 0xB7, 0x69, 0x42, 0x67, 0x25, 0xEA, 0x96, 0x63, 0x1B, 0xA7, 0x03, 0x0B]
XOR_KEY = [0x7E, 0x33, 0x91, 0x4C, 0xA5]
ROTATION_PATTERN = [1, 3, 5, 7, 2, 4, 6]
MAGIC_SUB = 0x5D
position_squared = [(i*i) % 256 for i in range(32)]

for i in range(len(TARGET)):
    TARGET[i] ^= position_squared[i]

for i in range(0, len(TARGET), 5):
    TARGET[i:i+5] = reversed(TARGET[i:i+5])

for i in range(len(TARGET)):
    TARGET[i] = (TARGET[i] + MAGIC_SUB) % 256

for i in range(0, len(TARGET), 2):
    temp = TARGET[i]
    TARGET[i] = TARGET[i+1]
    TARGET[i+1] = temp

for i in range(len(TARGET)):
    n = ROTATION_PATTERN[i%7]
    TARGET[i] = (TARGET[i] >> n) | (TARGET[i] << (8 - n)) & 0xff

for i in range(len(TARGET)):
    TARGET[i] ^= XOR_KEY[i%5]

for i in range(len(TARGET)):
    print(chr(TARGET[i]),end="")

