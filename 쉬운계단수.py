n = int(input())
dp = [[0,0,0,0,0,0,0,0,0,0] for _ in range(n+1)]
dp[1] = [0,1,1,1,1,1,1,1,1,1]
for i in range(2, n+1):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]
    for j in range(1,9):
        dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1]
print(sum(dp[n])%1000000000)        