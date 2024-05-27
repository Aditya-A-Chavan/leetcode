from collections import defaultdict, deque


N, M, S = map(int, input().split())

graph = defaultdict(list)

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append[v]
    print(graph)    