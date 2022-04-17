# 递归实现
def Recursion(array):
    def merge_sort(array):
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        left = merge_sort(array[:mid])
        right = merge_sort(array[mid:])
        return merge(left, right)

    def merge(l, r):
        result = []
        i = 0
        j = 0
        while i < len(l) and j < len(r):
            if(l[i] <= r[j]):
                result.append(l[i])
                i += 1
            else:
                result.append(r[j])
                j += 1
        result += l[i:]
        result += r[j:]
        return result
    return merge_sort(array)

# 非递归实现
def Stack(array):
    def merge(array, low, mid, high):
        left = array[low: mid]
        right = array[mid: high]
        i = 0
        j = 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        array[low: high] = result

    def merge_sort(array):
        i = 1
        while i < len(array):
            low = 0
            while low < len(array):
                mid = low + i
                high = min(low + 2 * i, len(array))
                if mid < high:
                    merge(array, low, mid, high)
                low += 2 * i
            i *= 2
    merge_sort(array)