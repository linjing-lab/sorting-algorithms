from regex import D


def Doubleloop(array):
      # loop to access each array element
  for i in range(len(array) - 1):
    # loop to compare array elements
    for j in range(len(array) - i - 1):
      # compare two adjacent elements and change > to < to sort in descending order
      if array[j] > array[j + 1]:
        # swapping elements if elements are not in the intended order
        array[j], array[j+1] = array[j+1], array[j]

def Flag(array):
    for i in range(len(array) - 1):
        flag = False # 旗帜
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True
        if not flag:
            break

def Bidirection(array):
    for i in range(len(array) - 1):
        flag = False
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True
        if flag: # 反向排序
            flag = False
            for j in range(len(array) - 2 - i, 0, -1):  
                if array[j - 1] > array[j]:
                    array[j], array[j - 1] = array[j - 1], array[j]
                    flag = True
        if not flag:
            break