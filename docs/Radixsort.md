# 基数排序（Radix Sort）

## 一、基本思想

基数排序是一种非比较型**整数**排序算法，是桶排序的扩展。基本思想是：取得所有数的数位并统一为相同的长度，数位较短的数字前面补零。从低位开始排序，分别放入0~9个队列中，然后采用先进先出的原则进行收集；在按照高位排序，然后在收集；依次类推，直到最高位，最终得到排好序的数列。对于数值偏小的一组序列，该算法速度非常快，时间复杂度可以达到线性。

## 二、实现逻辑

该算法的核心在对数字按位数从低到高进行排序。

算法步骤：
1. 取得数组中的最大数并取得位数；
2. 对数位较短的数进行前面补零；
3. 从个位开始分配，根据位值（0~9）分别放在（0~9）号桶中；
4. 收集数据放在（0~9）号桶中的数据按顺序放到数组中；
5. 重复3~4过程，直到最高位，即可完成排序。

## 三、时间复杂度的分析

## 四、空间复杂度的分析

## 五、算法实现

### 按低位排序

```python
def radix_sort(array: List[int], reverse: bool=False) -> List[int]:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    reverse: 是否降序, 默认采用升序。
    '''
    numbers = len(str(max(array))) # note the length of the biggest num
    for step in range(numbers):
        container = [[] for _ in range(10)] # 0~9
        for value in array:
            pos = value // (10 ** step) % 10
            container[9 - pos if reverse else pos].append(value) # 取个位
        array.clear()
        array = [value for index in container for value in index]
    return array
```

### 按高位排序

```python
def radix_sort(array: List[int], radix: int=6, reverse: bool=False) -> List[int]:
    '''
    array: 支持数值型数据，如整型与浮点型混合；支持全为字符串类型的数据；不支持字符串型与数值型混合。
    radix: 基数大小, 最好取用最大数的位数
    reverse: 是否降序, 默认采用升序。
    '''
    container, num, k = [[] for _ in range(10)], [0] * 10, pow(10, radix - 1)
    for value in array:
        pos = value // k % 10
        container[pos].append(value)
        num[pos] += 1 # 计数器
    array.clear()
    for index in range(10):
        if num[index] == 1:
            array.append(container[index][0]) # 退出
        elif num[index] > 1:
            con = msd(container[index], radix - 1)
            array.extend(con)
    if reverse:
        array.reverse()
    return array
```