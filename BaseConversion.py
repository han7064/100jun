a, b = map(int, input().split())
m = int(input())
arr = list(map(int, input().split()))
arr = list(reversed(arr))
num = 0
for i in range(m):
    num = num + arr[i]*(a**i)
res = []
while num:
    res.append(num%b)
    num = num//b
res.reverse()
print(*res)