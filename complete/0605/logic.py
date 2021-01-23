ja = int(input('国語の点数は？'))
ma = int(input('算数の点数は？'))

if ja >= 70 and ma >= 70:
    print('合格です！')
elif ja >= 70 or ma >= 70:
    print('あと少し！苦手を克服しましょう！')
else:
    print('残念…不合格……')
   