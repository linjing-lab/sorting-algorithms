# 直接插入
def direct(array):
    for index in range(1, len(array)):
        key = array[index]
        pre = index - 1
        while pre >= 0 and key < array[pre]:
            array[pre + 1] = array[pre]
            pre -= 1
        array[pre + 1] = key

# 折半插入
def binary(array):
    for index in range(1, len(array)):
        key = array[index]
        low, high = 0, index - 1
        while low <= high: # 符合单调性的序列
            mid = (low + high) // 2
            if key > array[mid]:
                low = mid + 1
            else:
                high = mid - 1
        for pre in range(index, low, -1): # 从后往前
            array[pre] = array[pre - 1]
        array[low] = key 