import sys
input = sys.stdin.readline

so = [True]*1000001
for i in range(2, 1000001):
    if so[i] == True:
        for j in range(i*i,1000001, i):
            so[j] = False

T = int(input())
for _ in range(T):
    res = 0
    N = int(input())
    for h in range(2, N//2+1):
        if so[h] and so[N-h]:
            res+=1
    print(res)