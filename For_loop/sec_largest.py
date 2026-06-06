li = [1,12,4,5,7,8,9]

largest = li[0]
second = li[0]

for num in li:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Largest =", largest)
print("Second Largest =", second)
