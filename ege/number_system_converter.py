def convert(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result

def f(n):
    new_n = convert(n, 2)
    s = 0
    if n % 3==0:
        new_n += new_n[-3:]
    else:
        new_n += convert(((n%3)*3),2)
    return int(new_n, 2)


for i in range(1, 10000):
    if int(f(i)) >99:
        print(i)
        break