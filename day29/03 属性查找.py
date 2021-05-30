
# 单继承背景下的属性查找
# 示范一：
# class Foo:
#     def f1(self):
#         print('Foo.f1')
#
#     def f2(self):
#         print('Foo.f2')
#         Foo.f1(self)
#         # self.f1()
#
# class Bar(Foo):
#     def f1(self):
#         print('Bar.f1')
#
# obj = Bar()
# obj.f2()
# Foo.f2
# Bar.f1

# 示范2
# class Foo:
#     def f1(self):
#         print('Foo.f1')
#
#     def f2(self):
#         print('Foo.f2')
#         Foo.f1(self)
#
# class Bar(Foo):
#     def f1(self):
#         print('Bar.f1')
#
# obj = Bar()
# obj.f2()

# 示范3
class Foo:
    def __f1(self):
        print('Foo.f1')

    def f2(self):
        print('Foo.f2')
        # Foo.f1(self)
        self.__f1() # 这里已经变形_Foo__f1

class Bar(Foo):
    def f1(self):  #__f1,也会调用Foo
        print('Bar.f1')

obj = Bar()
obj.f2()