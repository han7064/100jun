n=int(input())
cd = [list(input()) for _ in range(n)]
def check():
    max_ = 1
    for i in range(n):
        m = 1
        for j in range(1, n):
            if cd[i][j] == cd[i][j-1]:
                m += 1
            else:
                m = 1
            max_ = max(m, max_)
    for i in range(n):    
        m = 1
        for j in range(1, n):
            if cd[j][i] == cd[j-1][i]:
                m += 1
            else:
                m = 1
            max_ = max(m, max_)
    return max_
res = 1
for i in range(n):
    for j in range(n):
        if j+1 < n and cd[i][j] != cd[i][j+1]:
            cd[i][j], cd[i][j+1] = cd[i][j+1],cd[i][j]
            res = max(res, check())
            cd[i][j], cd[i][j+1] = cd[i][j+1], cd[i][j]
        if i+1 < n and cd[i][j] != cd[i+1][j]:
            cd[i][j], cd[i+1][j] = cd[i+1][j],cd[i][j]
            res = max(res, check())
            cd[i][j], cd[i+1][j] = cd[i+1][j],cd[i][j]
print(res)