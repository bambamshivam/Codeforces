import math,sys;input=sys.stdin.readline;S=lambda:input().rstrip();I=lambda:int(S());M=lambda:map(int,S().split());L=lambda:list(M());mod1=1000000007;mod2=998244353

from math import sqrt, floor
maxN = 10000000000
prime = []
def sieve(n):
    check = [0] * (1000007)
    i, j = 0, 0
    check[0] = 1
    check[1] = 1
    check[2] = 0

    for i in range(4, n + 1, 2):
        check[i] = True

    for i in range(3, n + 1, 2):
        if i * i > n:
            break
        if (not check[i]):
            for j in range(2 * i, n + 1, i):
                check[j] = True

    prime.append(2)
    for i in range(3, n + 1, 2):
        if (not check[i]):
            prime.append(i)

    return

sieve(floor(sqrt(maxN)))

for _ in range(I()):
    
    def count(a, n, m):
        
        parity = [0] * 3
        for i in range(1, 1 << n):
            mult = 1
            for j in range(n):
                if (i & (1 << j)):
                    mult *= a[j]
            parity[bin(i).count('1') & 1] += (m // mult)
    
        return parity[1] - parity[0]

    def countRelPrime(n, m):
    
        a = [0] * 20
        i = 0
        j = 0
        pz = len(prime)
        while (n != 1 and i < pz):
            if (prime[i] * prime[i] > n):
                break
            if (n % prime[i] == 0):
                a[j] = prime[i]
                j += 1
    
            while (n % prime[i] == 0):
                n //= prime[i]
            i += 1
    
        if (n != 1):
            a[j] = n
            j += 1
        return m - count(a, j, m)
    
    def countRelPrimeInRange(n, l, r):
        result = countRelPrime(n, r)
        return result

    n,m=M();a=L();f=0;ans=1
    for i in range(1,n):
        if a[i-1]%a[i]!=0:f=1;break
        ans=(ans*countRelPrimeInRange(a[i-1]//a[i],1,m//a[i]))%mod2
    print(0 if f else ans)
    