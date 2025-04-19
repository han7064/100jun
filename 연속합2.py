n = int(input())
a = list(map(int, input().split()))
dp = [[0]*n for _ in range(2)]
dp[0][0] = a[0]
dp[1][0] = a[0]
for i in range(1,n):
    dp[0][i] = max(dp[0][i-1]+a[i], a[i])
    dp[1][i] = max(dp[1][i-1]+a[i], dp[0][i-1])

print(max(max(dp[0]),max(dp[1])))