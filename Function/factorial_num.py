def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
k=factorial(5)
print(k)