p=input
n,m=map(int,p().split())
c=[1]
for i in range(m):
 a,b=map(int,p().split())
 c+=[c[i]+b*(3-a*2)]
 if a>2:c[-1]=c[b]
print((c[m]-1)%n+1)