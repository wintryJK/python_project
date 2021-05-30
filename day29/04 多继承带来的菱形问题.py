

# class A(object):
#     def test(self):
#         print('from A')
#
#
# class B(A):
#     def test(self):
#         print('from B')
#
#
# class C(A):
#     def test(self):
#         print('from C')
#
#
# class D(C,B):
#     pass
#
#
# obj = D()
# obj.test()
#
# print(D.mro())

# 二：如果多继承是非菱形
class E:
    # def test(self):
    #     print('from E')
    pass


class F:
    def test(self):
        print('from F')


class B(E):
    def test(self):
        print('from B')


class C(F):
    def test(self):
        print('from C')


class D:
    def test(self):
        print('from D')


class A(B, C, D):
    # def test(self):
    #     print('from A')
    pass


print(A.mro())
'''
[<class '__main__.A'>, <class '__main__.B'>, <class '__main__.E'>, <class '__main__.C'>, <class '__main__.F'>, <class '__main__.D'>, <class 'object'>]
'''

obj = A()
obj.test()
print(E.__bases__)