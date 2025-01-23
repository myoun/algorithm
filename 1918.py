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

# Parse
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
    elif c == '*' or c == '/' or c == '+' or c == '-':
        if bracket:
            parsed[-1].append(Operator(c))
        else:
            parsed.append(Operator(c))
    else:
        if bracket:
            parsed[-1].append(Term(c))
        else:
            parsed.append(Term(c))

def apply_priority(ast):
    new_ast=[]
    p = 0

    for i, e in enumerate(ast):

        if p > 0:
            p -= 1
            continue

        if isinstance(e, Operator) and (e.value == "*" or e.value =="/"):
            prev = new_ast[-1]
            del new_ast[-1]
            next = ast[i+1]
            if isinstance(ast[i+1], list):
                next = apply_priority(ast[i+1])
            new_ast.append([prev, e, next])
            p = 1
        elif isinstance(e, list):
            new_ast.append(apply_priority(e))
        else:
            new_ast.append(e)
    
    return new_ast

parsed = apply_priority(parsed)
