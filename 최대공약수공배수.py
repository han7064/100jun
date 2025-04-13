# 유클리드 호제법 활용
def gcd(x,y):
    while y:
        x,y = y,x%y
    return x
A,B = map(int, input().split())
result = gcd(A,B)
print(result)
print(int(A*B/result))