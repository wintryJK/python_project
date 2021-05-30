'''
银行相关业务的接口
'''
from db import db_handler
from lib import common

# 根据不同的接口类型传入不同的日志对象
bank_logger = common.get_logger(log_type='bank')


# 提现接口(手续费5%)
def withdraw_interface(username, money):
    # 1) 先获取用户字典
    user_dic = db_handler.select(username)

    # 账户中的金额
    balance = int(user_dic.get('balance'))

    # 提现本金 + 手续费
    money2 = int(money) * 1.05  # ---> float

    # 判断用户金额是否足够
    if balance >= money2:
        # 2）修改用户字典中的金额
        balance -= money2

        user_dic['balance'] = balance

        # 3）记录流水
        flow = f'用户[{username}] 提现金额[{money}$]成功，手续费为: [{money2 - float(money)}$]'
        user_dic['flow'].append(flow)

        # 4）再保存数据，或更新数据
        db_handler.save(user_dic)

        bank_logger.info(flow)

        return True, flow

    return False, '提现金额不足，请重新输入!'


# 还款接口
def repay_interface(username, money):
    '''
    1.获取用户的金额
    2.给用户的金额做加钱的操作
    :return:
    '''

    # 1.获取用户字典
    user_dic = db_handler.select(username)

    # 2.直接做加钱操作
    # user_dic['balance'] ---> int
    user_dic['balance'] += money

    # 3.记录流水
    flow = f'用户：[{username}]  还款：[{money}]成功!'
    user_dic['flow'].append(flow)

    # 4.调用数据处理层，将修改后的数据更新
    db_handler.save(user_dic)

    return True, flow


# 转账接口
def transfer_interface(login_user, to_user, money):
    '''
    1.获取 "当前用户" 数据
    2.获取 "目标用户" 数据
    3.获取转账金额
    :return:
    '''

    # 1）获取 "当前用户" 字典
    login_user_dic = db_handler.select(login_user)

    # 2) 获取 "目标用户" 字典
    to_user_dic = db_handler.select(to_user)

    # 3) 判断目标用户是否存在
    if not to_user_dic:
        return False, '目标用户不存在'

    # 4）若用户存在，则判断 "当前用户的转账金额" 是否足够
    if login_user_dic['balance'] >= money:
        # 5) 若足够，则开始给目标用户转账
        # 5.1）给当前用户的数据，做减钱操作
        login_user_dic['balance'] -= money

        # 5.2）给目标用户的数据，做加钱操作
        to_user_dic['balance'] += money

        # 5.3) 记录当前用户与目标用户的流水
        # 当前用户流水
        login_user_flow = f'用户: [{login_user}] 给 用户: [{to_user}] 转账: [{money}$] 成功!'
        login_user_dic['flow'].append(login_user_flow)

        # 目标用户流水
        to_user_flow = f'用户: [{to_user}] 接收 用户: [{login_user}] 转账: [{money}$] 成功!'
        to_user_dic['flow'].append(to_user_flow)

        # 6) 保存用户数据
        # 6.1) 调用数据处理层的save功能，保存当前用户数据
        db_handler.save(login_user_dic)

        # 6.2) 调用数据处理层的save功能，保存目标用户数据
        db_handler.save(to_user_dic)

        return True, login_user_flow

    return False, '当前用户转账金额不足!'


# 查看流水接口
def check_flow_interface(login_user):
    user_dic = db_handler.select(login_user)
    return user_dic.get('flow')


# 支付接口
def pay_interface(login_user, cost):
    user_dic = db_handler.select(login_user)

    # 判断用户金额是否足够
    if user_dic.get('balance') >= cost:
        # 减钱
        user_dic['balance'] -= cost

        # 记录消费流水
        flow = f'用户消费金额: [{cost}$]'
        user_dic['flow'].append(flow)

        # 保存数据
        db_handler.save(user_dic)

        # return True 或 return False 交给购物接口来做处理
        return True

    return False
