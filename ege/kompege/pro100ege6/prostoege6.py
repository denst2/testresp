# 2
# print("x y z w F")
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 F = (x or y) and not(y == z) and not(w)
#                 if F:
#                     print(x, y, z, w, F)


# #5
# def F(n):
#     new_n = bin(n)[2:]
#     s = 0
#     for i in range(0, len(new_n)):
#         s += int(new_n[i])
#     if s % 2 == 0:
#         new_n = "10" + new_n[2:] + "0"
#     else:
#         new_n = "11" + new_n[2:] + "1"
#     return int(new_n, 2)
#
#
# for i in range(0, 10**6):
#     if F(i) < 35:
#         print(i)

# # 8
# import itertools
#
# alph = "АИНПТЦЯ"
#
# words = itertools.product(alph, repeat=6)
#
# count = 0
# c = 1
# for el in words:
#     if c % 2 == 0 and el[0] != "Н" and el.count('Я') == 2:
#         count += 1
#     c += 1
#
# print(count)


# #9
# data = [int(a) for a in open('9.txt').read().split()]


# def stolb_c(el, ind, dat):
#     c = 0
#     while ind < len(dat):
#         if dat[ind] == el:
#             c += 1
#         ind += 5
#     return c
#
#
# ccc = 1
# for i in range(0, len(data), 5):
#     stroka = data[i:i+5]
#     if stroka[2] % 2 == 0 and stroka[3] % 2 == 0 and stroka[4] % 2 == 0:
#         ind = 0
#         for el in stroka:
#             cinstr = stroka.count(el)
#             if cinstr == stolb_c(el, ind, data):
#                 print(stroka, ccc)
#             ind += 1
#     ccc += 1


# #12
# n = 4
# while True:
#     stroka = "3" + "5" * n
#     while "25" in stroka or "355" in stroka or "555" in stroka:
#         if "25" in stroka:
#             stroka = stroka.replace("25", "5", 1)
#         if "355" in stroka:
#             stroka = stroka.replace("355", "52", 1)
#         if "555" in stroka:
#             stroka = stroka.replace("555", "3", 1)
#     if "3" not in stroka and "2" not in stroka:
#         print(n)
#         break
#     n += 1


# #13
# print(bin(192)[2:].zfill(8), bin(168)[2:].zfill(8), bin(32)[2:].zfill(8), bin(48)[2:].zfill(8))
# print()
# print(bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(240)[2:].zfill(8))
#
# c = 0
# for i in range(0, 16):
#     if (bin(i)[2:].zfill(4).count("1") + 8)%2 == 1:
#         c += 1
#
# print(c)


# #14
# for x in range(0, 22):
#     n = int("98079641", 22) + int("36014", 22) + int("7304",22) + x*22 + x*22**2 + x*22**5
#     if n % 21 == 0:
#         print(x, n/21)


# #15
# for A in range(0, 1000):
#     flag = True
#     for x in range(0, 1000):
#         for y in range(0, 1000):
#             f = (99 != y + 2*x) or (A < x) or (A < y)
#             if not f:
#                 flag = False
#                 break
#         if flag is False:
#             break
#     if flag:
#         print(A)


# #16
# def F(n):
#     if n >= 2025:
#         return n
#     return n + F(n+2)
#
# print(F(2022) - F(2023))


# #17
# data = [int(a) for a in open("17.txt").read().split()]
#
# maxx = None
# for a in data:
#     if abs(a) % 1000 == 221:
#         if maxx is None or a > maxx:
#             maxx = a
#
#
# answ = 0
# minss = None
# for i in range(0, len(data)-2):
#     troyka = data[i:i+3]
#     c = 0
#     for el in troyka:
#         if abs(el) > 9 and abs(el) % 100 // 10 % 2 == 1:
#             c += 1
#     if c == 2:
#         c2 = 0
#         for el in troyka:
#             if 100 > abs(el) > 9:
#                 c2 += 1
#         if c2 <= 2:
#             ss = troyka[0] + troyka[1] + troyka[2]
#             if ss > maxx:
#                 answ += 1
#                 if minss is None or ss < minss:
#                     minss = ss
#
# print(answ, minss)


# # 19 20 21
# def f(a, b, m):
#     if a + b >= 231:
#         return m % 2 == 0
#     if m == 0:
#         return 0
#     h = [f(a + 1, b, m - 1), f(a, b + 1, m - 1), f(a * 2, b, m - 1), f(a, b * 2, m - 1)]
#     return any(h) if (m - 1) % 2 == 0 else all(h)
#
#
# print('19', [s for s in range(1, 214) if f(s, 17, 2)])
# print('20', [s for s in range(1, 214) if not f(17, s, 1) and f(17, s, 3)])
# print('21', [s for s in range(1, 214) if not f(17, s, 2) and f(17, s, 4)])


# #23
# def f(start, end):
#     if start > end or start == 12:
#         return 0
#     if start == end:
#         return 1
#     return f(start+1, end) + f(start+2, end) + f(start*2, end)
#
# print(f(2, 9)*f(9, 17))


# #24
# data = open('24.txt').read()
# data = data.replace("XZZY", "1")
# data = data.split("1")
# maxl = None
# for el in data:
#     if maxl is None or len(el) > maxl:
#         maxl = len(el)
# print(maxl)


# # 25
# def dells(a):
#     divs = [1, a]
#     for k in range(2, int(a ** 0.5) + 1):
#         if a % k == 0:
#             divs.append(k)
#             if k != a // k:
#                 divs.append(a // k)
#         if len(divs) > 5:
#             return []
#     return divs
#
#
# for x in range(123456, 987655):
#     d = dells(x)
#     if len(d) == 5:
#         d.sort()
#         print(d)


#26
data = [int(a) for a in open('26_13744.txt').read().split()]
S, N = data[0], data[1]
data = data[2:]
data.sort()
c = 0
m = 0
last = None
print(N, S)
while True:
    m += data[c]
    if m > S:
        m -= data[c]
        last = data[c-1]
        break
    c += 1

print(c, m, last)
maxx = None
al = set(data)
for el in al:
    if m - last + el <= S:
        maxx = el

print(maxx)


# #27
# data = [int(a) for a in open('27-B_13745.txt').read().split()]
#
#
# c = 0
# ch = data[0]
# maxw = data[1]
# data = data[2:]
# data.sort()
# l = 0
# r = ch - 1
# while l <= r:
#     if data[l] + data[r] <= maxw:
#         l += 1
#     c += 1
#     r -= 1
# print(c)