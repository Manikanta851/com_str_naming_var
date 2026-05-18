X = float(input())
N = int(input())
sum = 0
for i in range(1,N+1):
    sum += X ** i 
m = round(sum,4)
print(m)