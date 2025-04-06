T = int(input())
for i in range(T):
    word = list(input().split())
    for j in word:
        print(j[::-1], end=' ')
    print()