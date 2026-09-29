a, b = input().split()
a = float(a)
b = float(b)

if a == 0:
    if b == 0:
        # 0x + 0 = 0: moi so thuc x deu la nghiem, nen co nghiem am
        print(1)
    else:
        # 0x + b = 0 voi b khac 0: vo nghiem
        print(0)
else:
    # Phuong trinh co 1 nghiem duy nhat x = -b / a
    x = -b / a
    if x < 0:
        print(1)
    else:
        print(0)
