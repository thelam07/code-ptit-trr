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
a = so[1:1 + n]

i = n - 2
while i >= 0 and a[i] < a[i + 1]:
    i = i - 1

if i < 0:
    print(0)
else:
    j = n - 1
    while a[j] > a[i]:
        j = j - 1

    tam = a[i]
    a[i] = a[j]
    a[j] = tam

    duoi = a[i + 1:]
    duoi.sort()
    duoi.reverse()
    a = a[0:i + 1] + duoi

    dong = ""
    for x in a:
        dong = dong + str(x) + " "
    print(dong)
