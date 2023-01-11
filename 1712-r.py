A, B, C = map(int, input().split(" "))

def breakEvenPoint(a,b,c,n=1):
    outcome = a + b * n
    income = c * n
    if income > outcome:
        return n
    elif c <= b :
        return -1
    else:
        return breakEvenPoint(a,b,c, n+1)

print(breakEvenPoint(A,B,C))