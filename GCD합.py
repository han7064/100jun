import sys

t = int(sys.stdin.readline())
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

for i in range(t):
    case = list(map(int, sys.stdin.readline().split()))
    n = case[0]
    res = 0
    for j in range(1, n+1):
        for h in range(j+1, n+1):
            res += gcd(case[j], case[h])
    print(res)        