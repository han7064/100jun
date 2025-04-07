import sys
input = sys.stdin.readline
q = []
N = int(input())
for i in range(N):
    command = input().split()
    if command[0] == 'push':
        q.append(command[1])
    elif command[0] == 'pop':
        if q:
            print(q.pop(0))
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)