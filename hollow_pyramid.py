a = int(input())
for i in range(1,a+1):
    hollow_space = (i - 2) * " "
    if i == 1 :
        pattern = "| "
        print(pattern)
    if i > 1 :
        pattern = "| " + hollow_space + "\ " 
        print(pattern)
for i in range(1,a):
    hollow_space = (a-i-1) * " "
    pattern = "| " + hollow_space + "/"
    print(pattern)
if a > 1 :
    print("|")
        