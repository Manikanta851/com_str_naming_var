a = int(input())
for i in range(1,a+1):
    l_s = (a-i) * " "
    hollow = ((i*2) - 2) * " "
    print(l_s + "/" + hollow + "\\")
for i in range(1,a+1):
    l_s = (i-1) * " "
    hollow = (2*(a-i)) * " "
    print(l_s + "\\" + hollow + "/")
    