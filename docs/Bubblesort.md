# 冒泡排序（Bubble Sort）

## 一、基本思想

冒泡排序是所有排序算法中最简单的一个。它是一种基于**比较排序**的算法，这个算法主要的排序思想就是比较每一对相邻的元素，如果它们的顺序不对，就交换它们，最终所有元素达到有序的状态。

## 二、实现逻辑

首先有一个数组，里面存放着待排序的元素。若需要把比较大的元素排到后面，把小的元素排到前面，那么需要从头到尾开始下面的比较操作：

1. 从头部开始比较相邻的两个元素，如果头部的元素比后面的大，就交换两个元素的位置；
2. 往后对每个相邻的元素都做这样的比较、交换操作，这样到数组尾部时，第一个元素会成为最小的元素；
3. 除已排好序的元素之外的，重新从头部开始第1、2步的操作；
4. 继续对越来越少的数据进行比较、交换操作，直到没有可比较的数据为止，排序完成。

**外循环遍历，内循环比较元素**。

## 三、时间复杂度的分析

最坏情况下，序列是逆序的，需要比较的次数为 $n(n-1)/2$（$n$ 个数据元素最多存在$\frac{n(n-1)}{2}$ 对逆序），则对应的时间复杂度是：$O(n^2)$。

最优情况下，序列已经排好序，只需要比较 $n-1$ 次即可退出外循环，即时间复杂度为 $\Omega(n^2)$。

对于 $n$ 个元素来说共有 $n!$ 种不同的序列，平均下来每个序列要存在 $\frac{n(n-1)}{4}$ 对逆序，所以冒泡排序平均时间复杂度是 $\Theta(n^2)$ 。

## 四、空间时间复杂度的分析

由于比较交换元素并不开辟额外的内存的空间，故有空间复杂度为：$O(1)$。

## 五、算法实现

### 普通版本

```python
def bubble_sort(array: List) -> None:
    '''
    原址排序：支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    '''
    for i in range(len(array) - 1): # loop to access each array element
        for j in range(len(array) - i - 1): # loop to compare array elements
        # compare two adjacent elements and change > to < to sort in descending order
            if array[j] > array[j + 1]:
                # swapping elements if elements are not in the intended order
                array[j], array[j + 1] = array[j + 1], array[j]
```

### 添加"旗帜"

```python
def bubble_sort(array: List) -> None:
    '''
    原址排序：支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    '''
    for i in range(len(array) - 1):
        flag = False # 旗帜
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True
        if not flag:
            break
```

### 双向排序

```python
def bubble_sort(array: List) -> None:
    '''
    原址排序：支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    '''
    for i in range(len(array) - 1):
        flag = False
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True
        if flag: # 反向排序
            flag = False
            for j in range(len(array) - i - 2, 0, -1):  
                if array[j - 1] > array[j]:
                    array[j], array[j - 1] = array[j - 1], array[j]
                    flag = True
        if not flag:
            break
```