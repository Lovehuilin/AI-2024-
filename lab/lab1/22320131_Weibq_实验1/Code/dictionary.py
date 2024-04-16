def ReverseKeyValue(dict1):
    # 我写的函数，用来反转给定非空字典的键值
    dict2 = {}

    for key, value in dict1.items():
        dict2[value] = key
        
    return dict2



def test1():
    # 实例一
    dict1 = {'name': '男', 'age': "男", 'g': '女', 'id': '男', "1": "男"}
    dict2 = ReverseKeyValue(dict1)
    print("test1: ", dict2)


def test2():
    # 实例二
    dict1 = {'name': '小明', 'age': 18, 'gender': '男', 'id': '001'}
    dict2 = ReverseKeyValue(dict1)
    print("test2: ", dict2)
    
test1()
test2()

# 函数缺点：键值不one-to-one时出现覆盖现象，即值相同的值只出现最后一个键值对换

"""
所以我参考https://blog.csdn.net/weixin_46707326/article/details/117387329
修改了函数
"""
from collections import defaultdict

def ReserveKeyValue_v1(dict1):
    
    dict2 = defaultdict(list)
    
    for key, value in dict1.items():
        dict2[value].append(key)

    return dict2

def test3():
    # 实例三
    dict1 = {'name': '男', 'age': "男", 'g': '女', 'id': '男', "1": "男"}
    dict2 = {}
    dict2 = ReserveKeyValue_v1(dict1)
    print("test3: ", dict2)
    
test3()
    
# 但是这么做会输出defaultdict(<class 'list'>, {'男': ['name', 'age', 'id', '1'], '女': ['g']})
# 而前面的defaultdict(<class 'list'>)不是所需要的， 参考 https://www.thinbug.com/q/48823942 我完成了去除类型显示

def test4():
    # 实例四
    dict1 = {'name': '男', 'age': "男", 'g': '女', 'id': '男', "1": "男"}
    dict2 = {}
    dict2 = ReserveKeyValue_v1(dict1)
    print("test4: ", dict(dict2))
    
test4()