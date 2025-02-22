import fractions as m
f=m.Fraction
a,b,c,d=map(int,open(0).read().split())
print(*(f(a,b)+f(c,d)).as_integer_ratio())