N = int(input())
M = int(input())

if M > 0:
    buttons = input().split()
else:
    buttons = []

if len(buttons) == 10:
    print(abs(N-100))
    exit()

u = N
d = N

break_u = False
break_d = False

while True:
    pass_u = False
    pass_d = False


    for b in buttons:
        if b in str(u) and not pass_u and not break_u:
            u += 1
            pass_u = True
        if b in str(d) and not pass_d and not break_d:
            d -= 1
            pass_d = True
        
        if pass_u and pass_d:
            break

    pb_u = False
    pb_d = False

    for b in buttons:
        if b in str(u):
            pb_u = True
            break
    
    for b in buttons:
        if b in str(d):
            pb_d = True
            break    
    
    if not pb_u:
        break_u = True
    if not pb_d:
        break_d = True
    
    
    if break_u and (abs(N-u) <= abs(N-d)):
        if not break_d:
            d = 999999
        break

    if break_d and (abs(N-d) < abs(N-u)):
        if not break_u:
            u = 999999
        break



if abs(N-d)+len(str(d)) < abs(N-u)+len(str(u)):
    best = d
else:
    best = u

length = len(str(best))
distance = abs(N-best)

a = length+distance
b = abs(N-100)

if a <= b:
    print(a)
else:
    print(b)