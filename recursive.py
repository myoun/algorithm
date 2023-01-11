# 재귀 함수

# def count_down(n):
#     if n == 0:
#         return
#     print(n)
#     count_down(n-1)

# count_down(5)

def pibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return pibo(n-1)+pibo(n-2)

print(pibo(7))