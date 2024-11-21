
class Employee:
    all_members=[]
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
        self.groupmembers=None
        Employee.all_members.append(self)
    def __repr__(self):
        return f'{self.name}--{self.salary}'    
    def set_members(self,other_member):
        if (self.groupmembers==None):
            other_member.groupmembers=self
        self.groupmembers=other_member
        other_member.groupmembers=self
    def remaining_members(cls):
        return list(filter(lambda x:x.groupmembers==None,cls.allmembers))

# emp1=Employee('Ali',50000)
# emp2=Employee('Ahmad',60000)
# emp3=Employee('abbas',70000)
# emp4=Employee('waa',65000)
# print(emp1.groupmembers)
# print(emp2.groupmembers)
# emp1.set_members(emp2)
# print(emp1.groupmembers)
# print(emp2.all_members)

class StudentGroup:
    def __init__(self, students_list1, students_list2):
        self.students_list1 = students_list1
        self.students_list2 = students_list2
        self.group_members = {}

    def pair_students(self):
        for i in range(len(self.students_list1)):
            self.group_members[self.students_list1[i]] = self.students_list2[i]

    def print_group_members(self):
        for student in self.students_list1:
            print(f"{student} is paired with {self.group_members[student]}")

students_list1 = ["hamza", "ali", "ahmad", "davoo"]
students_list2 = ["mahad", "zafar", "hanan", "jafar"]

student_group = StudentGroup(students_list1, students_list2)

student_group.pair_students()

student_group.print_group_members()