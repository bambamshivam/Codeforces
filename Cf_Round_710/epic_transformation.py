t = int(input().strip())
 
for _ in range(t):
    n = int(input().strip())
    d = {}
    
    for i in input().split():
        d[i] = d.get(i,0)+1
    
    print(max(2*max(d.values())-n, n%2))