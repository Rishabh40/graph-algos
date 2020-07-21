#Uses python3
import sys
import math

def getDistance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)** 2 + (y1 - y2)** 2)

def clustering(x, y, k):
    edges = []
    for i in range(n):
        for j in range(i, n):
            if i != j:
                edges.append((i, j, getDistance(x[i], y[i], x[j], y[j])))
    result = 0
    edges.sort(key=lambda x: x[2])
    membership = [i for i in range(n)]
    MST = []
    ans = 0
    for edge in edges:
        if membership[edge[0]] != membership[edge[1]]:
            if len(set(membership)) == k:
                ans = edge[2]
                break
            MST.append(edge)
            result += edge[2]
            membership = list(map(lambda x: membership[edge[0]] if x == membership[edge[1]] else x, membership))
    return ans


if __name__ == '__main__':
    n = int(input())
    x = []
    y = []
    for _ in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    k = int(input())
    print("{0:.9f}".format(clustering(x, y, k)))
