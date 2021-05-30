'''
用户视图层
'''
from interface import user_interface
from interface import bank_interface
from interface import shop_interface
from lib import common

# 全局变量，记录用户是否已登录
login_user = None  # 登录成功  login_user = username


# 1、注册功能
def register():
    while True:
        # 1）让用户输入用户名与密码进行校验
        username = input('请输入用户名: ').strip()
        password = input('请输入密码: ').strip()
        re_password = input('请确认密码: ').strip()
        # 可以输入自定义的金额

        # 小的逻辑处理: 比如两次密码是否一致
        if password == re_password:
            # 2) 调用接口层的注册接口，将用户名与密码交给接口层来进行处理

            # res ---> (False, '用户名已存在!')
            # res = user_interface.register_interface(
            # flag, msg ---> (flag---> False, msg --> '用户名已存在!')

            # (True, 用户注册成功)，  (False, 注册失败)
            flag, msg = user_interface.register_interface(
                username, password
            )

            # 3) 根据flag判断用户注册是否成功，flag控制break的结束
            if flag:
                print(msg)
                break

            else:
                print(msg)


# 2、登录功能
def login():
    # 登录视图
    while True:
        # 1) 让用户输入用户名与密码
        username = input('请输入用户名: ').strip()
        password = input('请输入密码: ').strip()

        # 2）调用接口层，将数据传给登录接口
        # (True, f'用户: [{username}] 登录成功!'),
        # (return False, '密码错误'), (False, '用户不存在，请重新输入！')
        flag, msg = user_interface.login_interface(
            username, password
        )

        if flag:
            print(msg)

            # 给用户记录，已登录
            global login_user
            login_user = username
            break

        else:
            print(msg)


# 3、查看余额
@common.login_auth
def check_balance():
    # 1.直接调用查看余额接口，获取用户余额
    balance = user_interface.check_bal_interface(
        login_user  # username
    )

    print(f'用户{login_user} 账户余额为: {balance}')


# 4、提现功能
@common.login_auth
def withdraw():
    while True:
        # 1) 让用户输入提现金额
        input_money = input('请输入提现金额: ').strip()

        # 2) 判断用户输入的金额是否是数字
        if not input_money.isdigit():
            print('请重新输入')
            continue

        # 3) 用户提现金额，将提现的金额交付给接口层来处理
        flag, msg = bank_interface.withdraw_interface(
            # 用户名, 提现金额
            login_user, input_money
        )

        if flag:
            print(msg)
            break

        else:
            print(msg)


# 5、还款功能
@common.login_auth
def repay():
    '''
    银行卡还款，无论是信用卡或储蓄卡，是否能充任意大小的金额
    :return:
    '''
    while True:
        # 1) 让用户输入还款金额
        input_money = input('请输入需要还款的金额: ').strip()
        # 2）判断用户输入的是否是数字
        if not input_money.isdigit():
            print('请输入正确的金额')
            continue
        input_money = int(input_money)

        # 3) 判断用户输入的金额大于0
        if input_money > 0:
            # 4）调用还款接口
            flag, msg = bank_interface.repay_interface(
                login_user, input_money
            )

            if flag:
                print(msg)
                break
        else:
            print('输入的金额不能小于0')


# 6、转账功能
@common.login_auth
def transfer():
    '''
    1.接收用户输入的 转账目标用户
    2.接收用户输入的 转账金额
    :return:
    '''
    while True:

        # 1）让用户输入转账用户与金额
        to_user = input('请输入转账目标用户: ').strip()
        money = input('请输入转账金额: ').strip()

        # 2）判断用户输入的金额是否是数字或 > 0
        if not money.isdigit():
            print('请输入正确的金额！')
            continue

        money = int(money)

        if money > 0:
            # 3） 调用转账接口
            flag, msg = bank_interface.transfer_interface(
                # 当前用户，目标用户，转账金额
                login_user, to_user, money
            )
            if flag:
                print(msg)
                break
            else:
                print(msg)

        else:
            print('请输入正确的金额！')


# 7、查看流水
@common.login_auth
def check_flow():
    # 直接调用查看流水接口
    flow_list = bank_interface.check_flow_interface(
        login_user
    )

    if flow_list:
        for flow in flow_list:
            print(flow)
    else:
        print('当前用户没有流水!')


# 8、购物功能
# 注意: 该功能比较 "长" 需要花更多的时间，写的过程中一定要记住，先写好思路
@common.login_auth
def shopping():
    # 不从文件中读取商品数据，直接写（ps: 课后作业，从文件中读取商品数据）
    # 1）创建一个商品列表
    # shop_list = {
    #     '0': {'name': '上海灌汤包', 'price': 30},
    # }

    # 列表套列表的商品数据
    # [[商品名称1, 商品单价1], [商品名称2, 商品单价2]...]
    shop_list = [
        ['上海灌汤包', 30],  # 0
        ['矮跟写真抱枕', 250],  # 1
        ['广东凤爪', 28],
        ['香港地道鱼丸', 15],
        ['坦克', 100000],
        ['macbook', 20000],
    ]

    # 初始化当前购物车:
    shopping_car = {}  # {'商品名称': ['单价', '数量']]}

    while True:
        # 1) 打印商品信息，让用户选择
        # 枚举: enumerate(可迭代对象) ---> (可迭代对象的索引， 索引对应的值)
        # 枚举: enumerate(可迭代对象) ---> (0, ['上海灌汤包', 30])
        print('============欢迎来到有趣用品商城============')
        for index, shop in enumerate(shop_list):
            shop_name, shop_price = shop
            print(f'商品编号为:[{index}]',
                  f'商品名称:[{shop_name}]',
                  f'商品单价:[{shop_price}]')
        print('================24小时服务哦==============')

        # 2) 让用户根据商品编号进行选择
        choice = input('请输入商品编号（是否结账输入y or n）: ').strip()

        # 2.1) 输入的是 y 进入支付结算功能
        if choice == 'y':
            if not shopping_car:
                print('购物车是空的，不能支付,请重新输入!')
                continue

            # 6）调用支付接口进行支付
            flag, msg = shop_interface.shopping_interface(
                login_user, shopping_car)

            if flag:
                print(msg)
                break
            else:
                print(msg)

        # 2.2) 输入的是 n 添加购物车
        elif choice == 'n':
            # 判断当前用户是否添加过购物车
            if not shopping_car:
                print('购物车是空的，不能添加,请重新输入!')
                continue

            # 7）调用添加购物车接口
            flag, msg = shop_interface.add_shop_car_interface(
                login_user, shopping_car
            )

            if flag:
                print(msg)
                break

        if not choice.isdigit():
            print('请输入正确的编号!')
            continue

        choice = int(choice)

        # 3) 判断choice是否存在
        if choice not in range(len(shop_list)):
            print('请输入正确的编号!')
            continue

        # 4) 获取商品名称和与单价
        shop_name, shop_price = shop_list[choice]

        # 5）加入购物车
        # 5.1） 判断用户选择的商品是否重复，重复则数量 +1
        if shop_name in shopping_car:
            # [shop_price, 1][1] ---> 1 += 1
            # 添加商品数量
            shopping_car[shop_name][1] += 1

        else:
            # 否则数量默认为1
            # {'商品名称': ['单价', '数量']]}
            shopping_car[shop_name] = [shop_price, 1]

        print('当前购物车: ', shopping_car)


# 9、查看购物车
@common.login_auth
def check_shop_car():
    # 直接调用查看购物车接口
    shop_car = shop_interface.check_shop_car_interface(
        login_user)
    print(shop_car)


# 10、管理员功能（考试额外加分项）
@common.login_auth
def admin():
    from core import admin
    admin.admin_run()


# 创建函数功能字典
func_dic = {
    '1': register,
    '2': login,
    '3': check_balance,
    '4': withdraw,
    '5': repay,
    '6': transfer,
    '7': check_flow,
    '8': shopping,
    '9': check_shop_car,
    '10': admin,
}


# 视图层主程序
def run():
    while True:
        print('''
        ===== ATM + 购物车 =====
            1、注册功能
            2、登录功能
            3、查看余额
            4、提现功能
            5、还款功能
            6、转账功能
            7、查看流水
            8、购物功能
            9、查看购物车
            10、管理员功能
        ========= end =========
        ''')

        # 让用户选择功能编号
        choice = input('请输入功能编号: ').strip()

        # 判断功能编号是否存在
        if choice not in func_dic:
            print('请输入正确的功能编号!')
            continue

        # 调用用于选择的功能函数
        func_dic.get(choice)()  # func_dic.get('1')() ---> register()
