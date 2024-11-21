
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


# Set group memberships for corresponding students
# Verify the results by printing group members of the first list


class Student:
    all_members = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.groupmembers = None
        Student.all_members.append(self)
        def __repr__(self):
            return f'{self.name}--{self.age}'
        def set_members(self, other_member):
            if (self.groupmembers == None):
                other_member.groupmembers = self
                self.groupmembers = other_member

# Create two lists of students at least 10
list1 = [Student('Ali', 20), Student('Ahmad', 21), Student('huss',22),Student('nasir',19)]
list2 = [Student('Ali', 20), Student('Ahmad', 21), Student('huss',22),Student('nasir',19)]


