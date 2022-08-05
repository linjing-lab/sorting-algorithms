# 选择排序（Selection Sort）

## 一、基本思想

选择排序(Selection-sort)是一种简单直观的排序算法。它的工作原理：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

## 二、实现逻辑

$n$ 个记录的数组可经过 $n-1$ 轮选择排序得到有序结果。

算法步骤：
1. 初始状态：无序区为 $R[1...n]$，有序区为空；
2. 第 $i$ 轮排序（$i=1,2,3,...,n-1$）开始时，当前有序区和无序区分别为 $R[1...i-1]$ 和 $R[i...n]$。该轮排序从当前无序区中选出关键字最小的记录 $R[k]$，将它与无序区的第 1 个记录 $R[i]$ 交换，使 $R[i]$ 和 $R[i+1...n]$ 分别变为记录个数增加 1 个的新有序区和记录个数减少 1 个的新无序区；
3. $n-1$ 轮结束后，数组已经有序化。

## 三、时间复杂度的分析

表现最稳定的排序算法之一，任何数据在算法中都是 $\Theta(n^2)$、$\Omega(n^2)$、$O(n^2)$。

## 四、空间复杂度的分析

不占用额外空间，故算法空间复杂度为：$O(n^2)$。

## 五、算法实现

### 普通版本

```python
def selection_sort(array: List) -> None:
    '''
    支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    '''
    length = len(array)
    for index in range(length - 1):
        mind = index # 标记最小关键字位置
        for next in range(index + 1, length): # 搜索
            if array[mind] > array[next]:
                mind = next
        array[index], array[mind] = array[mind], array[index]
```

### 标记最大值

```python
def selection_sort(array: List) -> None:
    '''
    支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    '''
    length = len(array)
    scope = length // 2
    for index in range(scope):
        mind, maxd = index, index # 从一个方向搜索来保证单调性
        for next in range(index + 1, length - index):
            if array[mind] > array[next]:
                mind = next
            if array[maxd] < array[next]:
                maxd = next
        array[mind], array[index] = array[index], array[mind]
        maxd = mind if index == maxd else maxd
        array[maxd], array[length - index - 1] = array[length - index - 1], array[maxd]
```