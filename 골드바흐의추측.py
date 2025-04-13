import sys

sosu = [True]*1000001
m = int(1000001**0.5)
for i in range(2,m+1):
    if sosu[i]==True:
        for j in range(i*i, 1000001, i):
            sosu[j] = False

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    for i in range(3, n//2+1, 2):
        if sosu[i] and sosu[n-i]:
            print("%d = %d + %d" %(n, i, n-i))
            break
    else:
        print("Goldbach's conjecture is wrong")