point = int(input('あなたの点数は？'))

if point >= 90:
    print('素晴らしい！文句なしの合格です！')
elif point >= 70:
    print('おめでとう！合格です！')
elif point >= 50:
    print('残念！もう少しでした……')
else:
    print('残念…不合格……')
