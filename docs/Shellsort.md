# 希尔排序（Shell Sort）

## 一、基本思想

希尔排序是插入排序的一种，也称缩小增量排序，是直接插入排序算法的一种更高效的改进版本。希尔排序是非稳定的排序算法，是记录按下标的一定增量分组，对每组使用直接插入排序算法排序；随着增量逐渐减少，每组包含的关键字越来越多，当增量减至1时，整个文件恰被分成一组。插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率。

## 二、实现步骤

在插入排序中提高效率，通过增大移动的步幅来提高效率。在插入排序中，每次增大移动一大步从而快速将元素移动到其应该所在大致位置。

算法步骤：
1. 将整个有 $n$ 个元素的数组序列分割成 $gap(gap=n/2)$ 个子序列，第 $1$ 个数据和第 $n/2 + 1$ 个数据分为一组；
2. 一次循环中，在每个子序列中分别采用直接插入排序；
3. 然后缩小间隔 $gap$，即 $gap=gap/2$，然后变为 $n/gap$ 个子序列，重复上述的子序列划分和排序工作；
4. 不断重复上述过程，随着序列减少最后变为一个，即完成了整个排序

## 三、时间复杂度的分析

由于不断折半步长，时间复杂度从三层循环中产生，故平均、最坏时间复杂度为：$\Theta(n(\log_2(n))^2)$、$O(n(\log_2(n))^2)$。当最后一层循环恰好不需要进行元素交换，即各分组恰好符合排序要求，则最好时间复杂度为：$\Omega(n \log_2(n))$。

## 四、空间复杂度的分析

就Donald提出的希尔排序算法而言，空间复杂度是：$O(1)$。

## 五、算法实现

### Donald Shell

```python
def shell_sort(array: list, reverse: bool=False) -> None:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    reverse: 是否降序, 默认采用升序。
    '''
    length = len(array)
    gap = length // 2 # set gap
    while gap >= 1:
        for index in range(gap, length):
            next = index
            while next >= gap and array[next - gap] < array[next] if reverse else array[next - gap] > array[next]: # insertion sort
                array[next], array[next - gap] = array[next - gap], array[next]
                next -= gap
        gap //= 2 # renew
```

### Knuth增量序列

```python
def shell_sort(array: list, reverse: bool=False) -> None:
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
```

### Hibbard增量序列

Hibbard增量序列的取法为：$D_k=2^k-1$。

```python
def shell_sort(array: list, reverse: bool=False) -> None:
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
```

### Sedgewick增量序列

Sedgewick增量序列的取法为： $D_k=9 \cdot 4^i-9 \cdot 2^i + 1$ 或 $4^i - 3 \cdot 2^i + 1$。

```python
def shell_sort(array: list, reverse: bool=False) -> None:
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
```