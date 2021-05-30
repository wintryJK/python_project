# 1、什么是继承
# I:继承是一种创建新类的方式，子类会遗传父类的属性
# II:python支持多继承  在python中，新建的类可以继承一个或多个类


# class Parent1:
#     pass
#
# class Parent2:
#     pass
#
# class Sub1(Parent1): # 单继承
#     pass
#
# class Sub2(Parent1,Parent2):
#     pass
#
# print(Sub1.__bases__)
# print(Sub2.__bases__)

# ps:python2中有经典类和新式类
# 新式类:继承了object及其子类，子类的子类
# 经典：没有继承object

# ps2：python3中没有继承任何类，默认继承object类

# III：python的多继承
#  优点：子类可以同时遗传多个父类的属性，最大限度地重用代码
#  缺点：
#       1、继承表达的是一种什么“是”什么的关系
#       2、代码的可读性会变差
#       3、不建议使用多继承，扩展性变差，如果真的涉及到重用多个父类的属性，应该使用,Mixins
#       4、有可能会引发菱形问题
# 2、为何要继承：解决类与类之间的代码冗余问题


# 3、如何实现继承
# 示范一
# class Student:
#     school = 'OLDBOY'
#
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def choose_course(self):
#         print('%s 正向选课' %self.name)
#
# class Teacher:
#     school = 'OLDBOY'
#
#     def __init__(self,name,age,sex):
#         pass

# 示范二
class OldboyPeople:
    school = 'OLDBOY'

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex



class Student(OldboyPeople):
    # school = 'OLDBOY'
    #
    # def __init__(self,name,age,sex):
    #     self.name = name
    #     self.age = age
    #     self.sex = sex

    def choose_course(self):
        print('%s 正向选课' %self.name)

stu_obj = Student('lili',18,'famle')
print(stu_obj.__dict__)

class Teacher(OldboyPeople):
    # school = 'OLDBOY'
    #
    def __init__(self,name,age,sex,salary,level):
        # 要指名道姓的要父类的init
        OldboyPeople.__init__(self,name,age,sex)
        self.salary = salary
        self.level = level

tea_obj = Teacher('lili',19,'famale',3000,18)
print(tea_obj.__dict__)


















