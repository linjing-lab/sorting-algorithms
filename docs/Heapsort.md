# 堆排序（Heap Sort）

## 一、基本思想

堆排序是利用堆这种数据结构而设计的一种稳定排序算法，是一种选择排序。堆具有以下性质：每个结点的值都大于或等于其左右孩子结点的值，称为大顶堆；或者每个结点的值都小于或等于其左右孩子结点的值，称为小顶堆。基本思路是：将一个无序序列调整为一个堆，能找出序列中的最大值（或最小值），然后将找出的这个元素与末尾元素交换，所有有序序列元素就增加一个，无序序列元素就减少一个，堆新的无序序列重复操作，从而实现排序。

## 二、实现逻辑

堆排序的核心在于构造大顶堆（或小顶堆），并对元素不断地进行交换。

算法步骤：
1. 构造初始堆：将给定无序序列构造成一个大顶堆（一般升序采用大顶堆，降序采用小顶堆）；
2. 将堆顶元素与末尾元素进行交换，使末尾元素最大，然后继续调整堆，再将堆顶元素与末尾元素交换，得到第二大元素；
3. 重新调整结构，使其满足堆定义，然后继续交换堆顶元素与当前末尾元素；
4. 如此反复进行交换、重建、交换，直到整个序列有序。

## 三、时间复杂度的分析

建堆的过程是在树结构上进行更新迭代操作，所以`build`方法时间复杂度为：$\Omega(\log_2(n))$、$\Theta(\log_2(n))$、$O(\log_2(n))$。算法主体外部遍历元素大小为 $n$ 的数组，故时间复杂度为：$\Omega(n\log_2(n))$、$\Theta(n\log_2(n))$、$O(n\log_2(n))$。

## 四、空间复杂度的分析

由于算法不需要开辟额外的存储记录的空间，所有算法的空间复杂度为：$O(1)$。

## 五、算法实现

### 非递归版本

```python
def heap_sort(array: list, reverse: bool=False) -> None:
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
```

### 递归版本

```python
def heap_sort(array: list, reverse: bool=False) -> None:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    reverse: 是否降序（小顶堆）, 默认采用升序（大顶堆）。
    '''
    def build(array: list, root: int, end: int) -> None:
        piv = root # 根据reverse
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
        build(array, 0, end - 1)
```