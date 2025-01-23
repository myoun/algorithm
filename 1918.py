from dataclasses import dataclass

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

def apply_priority1(ast):
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
                next = apply_priority1(ast[i+1])
            new_ast.append([prev, e, next])
            p = 1
        elif isinstance(e, list):
            new_ast.append(apply_priority1(e))
        else:
            new_ast.append(e)
    
    return new_ast

def apply_priority2(ast):
    new_ast=[]
    p = 0

    for i, e in enumerate(ast):

        if p > 0:
            p -= 1
            continue

        if isinstance(e, Operator) and (e.value == "+" or e.value =="-"):
            prev = new_ast[-1]
            del new_ast[-1]
            next = ast[i+1]
            if isinstance(ast[i+1], list):
                next = apply_priority2(ast[i+1])
            new_ast.append([prev, e, next])
            p = 1
        elif isinstance(e, list):
            new_ast.append(apply_priority2(e))
        else:
            new_ast.append(e)
    
    return new_ast

def to_postfix(ast):
    result = []
    operator = ""
    for element in ast:
        if isinstance(element, list):
            result.append(to_postfix(element))
        elif isinstance(element, Term):
            result.append(element.value)
        elif isinstance(element, Operator):
            operator = element.value
    return "".join(result)+operator

parsed = apply_priority2(apply_priority1(parsed))
postfix_expression = to_postfix(parsed)
print(postfix_expression)
