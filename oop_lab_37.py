import math
import random

class MechaStudent:
    'This class defines a Student for Mechatronics Department'
    _department = 'Mechatronics'
    _offSubjects = ['Mech', 'LA', 'ES', 'CP-II', 'MOM', 'Proj']
    _allStudents = []

    def __init__(self, fName, lName, reg):
        self.fName = fName
        self.lName = lName
        self.reg = reg
        self.email = f'{self.reg.lower()}@uet.edu.pk'
        self._courses = ['Proj']
        self._groupMember = None
        self.fullName = f'{self.fName} {self.lName}'
        MechaStudent._allStudents.append(self)

    ## Getters and Setters
    @property
    def fullName(self):
        return f'{self.fName} {self.lName}'

    @fullName.setter
    def fullName(self, newname):
        f, l = newname.split(' ')
        self.fName = f
        self.lName = l
        self._fullName = newname

    @property
    def fName(self):
        return self._fName

    @fName.setter
    def fName(self, newname):
        if MechaStudent.validName(newname):
            self._fName = newname
        else:
            raise ValueError('Name should contain alphabet only and at least 2 of those!')

    @property
    def lName(self):
        return self._lName

    @lName.setter
    def lName(self, newname):
        if MechaStudent.validName(newname):
            self._lName = newname
        else:
            raise ValueError('Name should contain alphabet only and at least 2 of those!')

    @property
    def reg(self):
        return self._reg

    @reg.setter
    def reg(self, newreg):
        if isinstance(newreg, str) and str(newreg).startswith('MCT-UET-'):
            self._reg = newreg
        else:
            raise ValueError('Reg must start as MCT-UET-')

    ## Static Methods ##
    @staticmethod
    def validName(name):
        return isinstance(name, str) and len(name) >= 2 and name.isalpha()

    ## Instance Methods ##
    def registerSubject(self, *sub):
        for s in sub:
            if s not in MechaStudent._offSubjects:
                raise ValueError(f'{s} is not offered!')
            if s in MechaStudent._offSubjects and s not in self._courses:
                self._courses.append(s)

    ## Class Methods ##
    @classmethod
    def notRegSub(cls):
        a = set()
        for std in cls._allStudents:
            s = set(std._courses)
            a.update(s)
        return list(set(cls._offSubjects).difference(a))

    @classmethod
    def withoutGroupMembers(cls):
        return list(filter(lambda s: s._groupMember is None, cls._allStudents))

    ## Magic Methods ##
    def __repr__(self):
        return f'{self.lName}-{self.reg[-2:]}'

    def __add__(self, other):
        if self._groupMember is not None:
            raise ValueError(f'{self} already has {self._groupMember} as group member')
        elif other._groupMember is not None:
            raise ValueError(f'{other} already has {other._groupMember} as group member')
        else:
            self._groupMember = other
            other._groupMember = self

    def __sub__(self, other):
        if self._groupMember is None and other._groupMember is None:
            return
        elif self._groupMember != other:
            raise ValueError(f'{self} is not group member of {other}.')
        else:
            self._groupMember = None
            other._groupMember = None

    def __lt__(self, other):
        return len(self) < len(other)

    def __eq__(self, other):
        return len(self) == len(other)

    def __len__(self):
        return len(self._courses)

    def __iter__(self):
        yield self.fName
        yield self.lName
        yield self.reg
        for c in self._courses:
            yield c

# Create MechaStudent instances
std1 = MechaStudent('Anwar', 'Ali', 'MCT-UET-01')
std2 = MechaStudent('Akbar', 'Khan', 'MCT-UET-02')
std3 = MechaStudent('Asad', 'Shabir', 'MCT-UET-03')
std4 = MechaStudent('Faisal', 'Iqbal', 'MCT-UET-04')

# Register subjects for each student
std1.registerSubject('CP-II', 'Mech', 'MOM')
std2.registerSubject('ES', 'Mech', 'MOM')
std3.registerSubject('ES', 'LA', 'MOM', 'Mech')
std4.registerSubject('LA', 'Mech', 'MOM')

# Perform student operations
std1 + std2  # Will print Akbar Khan-MCT-UET-02 
std3 + std4
print(std1._groupMember)

# This should generate errors as specified
# std1 + std3
# std1 - std3

# Sort and print all students
MechaStudent._allStudents.sort()
print(MechaStudent._allStudents)
# Will Print [Anwar Ali-MCT-UET-01, Akbar Khan-MCT-UET-02, Faisal Iqbal-MCT-UET-04, Asad Shabir-MCT-UET-03]

# Point class with required features
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Point):
            self.x += other.x
            self.y += other.y
            return self
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __isub__(self, other):
        if isinstance(other, Point):
            self.x -= other.x
            self.y -= other.y
            return self
        return NotImplemented

    def __truediv__(self, number):
        if isinstance(number, (int, float)):
            return Point(self.x / number, self.y / number)
        return NotImplemented

    def __eq__(self, other):
        return abs(self) == abs(other)

    def __ne__(self, other):
        return abs(self) != abs(other)

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __le__(self, other):
        return abs(self) <= abs(other)

    def __gt__(self, other):
        return abs(self) > abs(other)

    def __ge__(self, other):
        return abs(self) >= abs(other)

    def __iter__(self):
        yield self.x
        yield self.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Main Program
# Create a list of 10 random points
points = [Point(random.randint(-5, 5), random.randint(-5, 5)) for _ in range(10)]

# Filter out points with magnitude between 2 and 3 (inclusive)
filtered_points = [point for point in points if 2 <= abs(point) <= 3]

# Print original and filtered points
print("Original points:")
for point in points:
    print(point)

print("\nFiltered points with magnitude between 2 and 3:")
for point in filtered_points:
    print(point)
