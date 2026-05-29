def rem_dup(li):
    temp = []
    for i in li:
        if i not in temp:
            temp.append(i)
    return temp
k = rem_dup([1,1,2,2,3,3,4,4])
print(k)
