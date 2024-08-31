li = [1,-4,3,2,-7]
    

found = 0
for i in range(0, len(li)-1):
    biggest = (0, float('-inf'))
    for i2 in range(0, len(li)-found):
        if li[i2] > biggest[1]:
            biggest = (i2, li[i2])
    li[biggest[0]], li[len(li)-1-found] = li[len(li)-1-found], li[biggest[0]]
    found += 1

print(li)