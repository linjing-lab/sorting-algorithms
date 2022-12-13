import sortingx as six

data = {('Alex', 100, 90, 98, 95), ('Jack', 97, 88, 98, 92), ('Peter', 92, 95, 92, 96), ('Li', 97, 89, 98, 92)}
test = six.bubble(data, key=lambda x: (x[0], x[1]), reverse=True)
output = sorted(data, key=lambda x: (x[0], x[1]), reverse=True)
print(test, '\n', output)