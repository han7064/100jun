import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
cnt = [0]*10000001
res = [-1]*N
stack = []
for num in A:
    cnt[num] += 1
for i in range(N):
    while stack and cnt[A[stack[-1]]] < cnt[A[i]]:
        res[stack.pop()] = A[i]
    stack.append(i)
print(*res)