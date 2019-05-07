import math


# 1. 定义类，实现 power(x, n) 功能


class Solution():

    def power(self, a, b):
        return a ** b


print(Solution().power(2, -3))
print(Solution().power(3, 5))
print(Solution().power(100, 0))


#  2. 定义类，实现字符串逆序
class Solution():

    def reverse_words(self, one_str):
        return one_str[::-1]


print(Solution().reverse_words('hello.py'))


#  3. 定义三角形类，实现求三角形周长和面积的方法，属性为三个边长
class Rectangle():

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        if self.a + self.b <= self.c:
            return ('不符合三角形边的规定！')
        else:
            return math.sqrt(
                (((self.a + self.b + self.c) / 2) - self.a) * (((self.a + self.b + self.c) / 2) - self.b) * (
                        ((self.a + self.b + self.c) / 2) - self.c) * ((self.a + self.b + self.c) / 2))


rectangle = Rectangle(3, 4, 5)
print(rectangle.perimeter())
print(rectangle.area)


# 4. 定义立方体类，属性为长度、宽度、高度，通过方法来计算它的体积
class Cube():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def volume(self):
        return self.x * self.y * self.z


cube = Cube(1, 2, 3)
print(cube.volume())


# 5. 定义一个人类，包含姓名、性别、年龄等信息
# 所有的变量必须私有。其他类只能通过该类的方法获取和修改
# 实例化一个人类，试着通过该类的方法修改实例化的人的信息
class Human():
    def __init__(self, name, gender, age):
        self.__name = name
        self.__gender = gender
        self.__age = age

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_gender(self, gender):
        self.__gender = gender

    def set_age(self, age):
        self.__age = age


tom = Human('Tom', 'male', 20)
print(tom.get_name(), tom.get_gender(), tom.get_age())
tom.set_age(23)
print(tom.get_age())


# 6. 定义一个学生类，包含三个属性（学号，姓名，成绩）均为私有的
#    分别给这三个属性定义两个方法，一个设置它的值，另一个获得它的值
#    测试这些方法
class Students():
    def __init__(self, id, name, grade):
        self.__id = id
        self.__name = name
        self.__grade = grade

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        self.__grade = grade


zhansan = Students(1850311121, 'zhansan', 567)
print(zhansan.get_id())
zhansan.set_id(1750311121)
print(zhansan.get_id())


# 7. 继承人类编写一个学生类，为学生类添加新的属性和方法，并进行测试
class Students(Human):
    def __init__(self, name, sex, age, num, grade):
        Human.__init__(self, name, sex, age)
        self.__num = num
        self.__grade = grade

    def get_num(self):
        return self.__num

    def get_grade(self):
        return self.__grade

    def set_num(self, num):
        self.__num = num

    def set_grade(self, grade):
        self.__grade = grade

    def study(self):
        return ('恭喜你满分考入天软！')


chao = Students('Chao', 'male', 18, 12132323, 810)
print(chao.get_name(), chao.get_gender(), chao.get_age(), chao.get_num(), chao.get_grade(), chao .study())
