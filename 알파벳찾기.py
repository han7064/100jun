S = input()
res = [-1]*26
for i in range(len(S)):
    a = ord(S[i]) - 97
    if res[a] == -1:
        res[a] = i
print(*res)