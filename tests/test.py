import random
import sortingx as six

data = [[random.randint(0, 10) for _ in range(1000)] for _ in range(10000)]
test = sorted(data, key=lambda x : (x[1], x[2], x[3]), reverse=True)
six.bubble(data, lambda x : (x[1], x[2], x[3]), reverse=True)
print(data == test)