def count_char(str,temp="",count=0):
    if str == "":
        return count
    temp = str[0]
    count+=1
    return count_char(str[1::],count=count,temp=temp)
    
k=count_char("Omkar")
print(k)
