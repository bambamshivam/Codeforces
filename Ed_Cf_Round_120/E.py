def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    g = [input() for i in range(n)]
    ma = -1
    ans = []
    for mask in range(1<<n):
        L = [0]*m
        for i in range(n):
            for j in range(m):
                if g[i][j] == "1":
                    L[j] += ((mask>>i&1)<<1)-1
        cur = sum(arr[i]*(-((mask>>i&1)<<1)+1) for i in range(n))
        cl = [0]*(2*n+1)
        for a in L:
            cl[a+n] += 1
        k = 1
        for i, c in enumerate(cl):
            cur += (i-n)*(2*k+c-1)*c//2
            k += c
        if ma < cur:
            ma = cur
            ans = L
    cl = [0]*(2*n+1)
    for a in ans:
        cl[a+n] += 1
    for i in range(1, 2*n+1):
        cl[i] += cl[i-1]
    ca = []
    for a in ans:
        ca.append(cl[a+n])
        cl[a+n] -= 1
    return ca


import sys
input = lambda: sys.stdin.readline().rstrip()
t = int(input())
for i in range(t):
    print(*solve())
