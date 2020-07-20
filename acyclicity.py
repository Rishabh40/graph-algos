#Uses python3

import sys

def dfs(adj, x, visited, stack):
    visited[x] = 1
    stack[x] = 1
    for i in range(len(adj[x])):
        if visited[adj[x][i]] == 0 and dfs(adj, adj[x][i], visited, stack):
            return 1
        elif stack[adj[x][i]] == 1:
            return 1
    stack[x] = 0
    return 0

def acyclic(adj):
    visited = [0 for _ in range(len(adj))]
    stack = [0 for _ in range(len(adj))]
    for i in range(len(adj)):
        if visited[i] == 0:
            if dfs(adj, i, visited, stack):
                return 1
    return 0

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
