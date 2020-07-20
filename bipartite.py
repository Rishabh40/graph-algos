#Uses python3

def bipartite(adj):
    color = [-1] * len(adj)
    color[0] = 1
    queue = []
    queue.append(0)
    while queue:
        u = queue.pop(0)
        for v in adj[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                queue.append(v)
            elif color[v] == color[u]:
                return 0
    return 1

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
