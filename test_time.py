# 导包
import sortingx
import time
import polars as pl
import random

# 测试函数
class Timer:
    def __init__(self, genre: str, method: list, part: bool=False):
        '''
        genre: 类型名称; method: 方法列表; part: 分区控制;
        '''
        self.method = 'sortingx.' + genre
        self.call = method # genre.def
        self.part = part # 分区 l, r
        self.dict = {} # 训练日志

    def generate(self, left: int=0, right: int=100, size: int=10000, seed: int=0) -> str:
        '''
        left: 数值范围左限, 默认值为0; right: 数值范围右限, 默认值为100; size: 数据大小, 默认值为10000; seed: 随机数种子, 默认值为0
        '''
        if seed != None:
            random.seed(seed)
        self.data = [random.randint(left, right) for _ in range(size)]
        self.testing = [self.data for _ in range(len(self.call))]
        return 'The Test Data Is Generated!'
    
    def collect(self) -> str:
        '''
        函数运行时间收集
        '''
        for index, value in enumerate(self.call):
            func = eval(self.method + '.' + value)
            if not self.part:
                times = time.time()
                func(self.testing[index])
                timee = time.time()
            else:
                times = time.time()
                func(self.testing[index], 0, len(self.data) - 1)
                timee = time.time()
            gap = round(timee-times, 3)
            self.dict[value] = [gap]
        return 'The Process of Collection Is Over!'
    
    def ouput(self) -> str:
        '''
        测试日志
        '''
        return 'The Time Record of {0} is: \n{1}'.format(self.method, pl.DataFrame(self.dict))

Counting = Timer('counting', ['whilediv', 'forenum', 'reverfill'])
print(Counting.generate(0, 100, 10000, 1))
print(Counting.collect())
print(Counting.ouput())