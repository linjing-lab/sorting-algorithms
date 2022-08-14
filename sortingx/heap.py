# normal
def normal(array: list, reverse: bool=False) -> None:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    reverse: 是否降序（小顶堆）, 默认采用升序（大顶堆）。
    '''
    def build(array: list, root: int, end: int) -> None:
        while 1:
            child = 2 * root + 1 # 左子节点的位置
            if child > end: # 若左子节点超过了最后一个节点，则终止循环
                break
            if (child + 1 <= end) and (array[child + 1] < array[child] if reverse else array[child + 1] > array[child]): # 若右子节点在最后一个节点之前，并且右子节点比左子节点大，则我们的孩子指针移到右子节点上
                child += 1
            if (array[child] < array[root] if reverse else array[child] > array[root]): # 若最大的孩子节点大于根节点，则交换两者顺序，并且将根节点指针，移到这个孩子节点上
                array[child], array[root] = array[root], array[child]
                root = child
            else:
                break

    length = len(array)
    for root in range(length // 2 - 1, -1, -1):
        build(array, root, length - 1)
    for end in range(length - 1, 0, -1):
        array[0], array[end] = array[end], array[0] # 交换堆顶与待排序数组末尾位置
        build(array, 0, end - 1)

# 递归
def recur(array: list, reverse: bool=False) -> None:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    reverse: 是否降序（小顶堆）, 默认采用升序（大顶堆）。
    '''
    def build(array: list, root: int, end: int) -> None:
        piv = root
        left = 2 * root + 1
        right = 2 * root + 2
        if left < end and (array[root] > array[left] if reverse else array[root] < array[left]):
            piv = left
        if right < end and (array[piv] > array[right] if reverse else array[piv] < array[right]):
            piv = right
        if piv != root:
            array[root], array[piv] = array[piv], array[root]
            build(array, piv, end)
    
    length = len(array)
    for root in range(length // 2 - 1, -1, -1):
        build(array, root, length - 1)
    for end in range(length - 1, 0, -1):
        array[0], array[end] = array[end], array[0]
        build(array, 0, end)