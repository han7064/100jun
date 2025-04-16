n = int(input())
a = list(map(int, input().split()))
dp = [1]*n
for i in range(n):
    for j in range(i):
        if a[i]>a[j]:
            dp[i] = max(dp[i],dp[j]+1)
m = max(dp)
print(m)
res = []
for i in range(n-1,-1,-1):
    if dp[i] == m:
        res.append(a[i])
        m -= 1
res.reverse()
print(*res)