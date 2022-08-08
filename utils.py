def cmp(array1: tuple or list, array2: tuple or list, reverse: bool) -> bool:
    for index in range(0, len(array1)):
        if array1[index] > array2[index] and reverse:
            return False
        elif array1[index] > array2[index] and not reverse:
            return True
        elif array1[index] < array2[index] and reverse:
            return True
        elif array1[index] < array2[index] and not reverse:
            return False
    return False