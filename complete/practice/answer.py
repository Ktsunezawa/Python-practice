answer1 = int(input('解答1の値は？'))
answer2 = int(input('解答1の値は？'))

if answer1 == 1 and answer2 == 5:
    print('双方が正解')
else:
    if answer1 == 1:
        print('解答1だけが正解')
    elif answer2 == 5:
        print('解答2だけが正解')
    else:
        print('双方が不正解')
