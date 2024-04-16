import re
import copy
from __print__ import print_msg, __print
from __Predicate import Predicate

S = [] # 存储子句集

def end_or_not(new_clause, set_of_clause):
    if len(new_clause) == 0:  # 新生成的new_clause已经为空
        print("[]")
        return True
    if len(new_clause) == 1:  # 查找已有的子句中是否存在与新子句互补
        for i in range(len(set_of_clause) - 1):  # set_of_clause[j]超过一个谓词的取或的子句
            if len(set_of_clause[i]) == 1 and new_clause[0].get_name() == set_of_clause[i][0].get_name() and new_clause[0].element[1:] == \
                    set_of_clause[i][0].element[1:] and new_clause[0].get_pre() != set_of_clause[i][0].get_pre():
                print(len(set_of_clause) + 1, ": R[", i + 1, ", ", len(set_of_clause), "]() = []", sep="")
                return True
    return False  # 不符合条件不结束


def ResolutionFOL(num_of_clause):
    set_of_clause = []  # 存储子句集
    tmp = ""  # 用于拆分子句使用的中间变量
    for i in range(int(num_of_clause)):
        clause_input = input()  # 输入子句
        if clause_input[0] == '(':  # 去掉子句的左括号
            clause_input = clause_input[1: -1]
        
        clause_input = clause_input.replace(' ', '')  # 去掉子句中的空格
        set_of_clause.append([])  # 为子句集添加一个新的子句
        for cnt in range(len(clause_input)):  # 拆分存储在列表里
            tmp += clause_input[cnt] # 一个一个字符的拆分
            if clause_input[cnt] == ')':  # 遇到右括号，说明一个谓词结束
                if cnt + 1 != num_of_clause: # 如果不是最后一个谓词，加上逗号
                    clause_tmp = Predicate(tmp)  # 创造一个谓词公式类Predicate的变量
                    set_of_clause[i].append(clause_tmp)  # 加入到子句集的第i个子句中
                tmp = "" # 清空tmp

    for i in range(len(set_of_clause)):  # 输出子句
        __print(set_of_clause[i]) 
    status = True  # 用于判断是否结束归结过程
    while status:
        for i in range(len(set_of_clause)):
            if not status: # 用于跳出多重循环
                break
            if len(set_of_clause[i]) == 1:  # set_of_clause[i]是只有一个谓词的子句
                for j in range(0, len(set_of_clause)):  # 找可使用规则 (A)and(¬A,B,C,...) => (B,C,...) 的子句set_of_clause(j)
                    if not status:   # 用于跳出多重循环
                        break
                    if i == j:  # 不能与自己进行消去
                        continue
                    prename = [] # 记录需要换名的变量
                    newname = []  # 记录换名后的变量
                    target = -1  # 记录可以消去的子句的位置
                    for k in range(len(set_of_clause[j])):  # 找到可以消去的子句
                        if set_of_clause[i][0].get_name() == set_of_clause[j][k].get_name() and set_of_clause[i][
                            0].get_pre() != set_of_clause[j][k].get_pre():
                            target = k
                            for l in range(len(set_of_clause[j][k].element) - 1):  # 找到可以换名的变量并记录
                                if len(set_of_clause[j][k].element[l + 1]) == 1:  # 是自由变量
                                    prename.append(set_of_clause[j][k].element[l + 1])
                                    newname.append(set_of_clause[i][0].element[l + 1])
                                # 是相同的变量
                                elif len(set_of_clause[i][0].element[l + 1]) == 1:
                                    prename.append(set_of_clause[i][k].element[l + 1])
                                    newname.append(set_of_clause[j][0].element[l + 1])
                                # 是不同的变量
                                elif set_of_clause[j][k].element[l + 1] != set_of_clause[i][0].element[l + 1]:
                                    target = -1
                                    break
                                
                            break
                    if target == -1:  # 没有找到可以消去的子句
                        continue
                    new_clause = []  # 记录生成的新子句
                    for k in range(len(set_of_clause[j])):
                        if k != target:  # 生成新子句
                            p = Predicate("")
                            p.new(set_of_clause[j][k].element)
                            p.rename(prename, newname)
                            new_clause.append(p)
                    if len(new_clause) == 1:  # 判断是否生成的子句是否与已有重复（不判断是否生成了子句）
                        for k in range(len(set_of_clause)):
                            if len(set_of_clause[k]) == 1 and new_clause[0].element == set_of_clause[k][0].element:
                                target = -1
                                break
                    if target == -1:  # 如果生成的子句已存在，跳过加入子句集的过程
                        continue
                    set_of_clause.append(new_clause)  # 生成的新的子句加入的子句集中
                    print_msg(target, i, j, prename, newname, set_of_clause)  # 输出生成新子句的相关信息
                    __print(new_clause)  # 输出该新子句
                    if end_or_not(new_clause, set_of_clause):  # 判断是否应该结束归结过程
                        status = False
                        break
            #  set_of_clause[i]是有多个谓词的子句
            else:  
                for j in range(0, len(set_of_clause)):  # 找可使用规则 (A,B,C,...)and(¬A,B,C,...) => (B,C,...) 的子句set_of_clause(j)
                    target = -1
                    if i != j and len(set_of_clause[i]) == len(set_of_clause[j]):
                        for k in range(len(set_of_clause[i])):
                            if set_of_clause[i][k].element == set_of_clause[j][k].element:
                                continue
                            elif set_of_clause[i][k].get_name() == set_of_clause[j][k].get_name() and set_of_clause[i][k].element[1:] == set_of_clause[j][k].element[1:]:
                                # 找到可以消去的子句
                                if target != -1:  # 表明已经存在一处不等的情况，无法使用该规则进行消除
                                    target = -1
                                    break
                                target = k
                            else:
                                target = -1
                                break
                    if target == -1:
                        continue
                    new_clause = []
                    for k in range(len(set_of_clause[i])):
                        if k != target:
                            p = Predicate("")
                            p.new(set_of_clause[j][k].element)
                            new_clause.append(p)
                    if len(new_clause) == 1:  # 判断是否生成的子句是否与已有重复（不判断是否生成了子句）
                        for k in range(len(set_of_clause)):
                            if len(set_of_clause[k]) == 1 and new_clause[0].element == set_of_clause[k][0].element:
                                target = -1
                                break
                    if target == -1:  # 如果生成的子句已存在，跳过加入子句集的过程
                        continue
                    set_of_clause.append(new_clause)
                    print_msg(target, i, j, [], [], set_of_clause)  # 输出生成新子句的相关信息
                    __print(new_clause)  # 输出该新子句
                    if end_or_not(new_clause, set_of_clause):  # 判断是否应该结束归结过程
                        status = False
                        break
    print("结束归结过程")