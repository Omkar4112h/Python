li=[1,12,4,5,7,8,9]
max = li[0]
for i in range(1,len(li)):
    if max < li[i]:
        max = li[i]
print("largest number is ",max)
