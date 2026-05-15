a = input()
b = a.split()
small = b[0]
big = b[0]
for i in b[1:] :
    if i.lower() < small.lower() :
        small = i
    if i.lower() > big.lower() :
        big = i
print(small+ " " +big)
        

    
    
