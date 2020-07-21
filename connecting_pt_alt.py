#Uses python3
import sys
import math



if __name__ == '__main__':
    n = int(input())
    x = []
    y = []
    for _ in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    print("{0:.9f}".format(minimum_distance(x, y)))