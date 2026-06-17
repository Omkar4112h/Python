# Reverse the characters in a string without using built-in functions.
def rev_char(st,temp=""):
    for i in st:
        if i != " ":
            temp = i+temp
        else:
            print(temp,end=" ")
            temp = ""
    return temp
k = rev_char("Hello World")
print(k)

# reverse the string without reversing the words
def rev_str(st,temp=""):
    for i in st:
        temp = i+temp
    return temp
k = rev_str("Hello World")
print(k)
# _________________________________________________________
a = "Hello World"
print(a[::-1])
        



 
        