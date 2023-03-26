import sortingx

with open('./data/test.txt', 'rt', encoding='utf-8') as fout:
    strings = fout.readlines()
    data = [string.strip('\n') for string in strings]

for value in data:
    print(sortingx.heap(eval(value)))