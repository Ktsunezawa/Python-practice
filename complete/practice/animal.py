class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, ':', self.age, '歳')

class Hamster(Animal):
    def __init__(self, name, age, type):
        super().__init__(name, age)
        self.type = type

if __name__ == '__main__':
    h = Hamster('サクラ', 1, 'スノーホワイト')
    print(h.type)
