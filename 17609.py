t = int(input())
strs = [input() for _ in range(t)]

for s in strs:
    data, dl = s, len(s)

    c1 = True
    c2 = True
    c3 = True

    for i in range(dl//2):
        if data[i] != data[-1-i]:
            c1 = False
            break

    if not c1:
        lc = rc = 0
        for i in range(dl//2):
            if data[i+lc] != data[-1-i]:
                if lc != 0:
                    c2 = False
                    break
                if data[i+1] == data[-1-i]:
                    lc += 1
                else:
                    c2 = False
                    break
        for i in range(dl//2):
            if data[i] != data[-1-i-rc]:
                if rc != 0:
                    c3 = False
                    break
                if data[i] == data[-2-i]:
                    rc += 1
                else:
                    c3 = False
                    break

    
    if c1:
        print(0)
    elif c2 or c3:
        print(1)
    else:
        print(2)