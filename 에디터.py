talk = list(input())
curser = []
M = int(input())
for i in range(M):
    command = input().split()
    if command[0] == 'L' and talk:
        curser.append(talk.pop())
    elif command[0] == 'D' and curser:
        talk.append(curser.pop())
    elif command[0] == 'B' and talk:
        talk.pop()
    elif command[0] == 'P':
        talk.append(command[1])
answer = talk+curser[::-1]
print(''.join(answer))