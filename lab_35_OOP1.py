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

# students_list1 = ["Alice", "Bob", "Charlie", "David"]
# students_list2 = ["Eve", "Frank", "Grace", "Hannah"]

# student_group = StudentGroup(students_list1, students_list2)

# student_group.pair_students()

# student_group.print_group_members()







class Subject:
    def __init__(self, subject_name, subject_code):
        self.subject_name = subject_name
        self.subject_code = subject_code

    def __str__(self):
        return f"{self.subject_name} ({self.subject_code})"


class Student:
    all_registered_subjects = [] 

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.registered_subjects = []

    def register_subject(self, subject):
        if subject not in self.registered_subjects:
            self.registered_subjects.append(subject)
            Student.all_registered_subjects.append(subject)  
            print(f"{self.name} has registered for {subject}.")
        else:
            print(f"{self.name} is already registered for {subject}.")

    @classmethod
    def notRegSub(cls, all_subjects):
        unregistered_subjects = []
        for subject in all_subjects:
            if subject not in cls.all_registered_subjects:
                unregistered_subjects.append(subject)
        return unregistered_subjects


math = Subject("Mathematics", "MATH101")
science = Subject("Science", "SCI101")
history = Subject("History", "HIST101")
english = Subject("English", "ENG101")

all_subjects = [math, science, history, english]


student1 = Student("Alice", "S001")
student2 = Student("Bob", "S002")


student1.register_subject(math)
student1.register_subject(science)
student2.register_subject(math) 


unregistered_subjects = Student.notRegSub(all_subjects)
print("Subjects with no registrations:")
for subject in unregistered_subjects:
    print(subject)
    
