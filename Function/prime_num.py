def prime(n, count=0):
    for i in range(2, (n//2)+1):
        if n % i == 0:
            count += 1
            break

    if count == 0:
        return "Prime number"
    else:
        return "Not a prime number"

k = prime(9)
print(k)