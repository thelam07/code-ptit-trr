n = int(input())
tong = 0
t = 0
s = 1
while True:
    tong = tong + s*s
    if tong > n:
        break
    t += 1
    s += 1
print(t)