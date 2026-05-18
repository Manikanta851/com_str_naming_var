N = int(input())
S = float(input())
sum = 0
for i in range(N):
    M = float(input())
    sum += M 
b = round(sum,3)
print(S == b)