n = int(input())

phi = list(range(n + 2))

for i in range(2, n + 1):
    if phi[i] == i:
        for j in range(i, n + 1, i):
            phi[j] -= phi[j] // i

t = 1
for b in range(1, n + 1):
    t += phi[b]

print(t)