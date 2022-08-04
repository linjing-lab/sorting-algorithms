# 快速排序（Quick Sort）

## 一、基本思想

通过一趟排序将待排记录分割成独立的两部分，其中一部分记录的关键字均比另一部分的关键字小，则可分别对这两部分记录继续进行排序，以达到整个序列有序。

## 二、实现逻辑

快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分成两个子序列（sub-lists）。

算法步骤：

1. 选定Pivot中心轴；
2. 将大于Pivot的数字放在Pivot的右边；
3. 将小于Pivot的数字放在Pivot的左边；
4. 分别对左右子序列重复前三步操作，直到各子序列中的元素个数为1。

## 三、时间复杂度的分析

递归算法的时间复杂度公式：$T[n]=aT[n/b] + f(n)$

快速排序的最优情况是每一次取到的元素都刚好平分整个数组。此时时间复杂度的公式则为：$T[n]=2T[n/2]+f(n)$，$T[n/2]$为平分后的子数组的时间复杂度，$f(n)$为平分这个数组所花的时间。

下面来推算一下，在**最优的情况**下快速排序时间复杂度的计算：

第一次递归：$T[n] = 2T[n/2] + n$；

令：$n = n/2$，则有：$T[n]=2\{2 \ T[n/4] + (n/2)\} + n = 2^2 T[n / (2^2)] + 2n$

令：$n = n / (2^2)$，则有：$T[n] = 2^3 T[n/(2^3)]+3n$

若m次递归结束，则令：$n=n/(2^{m-1})$，有：$T[n]=2^{m} T[1] + mn$

于是得到：$T[n/(2^m)]=T[1]$，则有：$n=2^m$，即：$m=\log_2(n)$。

故有：$T[n] = 2^{\log_2(n)} T[1] + n \log_2(n)$，其中$n$为元素个数，当$n \geq 2$时，$n \log_2(n) \geq n$，所以取后面的$n\log_2(n)$；

综上所述：快速排序最优情况下时间复杂度为：$\Omega(n \log_2(n))$。

在**平均的情况**下，设枢轴的关键字应该在第$k$的位置（$1 \leq k \leq n$），那么：

$$
T[n]=\frac{1}{n} \sum_{k=1}^{n}(T[k-1] + T[n-k]) + n = \frac{2}{n} \sum_{k=1}^{n} T[k] +n 
$$

由数学归纳法可知，其数量级为$\Theta(n \log_2(n))$。

当我们选取的枢纽每次都是**最大元素**时，就是**最差**情况，待排序的序列为正序或者逆序，每次划分只得到一个比上一次划分少一个记录的子序列，注意另一个为空。如果递归树画出来，它就是一棵斜树。此时需要执行$n‐1$次递归调用，且第 $i$ 次划分需要经过 $n‐i$ 次关键字的比较才能找到第 $i$ 个记录，是枢轴的位置，因此比较次数为：

$$
\sum_{i=1}^{n-1} = (n-1) + (n-2) + + ... + 1 = \frac{n(n-1)}{2}
$$

于是时间复杂度为：$O(n^2)$。

## 四、空间复杂度的分析

递归造成的栈空间的使用，最好情况，递归树的深度为 $\log_2n$，其空间复杂度也就为 $\Omega(\log(n))$；最坏情况，需要进行$n‐1$递归调用，其空间复杂度为 $O(n)$；平均情况，空间复杂度也为$\Theta(\log(n))$。

由于关键字的比较和交换是跳跃进行的，因此，快速排序是一种不稳定的排序方法。

## 五、算法实现

### 一行实现

```python
quick_sort = lambda array: array if len(array) <= 1 else quick_sort([item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])
```

### 递归实现

```python
def quick_sort(array, l, r):
    if l < r:
        mid = partition(array, l, r)
        quick_sort(array, l, mid - 1)
        quick_sort(array, mid + 1, r)

def partition(array, l, r):
    value = array[r]
    index = l - 1
    for ind in range(l, r):
        if array[ind] <= value:
            index += 1
            array[index], array[ind] = array[ind], array[index]
    array[index + 1], array[r] = array[r], array[index + 1]
    return index + 1
```

### 非递归实现

```python
def quick_sort(array, l, r):
	if l >= r:
		return
	stack = []
	stack.append(l)
	stack.append(r)
	while stack:
		low = stack.pop(0)
		high = stack.pop(0)
		if high - low <= 0:
			continue
		value = array[high]
		index = low - 1
		for ind in range(low, high):
			if array[ind] <= value:
				index += 1
				array[index], array[ind] = array[ind], array[index]
		array[index + 1], array[high] = array[high], array[index + 1]
		stack.extend([low, index, index+2, high])
```