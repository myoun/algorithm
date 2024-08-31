import re

s = input()

regex = r"(100+1+|01)+"

p = re.compile(regex)
m = p.fullmatch(s)
if m:
    print("SUBMARINE")
else:
    print("NOISE")