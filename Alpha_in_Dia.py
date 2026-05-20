a = int(input())
alpha = 65
container = []
for i in range(1,a+1):
    l_space = (a-i) * " "
    hollow_space = (((i-1)*2)-1) * " "
    if i == 1 :
        container.append(l_space+chr(alpha))
        alpha += 1 
    else :
        container.append(l_space+chr(alpha)+hollow_space+chr(alpha+1))
        alpha += 2 
for i in container:
    print(i)
for i in reversed(container[:-1]):
    print(i)

      
        