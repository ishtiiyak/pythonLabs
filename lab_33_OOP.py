
class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
        self.groupmembers=None
    def __repr__(self):
        return f'{self.name}--{self.salary}'    
    def set_members(self,other_member):
        self.groupmembers=other_member

emp1=Employee('Ali',50000)
emp2=Employee('Ahmad',60000)
print(emp1.groupmembers)
print(emp2.groupmembers)
emp1.set_members(emp2)
print(emp1.groupmembers)
print(emp2.groupmembers)
