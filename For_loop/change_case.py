# Change the case of a string
st = "Hello"
temp = ""
for i in st:
      if "A"<=i<="Z":
            i = ord(i)
            ind = i+32
            res = chr(ind)
            temp+=res
      elif "a"<=i<="z":
            i = ord(i)
            ind = i-32
            res = chr(ind)
            temp+=res
print(temp)