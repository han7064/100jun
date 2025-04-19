nan = []
for _ in range(9):
    nan.append(int(input()))
m = sum(nan)
nan.sort()
one, two = 0, 0
for i in range(1,9):
    for j in range(i):
        if m-(nan[i]+nan[j])==100:
            one, two = nan[i], nan[j]
            break
nan.remove(one)
nan.remove(two)
for i in nan:
    print(i)