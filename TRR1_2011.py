import sys

raw = sys.stdin.read()

sach = ""

for ch in raw:
    if ch.isdigit() or ch.isspace():
        sach += ch

dl = sach.split()
n = int(dl[0])
k = int(dl[1])

d = [0] * (n+1)

for i in range(0, k):
    if i <= n:
        d[i] = 2**i

for i in range(k, n + 1):
    tong = 0
    for j in range(1, k + 1):
        tong = tong + d[i - j]
    d[i] = tong

print(d[n])