# Given a string, count the frequency of each character in the string and return a dictionary with the characters as keys and their frequencies as values.
st = "aaabbbbccc"
temp = {}
for i in st:
    if i not in temp:
        temp[i]=1
    else:
        temp[i]+=1
print(temp)