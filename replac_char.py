a = input()
c = ""
for i in a :
    if i == " " :
        c += i
    else:   
        b = (ord(i) + 1) 
        c += chr(b)
print(c)