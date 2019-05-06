class ClassName(object):
    pass


class Human:
    def __init__(self, name, age, gender):  # 强制定义属性
        self.name = name
        self.__age = age
        self._gender = gender

    def fun_test(self):
        pass

    def get_name(self):
        return self.name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            raise ValueError("Error: age < 0")


tom = Human('Tom', 19, 'male')

print(tom.name)

print(tom.get_age())


class Human(object):
    pass


human = Human()
print(type(human))

human.name = 'Tom'
print(human.name)  # 自由绑定属性
