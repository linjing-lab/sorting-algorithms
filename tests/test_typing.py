import sortingx as six

data = (('Alex', 100, 90, 98, 95), ('Jack', 97, 88, 98, 92), ('Peter', 92, 95, 92, 96), ('Li', 97, 89, 98, 92))
print(six.bubble(data, key=lambda x: (x[1], x[2]), reverse=False))
# sorted(data, key=lambda x: (x[1], x[2]), reverse=False)
print(data)