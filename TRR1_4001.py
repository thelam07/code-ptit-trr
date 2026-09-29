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
b = so[1]

a = []
c = []
for i in range(n):
    a.append(so[2 + 2*i])
    c.append(so[3 + 2*i])

h = n //2

def liet_ke(dau, cuoi):
    ta = [0]
    tc = [0]
    for i in range(dau, cuoi):
        them_a = []
        them_c = []
        for j in range(len(ta)):
            them_a.append(ta[j] + a[i])
            them_c.append(tc[j] + c[i])
        ta = ta + them_a
        tc = tc + them_c
    return ta, tc

ta1, tc1 = liet_ke(0, h)
ta2, tc2 = liet_ke(h, n)

nua_2 = []
for k in range(len(ta2)):
    nua_2.append([ta2[k], tc2[k], k])
nua_2.sort()

tot_v = []
tot_m = []
cao = -1
caom = 0

for k in range(len(nua_2)):
    if nua_2[k][1] > cao:
        cao = nua_2[k][1]
        caom = nua_2[k][2]
    tot_v.append(cao)
    tot_m.append(caom)

nua_1 = []
for k in range(len(ta1)):
    nua_1.append([ta1[k], tc1[k], k])
nua_1.sort()

best = -1
bestm = 0
j = len(nua_2) - 1

for k in range(len(nua_1)):
    w1 = nua_1[k][0]
    if w1 > b:
        break
    con = b - w1
    while j >= 0 and nua_2[j][0] > con:
        j = j - 1
    if j < 0:
        break
    tong = nua_1[k][1] + tot_v[j]
    if tong > best:
        best = tong
        bestm = nua_1[k][2] + tot_m[j] * (2 ** h)

kq = []
x = bestm
for i in range(n):
    kq.append(x % 2)
    x = x // 2

print(best)

dong = ""
for t in kq:
    dong = dong + str(t) + " "
print(dong)