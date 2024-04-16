class Predicate:  # 我们先定义一个谓词类来对子句中的谓词进行存储
    element = []

    def __init__(self, str_in):
        self.element = []
        if len(str_in) != 0:
            if str_in[0] == ',':  # 把原来用于分隔谓词的 , 去掉
                str_in = str_in[1:]
            tmp = ""
            for i in range(len(str_in)):
                tmp += str_in[i]
                if str_in[i] == '(' or str_in[i] == ',' or str_in[i] == ')':
                    self.element.append(tmp[0:-1])
                    tmp = ""

    def new(self, list_in):
        for i in range(len(list_in)):
            self.element.append(list_in[i])

    def rename(self, old_name, new_name):
        for i in range(len(old_name)):
            j = 1
            while j < len(self.element):
                if self.element[j] == old_name[i]:
                    self.element[j] = new_name[i]
                j = j + 1

    def get_pre(self):  # 返回谓词的前缀是否为"¬"
        return self.element[0][0] == "¬"

    def get_name(self):  # 返回谓词名称
        if self.get_pre():
            return self.element[0][1: ]
        else:
            return self.element[0]