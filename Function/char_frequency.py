def word_freq(li):
    for word in li:
        count = 0
        for ch in word:
            count+=1
        print(word,":",count)
k = word_freq(["Hello","hi"])
print(k)

