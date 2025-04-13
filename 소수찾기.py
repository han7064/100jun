N = int(input())
a = list(map(int, input().split()))
result = 0
for i in a:
    stack = []
    for j in range(1,i+1):
        if i%j == 0:
            stack.append(j)
    if len(stack) == 2:
        result += 1
print(result)