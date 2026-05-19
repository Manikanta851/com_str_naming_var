a = int(input())
for i in range(a):
    l_s = ((a-i) * "* ")
    h_s = (i*2) * "  "
    print(l_s+h_s+l_s)
for i in range(1,a+1):
    l_s = i * "* " 
    h_s = ((a-i)*2) * "  "
    print(l_s+h_s+l_s)