def solve(n, x):
    if x / 26 > n or n > x:
        print("!")
        return
    
    points = [1]*n
    rem = x-n

    for i in range(r:=rem//25):
        points[-(i+1)] = 26
        rem -= 25

    if rem != 0:
        points[-(r+1)] = rem+1

    
    print("".join(map(lambda x: chr(x+64), points)))


N, X = map(int, input().split())
solve(N, X)