point = int(input('あなたの点数は？'))

if point >= 70:
    print('合格です！')
else:
    print('残念…不合格……')
    if point >= 50:
        print('でも、あともう少しですよ……')
    else:
        print('もっと頑張りましょう！')
