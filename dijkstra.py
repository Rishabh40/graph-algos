#Uses python3

import sys
import queue
from heapq import heapify, heappop, heappush


def distance(adj, cost, s, t):
    dist = [float("inf")] * len(adj)
    dist[s] = 0
    li = [(0, s)]  # (distance,index)
    heapify(li)
    while len(li) > 0:
        u_whole = heappop(li)
        u = u_whole[1]
        # u_d = u_whole[0]
        for i in range(len(adj[u])):
            v = adj[u][i]
            if dist[v] > dist[u] + cost[u][i]:
                dist[v] = dist[u] + cost[u][i]
                heappush(li, (dist[v], v))
    if dist[t] == float("inf"):
        return -1
    return dist[t]


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for i in range(m):
        a, b, w = map(int, input().split())
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = map(int, input().split())
    print(distance(adj, cost, s - 1, t - 1))

"""
4 4
1 2 1
4 1 2
2 3 2
1 3 5
1 3
"""