n,m = map(int, input().split())
s = []
visited = [False]*(n+1)

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        if visited[i]:
            continue
        if s and i <= s[-1]:
            continue
        s.append(i)
        visited[i] = True
        dfs()
        s.pop()
        visited[i] = False
dfs()


# 다른 방식 1 부터 시작해서 1씩 커진 값으로 시작 해서 오름차순
'''def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(start, n + 1):
        if not visited[i]:
            visited[i] = True
            s.append(i)
            dfs(i + 1)  # 다음 숫자는 지금보다 더 큰 수만
            s.pop()
            visited[i] = False

dfs(1)'''