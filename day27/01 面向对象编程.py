'''
面向过程：
    核心是过程
        将程序流程化
        过程是流水线，用分步骤来解决问题

面向对象：
    核心是对象
        对象是“容器”，用来盛放数据和功能的
        终极奥义就是将程序“整合”

'''

# 程序=数据+功能

# 学生的数据
stu_name = 'egon'
stu_age = 18
stu_gender = 'male'

def tell_info():
    print('名字 : %s 年龄 : %s 性别 : %s' %(stu_name,stu_age,stu_gender))

tell_info()