#Uses python3


def distance(adj, s, t):
    #write your code here
    dist = [float("inf")] * len(adj)
    dist[s] = 0
    queue = []
    queue.append(s)
    while queue:
        u = queue.pop(0)
        for v in adj[u]:
            if dist[v] == float("inf"):
                queue.append(v)
                dist[v] = dist[u] + 1
    if dist[t] != float("inf"):
        return dist[t]
    return -1

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = map(int, input().split())
    print(distance(adj, s - 1, t - 1))
