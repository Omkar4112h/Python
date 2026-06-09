def add_digit(n, pro=1):
    if n == 0:
        return pro

    digit = n % 10
    pro*= digit
    return add_digit(n // 10, pro)

k = add_digit(42)
print(k)



