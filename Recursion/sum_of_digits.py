def add_digit(n, sum=0):
    if n == 0:
        return sum

    digit = n % 10
    sum += digit
    return add_digit(n // 10, sum)

p = add_digit(1234)
print(p)