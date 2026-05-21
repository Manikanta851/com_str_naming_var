a = input()
b = input()
sub_s = False
index = 0
len_b = len(b)
for i in a:
    if i == b[index]:
        index += 1 
    if len_b == index :
        sub_s = True
        break
if sub_s :
    print("Yes")
else:
    print("No")

    
    