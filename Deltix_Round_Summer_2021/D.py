def s(x, y):
    print('and', x + 1, y + 1)
    p = int(input())
    print('or', x + 1, y + 1)
    q = int(input())
    return p + q
 
n, k = map(int, input().split())
a = [0] * n
x1 = s(0, 1)
x2 = s(0, 2)
x3 = s(1, 2)
a[1] = (x1 - x2 + x3) // 2
a[2] = x3 - a[1]
a[0] = x1 - a[1]
for i in range(3, n):
    a[i] = s(0,i) - a[0]
a.sort()
print('finish', a[k - 1])