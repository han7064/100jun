while True:
    try :
        word = list(input())
        lower, upper, num, blank = 0, 0, 0, 0
        for i in range(len(word)):
            if word[i] == ' ':
                blank += 1
            elif 65 <= ord(word[i]) <= 90:
                upper += 1
            elif 97 <= ord(word[i]) <= 122:
                lower += 1
            else:
                num += 1
        print(lower,upper,num,blank)
    except EOFError:
        break