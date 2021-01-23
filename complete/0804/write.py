import datetime

file = open('0804/hoge.txt', 'w', encoding='UTF-8')
file.write(str(datetime.datetime.now()) + '\n')
file.close()
print('ファイルを保存しました。')
