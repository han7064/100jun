n = int(input())
a = list(map(int, input().split()))

for i in range(1, n):
    a[i] = max(a[i], a[i]+a[i-1])
print(max(a))