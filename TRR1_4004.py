import sys

raw = sys.stdin.read()

sach = ""

for ch in raw:
    if ch.isdigit():
        sach = sach + ch
    else:
        sach = sach + " "

dl = sach.split()

so = []
for t in dl:
    so.append(int(t))

n = so[0]
c = []
for i in range(n):
    hang = []
    for j in range(n):
        hang.append(so[1 + i*n + j])
    c.append(hang)

VOCUNG = -10**18

d = []
for mask in range(2**n):
    d.append(VOCUNG)

d[0] = 0

vet = []
for mask in range(2**n):
    vet.append(-1)

for mask in range(2**n):
    dem = 0
    tam = mask
    for i in range(n):
        if tam % 2 == 1:
            dem = dem + 1
        tam = tam // 2
    for j in range(n):
        if (mask // (2**j)) % 2 == 0:
            moi = mask + 2 ** j
            chiphi = d[mask] + c[dem][j]
            if chiphi > d[moi]:
                d[moi] = chiphi
                vet[moi] = j

nguoc = []
mask = 2 ** n - 1
for t in range(n):
    j = vet[mask]
    nguoc.append(j + 1)
    mask = mask - 2**j

nguoc.reverse()

print(d[2 ** n - 1])

dong = ""
for t in nguoc:
    dong = dong + str(t) + " "
print(dong)
