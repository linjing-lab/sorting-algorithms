from keyword_sorting import bubble_sort, heap_sort, insertion_sort, shell_sort, quick_sort, merge_sort
import sortingx as six

'''
Choose from underlined lambda functions:
1. one keyword
lambda x: x[0]

2. two keywords
lambda x: (x[0], x[1])

3. str keyword
lambda x=str.lower

4. no keyword (all True compare.)
None
'''

data = [('Alex', 100, 90, 98, 95), ('Jack', 97, 88, 98, 92), ('Peter', 92, 95, 92, 96), ('Li', 97, 89, 98, 92)]
six.bubble(data, key=lambda x: (x[1], x[2]), reverse=True)
print(data)

'''
reverse=False: 
[('Peter', 92, 95, 92, 96), ('Jack', 97, 88, 98, 92), ('Li', 97, 89, 98, 92), ('Alex', 100, 90, 98, 95)]

reverse=True: 
[('Alex', 100, 90, 98, 95), ('Li', 97, 89, 98, 92), ('Jack', 97, 88, 98, 92), ('Peter', 92, 95, 92, 96)]
'''

data = [('Alex', 100, 90, 98, 95), ('Jack', 97, 88, 98, 92), ('Peter', 92, 95, 92, 96), ('Li', 97, 89, 98, 92)]
quick_sort(data, 0, 3, key=lambda x: x[2], reverse=True)
print(data)

'''
reverse=False:
[('Jack', 97, 88, 98, 92), ('Li', 97, 89, 98, 92), ('Alex', 100, 90, 98, 95), ('Peter', 92, 95, 92, 96)]

reverse=True:
[('Peter', 92, 95, 92, 96), ('Alex', 100, 90, 98, 95), ('Li', 97, 89, 98, 92), ('Jack', 97, 88, 98, 92)]
'''

data = ['Lin', 'Min', 'Max', 'Jack']
quick_sort(data, 0, 3, key=str.lower, reverse=True)
print(data)

'''
reverse=False:
['Jack', 'Lin', 'Max', 'Min']

reverse=True:
['Min', 'Max', 'Lin', 'Jack']
'''