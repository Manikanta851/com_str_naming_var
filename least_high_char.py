a = input()
least = a[0]
highest = a[0]
for i in a :
    if i < least:
        least = i
    if i > highest:
        highest = i
m = (least + " " + highest)
print(m)