import sys
import math

raw = sys.stdin.read()

sach = ""

for ch in raw:
    if ch.isdigit() or ch.isspace():
        sach += ch

dl = sach.split()
n = int(dl[0])
s = int(dl[1])

print(math.comb(n, s))