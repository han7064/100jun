import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

n, s = map(int, input().split())
A = list(map(int, input().split()))

for i in range(n):
    A[i] = abs(s - A[i]) 
res = A[0]
for i in range(1,n):
    res = gcd(res, A[i])
print(res)