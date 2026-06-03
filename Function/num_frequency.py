def num_frequency(li):
    dict = {}
    for i in li:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
    return dict

k = num_frequency([1,2,4,2,1,1,1])
print(k)