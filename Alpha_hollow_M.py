a = int(input())
A = 65
for i in range(1,a+1):
    l_s = (a-i) * " "
    hollow = ((2*i-1)-2) * " "
    m_s = (((a-i) * 2 ) * " ") + " "
    if i == 1:
        print(l_s+chr(A)+m_s+chr(A))
        A += 1
    else:
        print(l_s+chr(A)+hollow+chr(A)+m_s+chr(A)+hollow+chr(A))
        A +=1