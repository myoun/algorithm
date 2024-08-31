g, l = map(int, input().split())

def gcd(a, b):
    tmp = 0
    while b:
        tmp = a % b
        a = b
        b = tmp
    return a

t = g*l

i = 1
a = b = float('inf')
for i in range(1, t+1):
    if i*i > t:
        break
    if t % i == 0 and i+t//i < a+b and gcd(i, t//i) == g:
        a = i
        b = t // i
print(a,b)
