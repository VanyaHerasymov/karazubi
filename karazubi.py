def karatsuba(a, b):
    if a < 10 or b < 10:
        return a * b

    n = max(len(str(a)), len(str(b)))
    m = n // 2

    a1, a0 = divmod(a, 10**m)
    b1, b0 = divmod(b, 10**m)

    c2 = karatsuba(a1, b1)            
    c0 = karatsuba(a0, b0)            
    
    c1 = karatsuba(a1 + a0, b1 + b0) - c2 - c0

    return c2 * (10**(2 * m)) + c1 * (10**m) + c0

x = 12345678901234567890
y = 98765432109876543210

result = karatsuba(x, y)
print(f"Результат Карацуби: {result}")
print(f"Перевірка (x * y):  {x * y}")
