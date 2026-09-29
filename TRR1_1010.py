import math

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

if a == 0:
    if b == 0:
        if c == 0:
            print(1)
        else:
            print(0)
    else:
        x = -c / b
        if x > 0:
            print(1)
        else:
            print(0)
else:
    delta = b * b - 4 * a * c
    if delta < 0:
        print(0)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        if x1 > 0 or x2 > 0:
            print(1)
        else:
            print(0)
