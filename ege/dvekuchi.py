def f(a, b, m):
    if a + b >= 342:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a + 2, b, m - 1), f(a, b + 2, m - 1), f(a * 5, b, m - 1), f(a, b * 5, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)
    # для 19 задания если в формк=улировке звучит "после неудачного хода" any в обоих случаях


print('19', [s for s in range(1, 325) if f(11, s, 2)])
print('19', [s for s in range(1, 325) if not f(11, s, 1) and f(11, s, 3)])
print('19', [s for s in range(1, 325) if not f(11, s, 2) and f(11, s, 4)])
