n = int(input())
c = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    row = input().split()
    for j in range(1, n + 1):
        c[i][j] = int(row[j - 1])

INF = 10 ** 18
best = INF
sols = []

x = [0] * (n + 1)
x[1] = 1
used = [False] * (n + 1)
used[1] = True


def Try(k, cost):
    global best
    if cost > best:               
        return
    if k > n:
        total = cost + c[x[n]][1]   
        if total < best:
            best = total
            sols.clear()
            sols.append(x[1:n + 1])
        elif total == best:
            sols.append(x[1:n + 1])
        return
    for j in range(2, n + 1):
        if not used[j]:
            used[j] = True
            x[k] = j
            Try(k + 1, cost + c[x[k - 1]][j])
            used[j] = False

Try(2, 0)

if len(sols) == 1:
    print(best)
    print(' '.join(str(v) for v in sols[0]))
else:
    print(best, len(sols))
    for s in sols:
        print(' '.join(str(v) for v in s))