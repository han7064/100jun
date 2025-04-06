stack, ans, find = [], [], True
num1 = 1
n = int(input())
for i in range(n):
    num2 = int(input())
    while num1 <=num2:
        stack.append(num1)
        ans.append('+')
        num1 += 1
    if stack[-1] == num2:
        stack.pop()
        ans.append('-')
    else:
        find = False
if not find:
    print('NO')
else:
    for i in ans:
        print(i)