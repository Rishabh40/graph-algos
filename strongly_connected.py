#Uses python3
import sys
sys.setrecursionlimit(200000)

def dfs(adj, x, visited, stack):
    visited[x] = 1
    for i in range(len(adj[x])):
        if not visited[adj[x][i]]:
            dfs(adj, adj[x][i], visited, stack)
    stack.append(x)

def reverseEdges(adj):
    r_adj = [[] for _ in range(len(adj))]
    for i in range(len(adj)):
        for j in range(len(adj[i])):
            r_adj[adj[i][j]].append(i)
    return r_adj

def number_of_strongly_connected_components(adj):
    result = 0
    stack = []
    visited = [0] * len(adj)
    for i in range(len(adj)):
        if visited[i] == 0:
            dfs(adj, i, visited, stack)
    r_adj = reverseEdges(adj)
    visited = [0] * len(adj)
    while stack:
        x = stack.pop()
        if not visited[x]:
            dfs(r_adj, x, visited, [])
            result+=1
    return result

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
