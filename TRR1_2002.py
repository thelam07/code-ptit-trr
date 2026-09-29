import sys

raw = sys.stdin.read()

sach = ""
for ch in raw:
    if ch.isdigit() or ch.isspace():
        sach = sach + ch

d = sach.split()

a = int(d[0])
b = int(d[1])
k = int(d[2])
m = int(d[3])

dem = 0
for x in range(a, b + 1):
    if x % k == 0 or x % m == 0:
        dem += 1

print(dem)
