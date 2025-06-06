import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
result = [-1]*N
stack = []

for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        result[stack.pop()] = A[i]
    stack.append(i)

print(*result)