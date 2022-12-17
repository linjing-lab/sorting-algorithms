from operator import attrgetter
import sortingx as six

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = (
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
)

test = six.merge(student_objects, key=lambda student: student.age)
output = sorted(student_objects, key=lambda student: student.age)
print(test, '\n', output)

# reference: https://docs.python.org/3/howto/sorting.html