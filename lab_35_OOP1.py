#friv game 
class Subject:
    def __init__(self, sub_name):
        self.sub_name = sub_name

    def __str__(self):
        return f"{self.sub_name}"


class Student:
    all_reg_subs = []  

    def __init__(self, name):
        self.name = name
        self.reg_subs = []

    def reg_sub(self, subject):
        if subject not in self.reg_subs:
            self.reg_subs.append(subject)
            Student.all_reg_subs.append(subject)  
            print(f"{self.name} has registered for {subject}.")
        else:
            print(f"{self.name} is already registered for {subject}.")

    @classmethod
    def notRegSub(cls, all_subjects):
        un_reg_subs = []
        for subject in all_subjects:
            if subject not in cls.all_reg_subs:
                un_reg_subs.append(subject)
        return un_reg_subs

math = Subject("Mathematics")
science = Subject("Science")
history = Subject("History")
english = Subject("English")
chemistry=Subject("Chemistry")

all_subjects = [math, science, history, english,chemistry]


student1 = Student("Alice")
student2 = Student("Bob")


student1.reg_sub(math)
student1.reg_sub(science)
student1.reg_sub(science)
student2.reg_sub(math)


un_reg_subs = Student.notRegSub(all_subjects)
print("\nSubjects with no registrations:")
for subject in un_reg_subs:
    print(subject)
