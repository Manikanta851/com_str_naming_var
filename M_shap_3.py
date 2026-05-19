a = int(input())
for i in range(1,a+1) :
    l_s = (a-i) * ". "
    zeros = (2*i-1) * "0 "
    m_dot = ((a-i) * 2) * ". "
    print(l_s+zeros+m_dot+zeros+l_s)
    