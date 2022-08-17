def cmp(left: tuple or list, right: tuple or list, reverse: bool) -> bool:
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