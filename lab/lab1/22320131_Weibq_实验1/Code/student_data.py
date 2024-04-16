import os

class StuData:
    def __init__(self, file_name):
        self.data = []
        
        with open(file_name, 'r') as student:
            for line in student:
                one_of_student = line.strip().split()
                age = int(one_of_student[3])
                student_new = [one_of_student[0], one_of_student[1], one_of_student[2], age]
                self.data.append(student_new)
                
    def AddData(self, name, stu_num, gender, age):
        new_stu_data = [name, stu_num, gender, age]
        self.data.append(new_stu_data)
        
    def SortData(self, form__):
        if form__ == 'name':
            self.data.sort(key=lambda x: x[0])
        elif form__ == 'stu_num':
            self.data.sort(key=lambda x: x[1])
        elif form__ == 'gender':
            self.data.sort(key=lambda x: x[2])
        elif form__ == 'age':
            self.data.sort(key=lambda x: int(x[3]))
            
    def ExportFile(self, out_file):
        with open(out_file, 'w') as outfile:
            for student in self.data:
                outfile.write(f"{student[0]} {student[1]} {student[2]} {student[3]}\n")

# 测试样例
data = StuData('student_data.txt')
data.AddData(name = 'weibaiqiang', stu_num = '22320131', gender = 'M', age = 19)
data.SortData('gender')
data.ExportFile('new_stu_data.txt')
