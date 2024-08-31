n = int(input())

result = n // 5
remain  = n % 5

if n < 5:
    if n % 3 == 0:
        print(1)
    else:
        print(-1)
else:
    pre = n % 3 == 0
    if remain == 0:
        print(result)
    else:
        for i in range(result + 1):
            if remain % 3 == 0:
                rep = result - i + remain // 3
                if rep < n // 3:
                    print(rep)
                else:
                    print(n // 3)
                break
            remain += 5
            if remain == n:
                if pre:
                    print(n // 3)
                    break
                else:
                    print(-1)
                    break