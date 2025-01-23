from dataclasses import dataclass
from typing import Self

expression = input()

@dataclass
class Term:
    value: str

@dataclass
class Operator:
    value: str

parsed = []
bracket = 0

for i, c in enumerate(expression):
    if c == '(':
        bracket += 1
        parsed.append([])
    elif c == ')':
        if bracket > 1:
            last = parsed[-1]
            del parsed[-1]
            parsed[-1].append(last)
        bracket -= 1

    elif c == '*' or c == '/':
        if bracket == 0 or not isinstance(parsed[-1], list):
            parsed.append([])
        parsed[-1].append(Operator(c))
    elif c == '+' or c == '-':
        if bracket:
            parsed[-1].append(Operator(c))
        else:
            parsed.append(Operator(c))
    else:
        # 문자
        if bracket:
            parsed[-1].append(Term(c))
        else:
            parsed.append(Term(c))


print(parsed)
