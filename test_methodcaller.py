import math
import sortingx
from operator import methodcaller

class Point:
	def __init__(self, a, b, c, d):
		self.a = a
		self.b = b
		self.c = c
		self.d = d
	def __repr__(self):
		return 'Point({!r:},{!r:},{!r:},{!r:})'.format(self.a, self.b, self.c, self.d)
	def __lt__(self, other):
		return (self.a < other.a if self.a != other.a else (self.b < other.b if self.b != other.b else (self.c < other.c if self.c != other.c else self.d < other.d)))
	def __le__(self, other):
		return (self.a, self.b, self.c, self.d) <= (other.a, other.b, other.c, other.d)
	def __gt__(self, other):
		return (self.a > other.a if self.a != other.a else (self.b > other.b if self.b != other.b else (self.c > other.c if self.c != other.c else self.d > other.d)))
	def __ge__(self, other):
		return (self.a, self.b, self.c, self.d) >= (other.a, other.b, other.c, other.d)
	def __eq__(self, other):
		return self.a == other.a and self.b == other.b and self.c == other.c and self.d == other.d
	def distance(self, a, b, c, d):
		return math.hypot(self.a - a, self.b - b, self.c - c, self.d - d)

points = [
	Point(1, 2, 3, 4),
	Point(1, -1, 1, -1),
	Point(3, 0, -2, 1),
	Point(2, -2, 3, 2),
	Point(-1, 2, 0, 1),
	Point(1, 1, 1, 1),
	Point(-2, -1, -3, 0),
	Point(2, 0, 1, 1),
	Point(1, -3, -2, -1)
]

print(sortingx.heap(points, key=methodcaller('distance', 0, 0, 0, 0)))
# print(sortingx.insert(points))
# print(sortingx.insert(points, reverse=True))