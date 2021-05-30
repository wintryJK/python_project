
# 装饰器是在不修改被装饰对象的源代码以及调用方式的前提下为被装饰对象添加功能
# 新功能的可调用对象

# print(property)

# property是一个装饰器，是用来干什么的？
# 是用来将类中的方法伪装成数据属性
"""
成人的BMI数值：
过轻：低于18.5
正常：18.5-23.9
过重：24-27
肥胖：28-32
非常肥胖, 高于32
　　体质指数（BMI）=体重（kg）÷身高^2（m）
　　EX：70kg÷（1.75×1.75）=22.86
"""
# class People:
#     def __init__(self,name,weight,height):
#         self.name = name
#         self.weight = weight
#         self.height = height
#
#     # 定义函数的原因
#     # 1、bmi是通过计算得到的
#     # 2、bmi是随着身高体重的变化而动态变化的
#
#     # 但是bmi听起来更像是一个数据而不是功能
#     @property
#     def bmi(self):
#         return self.weight / (self.height ** 2)
#
#
# obj1 = People('egon',70,1.83)
# print(obj1.bmi)

# 案例二
# class People:
#     def __init__(self,name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self,val):
#         if type(val) is not str:
#             print("str!!!")
#             return
#         self.__name = val
#     def del_name(self):
#         print("no!!!")
#
#     name = property(get_name,set_name,del_name)
#
# obj1 = People('egon')
# print(obj1.get_name())

# obj1.set_name('EGON')
# print(obj1.get_name())
# 人的思维
# print(obj1.name)
# obj1.name = '111'
# del obj1.name


# 案例三
class People:
    def __init__(self,name):
        self.__name = name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,val):
        if type(val) is not str:
            print("str!!!")
            return
        self.__name = val
    @name.deleter
    def name(self):
        print("no!!!")









