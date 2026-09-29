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
        t = - c / b
        if t >= 0:
            print(1)
        else:
            print(0)
else:
    delta = b*b - 4*a*c
    if delta < 0:
        print(0)
    else:
        t1 = (-b + math.sqrt(delta)) / (2 * a)
        t2 = (-b - math.sqrt(delta)) / (2 * a)
        if t1 >= 0 or t2 >= 0:
            print(1)
        else:
            print(0)