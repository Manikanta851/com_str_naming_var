a = input()
b = a.split()
start_word = b[0]
for i in b[1:] :
    if i.lower() < start_word.lower() :
        start_word = i
print(start_word)
