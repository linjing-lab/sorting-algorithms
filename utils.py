def cmp(left: tuple or list, right: tuple or list, reverse: bool) -> bool:
    '''
    left: 左侧比较数组; right: 右侧比较数组; reverse: 是否逆序
    '''
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