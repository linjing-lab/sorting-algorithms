from operator import attrgetter
import sortingx as six
# reference: https://docs.python.org/3/howto/sorting.html

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = (
    Student('Joo', 'A', 15),
    Student('Jack', 'B', 12),
    Student('Peter', 'B', 10),
)

output = sorted(student_objects, key=attrgetter('grade', 'age'))
test = six.merge(student_objects, key=attrgetter('grade', 'age'))
print(test, '\n', output)