for x in range(0, 10000):
    B = 17 <= x <= 31
    C = 17 <= x <= 37
    A = 0
    f = C <= (B or A)
    if f != 1:
        print(x, end=" ")
print()
