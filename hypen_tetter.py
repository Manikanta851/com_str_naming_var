a = input()
container = ""
b = a[0]
for i in range(1,len(a)):
    container += "-" + a[i]
print(b+container)