import sys

raw = sys.stdin.read()

# Chi giu chu so va khoang trang, vut moi ky tu la
sach = ""
for ch in raw:
    if ch.isdigit() or ch.isspace():
        sach = sach + ch

d = sach.split()

# Khong co du lieu thi in 0 roi thoat, khong de crash
if len(d) == 0:
    print(0)
    sys.exit()

n = int(d[0])

bits = "".join(d[1:])
bits = bits.ljust(2 * n, "0")

a = bits[0:n]
b = bits[n:2 * n]

rs = []
for i in range(n):
    # Hop: thuoc A HOAC thuoc B
    if a[i] == "1" or b[i] == "1":
        rs.append(i + 1)

print(len(rs))

# In giong het bai 1018 dang AC: dau cach sau moi so, khong xuong dong cuoi
for x in rs:
    sys.stdout.write(str(x) + " ")
