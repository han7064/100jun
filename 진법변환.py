li = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
n, b = input().split()
b = int(b)
res = 0
n = list(reversed(n))
for i in range(len(n)):
    res = res + li.index(n[i])*(b**i)
print(res)