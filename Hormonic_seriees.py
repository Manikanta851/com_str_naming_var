a = int(input())
b = 0
for i in range(2,a+1) :
    b += 1/i 
b = float(b+1)
print(round(b,2))