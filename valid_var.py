a = input()
b = True 
for i in a:
    if not (i == "_" or i.isupper() or i.islower()): 
        b = False
print(b)