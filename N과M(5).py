n,m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
res = []
visited = [False]*(n+1)

def dfs():
    if len(res) == m:
        print(' '.join(map(str, res)))
        return
    for i in range(n):
        if visited[i]:
            continue
        res.append(a[i])
        visited[i] = True
        dfs()
        res.pop()
        visited[i] = False
dfs()