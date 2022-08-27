from keyword_sorting import bubble_sort, heap_sort, insertion_sort, shell_sort

'''
We choose from the following keyword lambda functions:
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
heap_sort(data, key=lambda x: (x[1], x[2]), reverse=False)
print(data)

'''
reverse=False: 
[('Peter', 92, 95, 92, 96), ('Jack', 97, 88, 98, 92), ('Li', 97, 89, 98, 92), ('Alex', 100, 90, 98, 95)]

reverse=True: 
[('Alex', 100, 90, 98, 95), ('Li', 97, 89, 98, 92), ('Jack', 97, 88, 98, 92), ('Peter', 92, 95, 92, 96)]
'''

data = [('Alex', 100, 90, 98, 95), ('Jack', 97, 88, 98, 92), ('Peter', 92, 95, 92, 96), ('Li', 97, 89, 98, 92)]
heap_sort(data, key=lambda x: x[2], reverse=False)
print(data)

'''
reverse=False:
[('Jack', 97, 88, 98, 92), ('Li', 97, 89, 98, 92), ('Alex', 100, 90, 98, 95), ('Peter', 92, 95, 92, 96)]

reverse=True:
[('Peter', 92, 95, 92, 96), ('Alex', 100, 90, 98, 95), ('Li', 97, 89, 98, 92), ('Jack', 97, 88, 98, 92)]
'''

data = ['Lin', 'Min', 'Max', 'Jack']
heap_sort(data, key=str.lower, reverse=False)
print(data)

'''
reverse=False:
['Jack', 'Lin', 'Max', 'Min']

reverse=True:
['Min', 'Max', 'Lin', 'Jack']
'''