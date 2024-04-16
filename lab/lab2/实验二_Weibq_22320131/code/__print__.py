import re

def print_msg(key, i, j, old_name, new_name, set_of_clause):
    tmp = str(len(set_of_clause)) + ": R[" + str(i + 1)
    if len(new_name) == 0 and len(set_of_clause[i]) != 1:
        tmp = tmp + chr(key + 97)
    tmp = tmp + ", " + str(j + 1) + chr(key + 97) + "]("
    for k in range(len(old_name)):
        tmp = tmp + old_name[k] + " = " + new_name[k]
        if k < len(old_name) - 1:
            tmp = tmp + ", "
    tmp = tmp + ") = "
    print(tmp, end = "")
    
    
def __print(clause_in):  # 从谓词列表打印出原来的子句
    tmp = ""
    if len(clause_in) > 1:
        tmp = tmp + "("
    for i in range(len(clause_in)):
        tmp = tmp + clause_in[i].element[0] + "("
        for j in range(1, len(clause_in[i].element)):
            tmp = tmp + clause_in[i].element[j]
            if j < len(clause_in[i].element) - 1:
                tmp = tmp + ","
        tmp = tmp + ")"
        if i < len(clause_in) - 1:
            tmp = tmp + ","
    if len(clause_in) > 1:
        tmp = tmp + ")"
    if (tmp != ""):
        print(tmp)