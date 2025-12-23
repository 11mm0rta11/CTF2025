from pathlib import Path

start = 0x060ea0
end = 0x061870
b1 = b"\x00\x00\x00\x00"
b2 = b"\x00\x00\x80\x3f"

p1 = Path(r"D:\CTF2025\0CTF\rev\Perspective\perspective.exe")
p2 = Path(r"D:\CTF2025\0CTF\rev\Perspective\perspective_patched.exe")
data = bytearray(p1.read_bytes())

for i in range(start, end, 4):
    tmp = data[i:i+4]
    if tmp == b1:
        data[i:i + 4] = b2
    if tmp == b2:
        data[i:i + 4] = b1

p2.write_bytes(data)