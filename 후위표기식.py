def main():
    word = input()
    stack = []
    res = ''
    for i in word:
        if 'A' <= i <= 'Z':
            res += i
        elif i == '(':
            stack.append(i)
        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(i)
        else:
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()

    while stack:
        res += stack.pop()
    print(res)
if __name__ == '__main__':
    main()