#friv game 
class Subject:
    def __init__(self, subject_name):
        self.subject_name = subject_name

    def __str__(self):
        return f"{self.subject_name}"


class Student:
    all_registered_subjects = []  

    def __init__(self, name):
        self.name = name
        self.registered_subjects = []

    def register_subject(self, subject):
        if subject not in self.registered_subjects:
            self.registered_subjects.append(subject)
            Student.all_registered_subjects.append(subject)  
            print(f"{self.name} has registered for {subject}.")
        # else:
        #     print(f"{self.name} is already registered for {subject}.")

    @classmethod
    def notRegSub(cls, all_subjects):
        unregistered_subjects = []
        for subject in all_subjects:
            if subject not in cls.all_registered_subjects:
                unregistered_subjects.append(subject)
        return unregistered_subjects



math = Subject("Mathematics")
science = Subject("Science")
history = Subject("History")
english = Subject("English")


all_subjects = [math, science, history, english]


student1 = Student("Alice")
student2 = Student("Bob")


student1.register_subject(math)
student1.register_subject(science)
student2.register_subject(math)


unregistered_subjects = Student.notRegSub(all_subjects)
print("\nSubjects with no registrations:")
for subject in unregistered_subjects:
    print(subject)
