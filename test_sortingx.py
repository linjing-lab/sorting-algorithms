import sortingx

with open('./data/test.txt', 'rt', encoding='utf-8') as fout:
    strings = fout.readlines()
    data = [string.strip('\n') for string in strings]

for value in data:
    input_ = eval(value)
    print(input_, sortingx.heap(input_))