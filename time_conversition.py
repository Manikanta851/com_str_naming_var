a = input()
if a[-1] == "M" :
    b = int(a[:(len(a)-1)])
    m = b/60
    H = round(m,2)
    print(str(H) + "H")
if a[-1] == "S" :
    b = int(a[:(len(a)-1)])
    m = b/3600
    H = round(m,2)
    print(str(H) + "H")
    
    