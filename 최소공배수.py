T = int(input())
for i in range(T):
    a,b = map(int, input().split())
    s = a*b
    while b:
        a,b = b,a%b
    print(int(s/a))