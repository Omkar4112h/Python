li=[1,12,4,5,7,8,9]
max = li[0]
second_max = li[0]
for i in range(1,len(li)):
    if max < li[i]:
        second_max = max
        max = li[i]
    elif second_max < li[i] and max != li[i]:
        second_max = li[i]
print("second largest number is ",second_max)
