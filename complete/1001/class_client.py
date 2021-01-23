import myclass

# p1 = myclass.Person()
# print(p1)

p1 = myclass.Person('サクラ', 1.21, 23)
bmi1 = p1.weight / (p1.height * p1.height)
print(p1.name, 'のBMI値は', bmi1, 'です。')

p2 = myclass.Person('キラ', 1.35, 30)
bmi2 = p2.weight / (p2.height * p2.height)
print(p2.name, 'のBMI値は', bmi2, 'です。')
