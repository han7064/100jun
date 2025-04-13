n = int(input())
res = 0
while n>1:
    res += n//5
    n = n//5
print(res)