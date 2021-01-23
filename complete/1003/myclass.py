class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def bmi(self):
        result = self.weight / (self.height * self.height)
        print(self.name, 'のBMI値は', result, 'です。')

class BusinessPerson(Person):
    def __init__(self, name, height, weight, title):
        super().__init__(name, height, weight)
        self.title = title

    def work(self):
        print(self.title, 'の', self.name, 'は働いています。')
