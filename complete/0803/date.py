import datetime

today = datetime.date.today()
print('今日は', today, 'です。')
birth = datetime.date(today.year, 6, 25)
ellap = birth - today
if ellap.days == 0:
    print('今日は誕生日です！')
elif ellap.days > 0:
    print('今年の誕生日まで、あと', ellap.days, '日です。')
else:
    print('今年の誕生日は、', -ellap.days, '日、過ぎました。')
