# Find the Target element in the given list using linear search
li = [5,2,4,8,3,9,3]
targ = 3
value = False
for i in li:
    if i == targ:
        value = True
if value:
    print("The target element is present in the list")
else:
    print("The target element is not present in the list")