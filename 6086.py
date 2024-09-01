from collections import deque

def char_to_int(c):
    if c.isupper():
        return ord(c) - ord('A')
    return ord(c) - ord('a') + 26

def max_flow(source, sink):
    total_flow = 0
    while True:
        parent = [-1] * 52
        queue = deque([source])
        parent[source] = source
        
        while queue and parent[sink] == -1:
            current = queue.popleft()
            for next_node in graph[current]:
                residual = capacity[current][next_node] - flow[current][next_node]
                if residual > 0 and parent[next_node] == -1:
                    parent[next_node] = current
                    queue.append(next_node)
        
        if parent[sink] == -1:
            break
        
        path_flow = float('inf')
        node = sink
        while node != source:
            parent_node = parent[node]
            path_flow = min(path_flow, capacity[parent_node][node] - flow[parent_node][node])
            node = parent_node
        
        node = sink
        while node != source:
            parent_node = parent[node]
            flow[parent_node][node] += path_flow
            flow[node][parent_node] -= path_flow
            node = parent_node
        
        total_flow += path_flow
    
    return total_flow

N = int(input())
graph = [[] for _ in range(52)]
capacity = [[0] * 52 for _ in range(52)]
flow = [[0] * 52 for _ in range(52)]

for _ in range(N):
    a, b, c = input().split()
    a, b = char_to_int(a), char_to_int(b)
    c = int(c)
    
    graph[a].append(b)
    graph[b].append(a)
    capacity[a][b] += c
    capacity[b][a] += c

source = char_to_int('A')
sink = char_to_int('Z')

print(max_flow(source, sink))