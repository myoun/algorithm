T = int(input())
li = [-1] * 101

def padoban(n: int) -> int:
    if n <= 3:
        return 1
    if n <= 5:
        return 2
    if li[n] != -1:
        return li[n]
    li[n] = padoban(n-1) + padoban(n-5)
    return li[n] 

for i in range(T):
    n = int(input())
    print(padoban(n))