# 计数排序（Counting Sort）

## 一、基本思想

计数排序不是基于比较的排序算法，其核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。 作为一种线性时间复杂度的排序，计数排序**要求输入的数据必须是有确定范围的整数**。它的基本思想是：给定的输入序列中的每一个元素 $x$，确定该序列中值小于等于 $x$ 元素的个数，然后将 $x$ 直接存放到最终的排序序列的正确位置上。

## 二、实现逻辑

由于用来计数的数组`count`的长度取决于待排序数组中数据的范围（等于待排序数组的最大值与最小值的差加上1），这使得计数排序对于数据范围很大的数组，需要大量时间和内存。计数排序是用来排序0到100之间的数字的最好的算法，但是它不适合按字母顺序排序人名。

算法步骤：
1. 找出待排序的数组种最大和最小的元素；
2. 统计数组中每个值为 $i$ 的元素出现的次数，存入数组`count`的第 $i$ 项；
3. 对所有的计数累加（从`count`中的第一个元素开始，每一项和前一项相加），为了直接求得元素的位置；
4. 反向填充目标数组：将每个元素 $i$ 放在新数组的第`count[i]`项，每放一个元素就将`count[i]`减去1。

## 三、时间复杂度的分析

遍历数组进行计数操作产生了 $\Omega(n)$、$O(n)$、$\Theta(n)$的时间复杂度，对计数数组进行前缀和操作产生了 $\Omega(k)$、$O(k)$、$\Theta(k)$的时间复杂度，进行反向填充操作同样产生了 $\Omega(n)$、$O(n)$、$\Theta(n)$的时间复杂度。综上所述：$\Omega(n+k)$、$O(n+k)$、$\Theta(n+k)$，$n$ 前常数可以忽略。

## 四、空间复杂度的分析

由于额外开辟了大小为`k = max(array) - min(array) + 1`的数组，所以空间复杂度为：$O(k)$。在算法实现中开辟了另外一个用于存储记录的列表`result`。

## 五、算法实现

### while循环（Whiledivide）

```python
def counting_sort(array: List[int]):
    arrmin = min(array)
    arrmax = max(array)
    count = [0] * (arrmax - arrmin + 1)
    for value in array:
        count[value - arrmin] += 1
    pos = 0 # 游标
    for index in range(arrmin, arrmax + 1): # 从最小的数开始
        while count[index - arrmin] >= 1:
            array[pos] = index
            count[index - arrmin] -= 1
            pos += 1
```

### enumerate函数（Forenumerate）

```python
def counting_sort(array: List[int]):
    arrmin = min(array)
    arrmax = max(array)
    count = [0] * (arrmax - arrmin + 1)
    for value in array:
        count[value - arrmin] += 1
    array.clear()
    for index, val in enumerate(count):
        for _ in range(val):
            array.append(index + arrmin)
```

### 反向填充（Reversefill）

反向填充是为了维持排序算法的稳定性：

```python
def counting_sort(array: List[int]):
    arrmin = min(array)
    arrmax = max(array)
    count = [0] * (arrmax - arrmin + 1)
    result = [0] * len(array)
    for value in array:
        count[value - arrmin] += 1
    for index in range(1, arrmax - arrmin + 1):
        count[index] += count[index - 1]
    for index in range(len(array) - 1, -1, -1):
        result[count[array[index] - arrmin] - 1] = array[index]
        count[array[index] - arrmin] -= 1
    return result
```