s1 = "CACI"
s3 = "PatriotCTF"

for i in range(0, 0x2710):
    a = (i + 0x16) % 0x6ca
    b = 6 * ((i + i) % 0x7d0) + 9
    if a == b:
        print(f"flag = {s1}-{i}-{s3}")