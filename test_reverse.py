# 导包
from typing import List
import sortingx

# 测试
class Reverser:
    def __init__(self, genre: str, method: List[str], part: List[bool]=None, ret: List[bool]=None):
        '''
        genre: 类型名称; method: 方法列表; part: 方法是否含参数l与r; ret: 函数是否有返回值
        '''
        if part != None:
            assert len(part) == len(method)
        if ret != None:
            assert len(ret) == len(method)
        self.method = 'sortingx.' + genre
        self.call = method # genre.def
        self.part = part
        self.ret = ret

    def __data(self):
        with open('./data/test.txt', 'rt', encoding='utf-8') as fout:
            strings = fout.readlines()
            self.data = [string.strip('\n') for string in strings]
        self.testing = [self.data for _ in range(len(self.call))]

    def __compare(self, func, index, nopart, noret):
        '''
        比较函数。
        '''
        self.count = 0
        for value in self.testing[index]:
            value = eval(value)
            result = sorted(value, reverse=True)
            if nopart and noret:
                func(value, reverse=True)
                self.count += (value == result)
            if not nopart and noret:
                func(value, 0, len(value) - 1, reverse=True)
                self.count += (value == result)
            if nopart and not noret:
                value = func(value, reverse=True)
                self.count += (value == result)
            if not nopart and not noret:
                value = func(value, 0, len(value) - 1, reverse=True)
                self.count += (value == result)

    def collect(self) -> str:
        '''
        收集测试结果。
        '''
        self.success = 0
        self.__data()
        for index, value in enumerate(self.call):
            func = eval(self.method + '.' + value)
            nopart = self.part == None or self.part[index] == False
            noret = self.ret == None or self.ret[index] == False
            self.__compare(func, index, nopart, noret)
            if self.count == len(self.data):
                self.success += 1
        return 'The Design of Reverse of ' + self.method + ' Is Correct!' if self.success == len(self.call) else 'Error!'

# 测试实例1
'''
Bubble = Reverser('bubble', ['normal', 'flag', 'bidirect'])
print(Bubble.collect())
'''

# 测试实例2
'''
Counting = Reverser('counting', ['whilediv', 'forenum', 'reverfill'], ret=[False, False, True])
print(Counting.collect())
'''

# 测试实例3
'''
Bucket = Reverser('bucket', ['numeric', 'mobase'])
print(Bucket.collect())
'''

# 测试实例4
'''
Insertion = Reverser('insertion', ['direct', 'binary'])
print(Insertion.collect())
'''

# 测试实例5
'''
Merge = Reverser('merge', ['recur', 'stack'], ret=[True, False])
print(Merge.collect())
'''

# 测试实例6
'''
Quick = Reverser('quick', ['lamb', 'recur', 'stack'], part=[False, True, True], ret=[True, False, False])
print(Quick.collect())
'''

# 测试实例7
'''
Selection = Reverser('selection', ['normal', 'withmax'])
print(Selection.collect())
'''

# 测试实例8
'''
Shell = Reverser('shell', ['donald', 'knuth', 'hibbard', 'sedgewick'])
print(Shell.collect())
'''

# 测试实例9
'''
Radix = Reverser('radix', ['lsd', 'msd'], ret=[True, True])
print(Radix.collect())
'''

# 测试实例10
'''
Heap = Reverser('heap', ['normal', 'recur'])
print(Heap.collect())
'''

# 测试实例11
'''
Tim = Reverser('tim', ['normal', 'binary'])
print(Tim.collect())
'''

# 测试实例12
'''
Tree = Reverser('tree', ['tree'], ret=[True])
print(Tree.collect())
'''