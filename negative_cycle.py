#Uses python3
def negative_cycle(adj, cost):
    #write your code here
    dis = [float("inf")] * len(adj)
    dis[0] = 0
    temp = list(dis)
    for i in range(len(adj)):
        for u in range(len(adj)):
            for j in range(len(adj[u])):
                v = adj[u][j]
                if dis[v] > dis[u] + cost[u][j]:
                    dis[v] = dis[u] + cost[u][j]
        if i == len(adj) - 2:
            temp = list(dis)
    if temp == list(dis):
        return 0
    return 1

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for i in range(m):
        a, b, w = map(int, input().split())
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
