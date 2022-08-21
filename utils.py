def generate(array: list, key) -> list:
    '''
    array: 同一数据维度下，支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    key: lambda函数, 仅含一个参量，用于关键字排序, 例如: key=lambda x: x[1], key=lambda x: (x[0], x[1])。
    '''
    compare = list(map(key, array)) if key != None else array
    compare = ([[value] for value in compare] if compare and compare[0] is not list else compare) if key != None else array
    return compare

def core(left: tuple or list, right: tuple or list, key, reverse: bool) -> bool:
    '''
    left: 左侧比较数组; right: 右侧比较数组; reverse: 是否逆序
    '''
    if key == None:
        return left < right if reverse else left > right
    for index in range(0, len(left)):
        if left[index] > right[index] and reverse:
            return False
        elif left[index] > right[index] and not reverse:
            return True
        elif left[index] < right[index] and reverse:
            return True
        elif left[index] < right[index] and not reverse:
            return False
    return False