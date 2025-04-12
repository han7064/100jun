S = input()
res = []

for i in range(len(S)):
    res.append(S[i:])
res.sort()
print(*res)