file = open("26.txt")
n, m = file.readline().split()
a = 0
b = {}
for i in file:
    if "A" in i:
        a += int(i[0]) * int(i[1])
    else:
      b[int(i[0])] = int(i[1])
m = int(m)
m -= a
counter = 0
for key in b:
    sum = key * b[key]
    if sum > m:
        for i in range(1, key):
            if i * b[key] > m:
                counter += i -1
                m -= (i-1) * b[key]
    else:
        m -= key * b[key]
        counter += key

print(m, counter)