res = [0]*26
S = input()
for i in S:
    res[ord(i)-97] += 1
print(*res)