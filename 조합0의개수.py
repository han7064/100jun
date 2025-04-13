import sys

n,m = map(int, sys.stdin.readline().split())

def cnt_k(n, k):
    res = 0
    cnt = k
    while n>1:
        res += n//cnt
        n = n//cnt
    return res

two = cnt_k(n,2) - cnt_k(m,2) - cnt_k(n-m,2)
five = cnt_k(n,5) - cnt_k(m,5) - cnt_k(n-m,5)
print(min(two, five))