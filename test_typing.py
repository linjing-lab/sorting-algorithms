import sortingx as six

data = {'Alex': 100, 'Jack': 97,  'Peter': 88, 'Li': 98}
print(type(data))
test = sorted(data, reverse=True)
output = six.merge(data, reverse=True)
print(output, '\n', output == test)