'''
根据输入的年龄计算要花费多少钱
帮一个高中生写的
'''
__author__ = '符灏'

# 计算不同年龄从婴儿到该年龄的总花费
def costbyage(age):
    cost = 0
    # 婴儿阶段
    if age <= 3:
        cost = 1000*12*age
    # 幼儿园
    elif age <= 6:
        cost = costbyage(3) + 5100 * 12 * (age - 3)
    # 小学
    elif age <= 12:
        cost = costbyage(6) + 1000*12*(age - 6) + 2000*(age - 6)
    # 初中
    elif age <= 15:
        cost = costbyage(12) + 3000*(age - 12) + 40000
    # 高中
    elif age <= 18:
        cost = costbyage(15) + 4000*(age - 15) + 50000
    else:
        print('目前只能计算到高中，请重新输入1-18的年龄')
    return cost


def inputage():
    # 接受用户输入
    ageinput = input('请输入年龄:')
    # 判断输入是否是整数
    if ageinput.isdigit():
        cost = costbyage(int(ageinput))
        # 计算出了花费
        if cost != 0:
            print('输入的年龄是:',ageinput,' 花费:', cost,'元')
        else:
            inputage()
    else:
        inputage()

cost = inputage()
