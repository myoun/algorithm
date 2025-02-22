V = int(input())

nodes = {i:{} for i in range(1, V+1)}
    
for i in range(V-1):
    p, c, w = map(int, input().split())
    nodes[p][c] = w
    nodes[c][p] = w

def dfs(start):
    stack = [(start, 0)]
    visited = 0

    deepest = (None, -1)

    while stack:
        node, acc = stack.pop()
        visited |= (1 << node)
        
        if acc > deepest[1]:
            deepest = (node, acc)

        children = nodes[node].keys()

        for next in children:
            if not (visited & (1 << next)):
                nd = nodes[node][next]
                stack.append((next, acc+nd))
    return deepest

a = dfs(1)[0]
b, d = dfs(a)

print(d)