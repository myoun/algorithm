exp = input()

exps = []
current = ''

for c in exp:
    if c in ['+', '-']:
        exps.append(int(current))
        exps.append(c)
        current = ''
    else:
        current += c
else:
    exps.append(int(current))

r = False

num = 0
oper = '+'

for e in exps:
    if e == '-' and not r:
        r = True
    
    if e in ['+', '-']:
        if r:
            oper = '-'
        continue
    
    if oper == '+':
        num += e
    else:
        num -= e

print(num)