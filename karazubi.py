def karatsuba(a, b):
    # Базовий випадок: якщо числа малі, використовуємо стандартне множення
    if a < 10 or b < 10:
        return a * b

    # Визначаємо розмір чисел
    n = max(len(str(a)), len(str(b)))
    m = n // 2

    # Розбиваємо числа на частини: A = A1 * 10^m + A0
    # A1 — старша частина, A0 — молодша
    a1, a0 = divmod(a, 10**m)
    b1, b0 = divmod(b, 10**m)

    c2 = karatsuba(a1, b1)            # A1 * B1
    c0 = karatsuba(a0, b0)            # A0 * B0
    
    c1 = karatsuba(a1 + a0, b1 + b0) - c2 - c0

    return c2 * (10**(2 * m)) + c1 * (10**m) + c0

# Приклад використання:
x = 12345678901234567890
y = 98765432109876543210

result = karatsuba(x, y)
print(f"Результат Карацуби: {result}")
print(f"Перевірка (x * y):  {x * y}")