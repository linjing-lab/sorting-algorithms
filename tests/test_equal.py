import sortingx

data1 = [['Jack', (98, 100)], ['Bob', (98, 99)], ['Jessi', (98, 97)]]
data2 = [['Jack', (98.1, 100)], ['Bob', (98.1, 99)], ['Jessi', (98.1, 97)]]
data3 = [['Jack', (98.11, 100)], ['Bob', (98.10000000000, 99)], ['Jessi', (98.1100000000000000, 97)]]

print(sortingx.bubble(data1, key=lambda x: x[1][0], reverse=True))
print(sorted(data1, key=lambda x: x[1][0], reverse=True))