import sys

sys.setrecursionlimit(10000000)

s = input()
atts = []

dp = {}
a = 0
b = 0
def solve(st: str, att):
    global a, b, atts
    a += 1
    if st in dp.keys():
        b += 1
        return dp[st]
    if "A" not in st and "B" not in st:
        return 1

    ml = []

    for i in range(len(st)):
        for n in range(i+1, len(st)):
            if (st[i] == "A" and st[n] == "B") or (st[i] == "B" and st[n] == "C"):
                strl = list(st)
                del strl[i]
                del strl[n-1]
                atts.append(att)
                dp[st] = att + solve("".join(strl), att + 1)
                ml.append(dp[st])

    if len(ml) > 0:
        return max(ml)
    else:
        return 1
    
solve(s, 0)
print(max(atts)+1)
print(dp)
print(a, b)