n = int(input())
m = int(input())
if m == 0:
    a = []
else:
    a = list(input().split())
cnt = abs(100-n)
for i in range(1000001):
    for j in str(i):
        if j in a:
            break
    else:
        cnt = min(cnt, len(str(i))+abs(i-n))
print(cnt)