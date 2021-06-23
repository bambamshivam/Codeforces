for _ in range(int(input())):
    n = int(input())
    ans = 0
    s = list(input())
    c = s.count("*")
    i = 0
    for x in s:
        if x > '*': ans += min(i, c - i)
        else: i += 1
    print(ans)