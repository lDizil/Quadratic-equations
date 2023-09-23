a = int(input())
b = int(input())
c = int(input())
D = b*b - 4*a*c
if D < 0:
    print("Корней нет")
else:
    x1 = int((-b+D**0.5)/2*a)
    x2 = int((-b-D**0.5)/2*a)
    if D == 0:
        print("x1 = x2 =", x1)
    else:
        print("x1 =", x1, "x2 =", x2)

