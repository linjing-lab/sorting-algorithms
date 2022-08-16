# Tim排序（Tim Sort）

## 一、基本思想

Tim排序是一种混合稳定排序算法。它是由插入排序和归并排序衍生出来的混合算法。它首先使用插入排序得到子数组，这些小的排序子数组被称为自然运行（run）。然后使用归并排序堆这些运行进行合并子数组，产生最终的排序数组。它的设计考虑到算法在真实世界数据上的最佳性能。它利用了插入排序在小尺寸子数组上表现非常好的事实。它是Java的`Array.sort()`和Python的`sorted()`和`sort()`使用的标准排序算法。

## 二、实现逻辑

假设有一个包含`n`元素的无序数组`array`，将考虑运行的大小为`32`。它可以是`2`的任何幂数，因为当数字是`2`的幂数时，合并更有效。

算法主体的步骤：
1. 将数组化分为`n/32`运行；
2. 使用插入排序函数对各个运行逐一进行排序；
3. 使用归并排序的merge函数将排序后的运行逐一合并。

merge的步骤：
1. 初始化辅助数组`result`来存储排序后的输出；
2. 初始化3个指针`i`、`j`和`k`：`i`指向第一个子数组`begin`的开始，`j`指向第二个子数组`mid+1`的开始，`k`用`begin`初始化，保持排序数组`result`的当前索引；
3. 直到到达`array[begin,...,mid]`或`array[mid+1,...,end]`子数组的末尾，在索引`i`&`j`的元素中挑出一个较小的值，插入到`result`中；
4. 当其中一个数组用完后，挑选剩余的元素插入到`result`中；
5. 将`result`复制到`array[begin,...,end]`中。

## 三、时间复杂度的分析

若数组元素的个数小于`run`的话，那么直接进行插入排序，时间复杂度为：$\Omega(n)$、$\Theta(n^2)$、$O(n^2)$，如果是二分插入排序的话，时间复杂度会减小。若数组元素的个数大于`run`的话，那么由于做`run`的插入排序会与归并排序产生并列的时间复杂度，故总时间复杂度为：$\Omega(n \log_2(n))$、$\Theta(n \log_2(n))$、$O(n \log_2(n))$。

## 四、空间复杂度的分析

在下述两个算法中，并没有在主体开辟数组，但是在归并排序的过程中用到了额外的数组，故空间复杂度为：$O(n)$。

## 五、算法实现

### 无二分优化

```python
def tim_sort(array: list, run: int=32, reverse: bool=False) -> None:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    run: 运行大小, 默认是32, 最好是2的幂数。
    reverse: 是否降序, 默认采用升序。
    '''
    def inser(l: int, r: int) -> None:
        '''
        l: 数据左侧游标(整型), r: 数据右侧游标(整型)
        '''
        for index in range(l + 1, r + 1):
            key = array[index]
            pre = index - 1
            while pre >= l and (key > array[pre] if reverse else key < array[pre]):
                array[pre + 1] = array[pre]
                pre -= 1
            array[pre + 1] = key
    
    def merge(low: int, mid: int, high: int) -> None:
        '''
        low: 数据低侧游标(整型), mid: 数据中间游标(整型), high: 数据高侧游标(整型)
        '''
        left = array[low: mid]
        right = array[mid: high]
        i = 0
        j = 0
        result = []
        while i < len(left) and j < len(right):
            if (left[i] > right[j] if reverse else left[i] <= right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        array[low: high] = result
    
    # choose run
    length = len(array)
    for index in range(0, length, run):
        inser(index, min(index + run - 1, length - 1))

    # merge run
    size = run
    while size < length:
        for low in range(0, length, 2 * size):
            mid = low + size
            high = min(low + 2 * size - 1, length - 1) + 1
            merge(low, mid, high)
        size = 2 * size
```

### 有二分优化

```python
def tim_sort(array: list, run: int=32, reverse: bool=False) -> None:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    run: 运行大小, 默认是32, 最好是2的幂数。
    reverse: 是否降序, 默认采用升序。
    '''
    def inser(l: int, r: int) -> None:
        '''
        l: 数据左侧游标(整型), r: 数据右侧游标(整型)
        '''
        for index in range(l + 1, r + 1):
            key = array[index]
            low, high = l, index - 1
            while low <= high: # 符合单调性的序列
                mid = (low + high) // 2
                if (key < array[mid] if reverse else key > array[mid]):
                    low = mid + 1
                else:
                    high = mid - 1
            for pre in range(index, low, -1): # 从后往前
                array[pre] = array[pre - 1]
            array[low] = key
    
    def merge(low: int, mid: int, high: int) -> None:
        '''
        low: 数据低侧游标(整型), mid: 数据中间游标(整型), high: 数据高侧游标(整型)
        '''
        left = array[low: mid]
        right = array[mid: high]
        i = 0
        j = 0
        result = []
        while i < len(left) and j < len(right):
            if (left[i] > right[j] if reverse else left[i] <= right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        array[low: high] = result
    
    # choose run
    length = len(array)
    for index in range(0, length, run):
        inser(index, min(index + run - 1, length - 1))

    # merge run
    size = run
    while size < length:
        for low in range(0, length, 2 * size):
            mid = low + size
            high = min(low + 2 * size - 1, length - 1) + 1
            merge(low, mid, high)
        size = 2 * size
```