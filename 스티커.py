t = int(input())
for _ in range(t):
    n = int(input())
    dp = [0]*2
    for i in range(2):
        dp[i] = list(map(int, input().split()))
    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue
    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]
    for i in range(2, n):
        dp[0][i] += max(dp[1][i-1],dp[1][i-2])
        dp[1][i] += max(dp[0][i-1],dp[0][i-2])
    print(max(dp[0][n-1],dp[1][n-1]))