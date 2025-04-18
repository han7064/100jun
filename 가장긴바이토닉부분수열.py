n = int(input())
a = list(map(int, input().split()))
reverseA = a[::-1]
dp_up = [1]*n
dp_down = [1]*n
for i in range(n):
    for j in range(i):
        if a[i]>a[j]:
            dp_up[i] = max(dp_up[i],dp_up[j]+1)
        
        if reverseA[i]>reverseA[j]:
            dp_down[i] = max(dp_down[i],dp_down[j]+1)
dp_down = dp_down[::-1]
res = []
for i in range(n):
    res.append(dp_up[i]+dp_down[i]-1)
print(max(res))