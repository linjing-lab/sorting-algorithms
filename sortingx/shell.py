# Donald Shell
def donald(array: list, reverse: bool=False) -> None:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    reverse: 是否降序, 默认采用升序。
    '''
    length = len(array)
    gap = length // 2 # set gap
    print(gap)
    while gap >= 1:
        for index in range(gap, length):
            next = index
            print(next - gap)
            while next >= gap and array[next - gap] < array[next] if reverse else array[next - gap] > array[next]: # insertion sort
                array[next], array[next - gap] = array[next - gap], array[next]
                next -= gap
        gap //= 2 # renew

# knuth
def knuth(array: list, reverse: bool=False) -> None:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    reverse: 是否降序, 默认采用升序。
    '''
    length = len(array)
    gap = 1
    while gap < length / 3:
        gap = int(3 * gap + 1)
    while gap >= 1:
        for index in range(gap, length):
            next = index
            while next >= gap and array[next - gap] < array[next] if reverse else array[next - gap] > array[next]:
                array[next], array[next - gap] = array[next - gap], array[next]
                next -= gap
        gap = int(gap / 3)

# Hibbard增量序列
def hibbard(array: list, reverse: bool=False) -> None:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    reverse: 是否降序, 默认采用升序。
    '''
    length, index, sequence = len(array), 1, []
    value = (1 << index) - 1
    while value <= length:
        sequence.append(value)
        index += 1
        value = (1 << index) - 1
    for gap in reversed(sequence):
        for index in range(gap, length):
            next = index
            while next >= gap and array[next - gap] < array[next] if reverse else array[next - gap] > array[next]:
                array[next], array[next - gap] = array[next - gap], array[next]
                next -= gap   

# Sedgewick增量序列
def sedgewick(array: list, reverse: bool=False) -> None:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    reverse: 是否降序, 默认采用升序。
    '''
    length, index, sequence = len(array), 0, []
    pre, nex = 9 * ((1 << 2 * index) - (1 << index)) + 1, (1 << 2 * index + 4) - 3 * (1 << index + 2) + 1
    while pre <= length or nex <= length:
        sequence.append(pre)
        sequence.append(nex)
        index += 1
        pre, nex = 9 * ((1 << 2 * index) - (1 << index)) + 1, (1 << 2 * index + 4) - 3 * (1 << index + 2) + 1
    for gap in reversed(sequence):
        for index in range(gap, length):
            next = index
            while next >= gap and array[next - gap] < array[next] if reverse else array[next - gap] > array[next]:
                array[next], array[next - gap] = array[next - gap], array[next]
                next -= gap