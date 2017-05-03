# coding=utf-8

"""
collections是python内置的一个集合模块，提供了许多的集合类
"""

# namedtuple 命名元祖
from collections import namedtuple, deque, defaultdict, OrderedDict, Counter
Point = namedtuple('Point', ['x', 'y', 'z'])
p = Point(100, 200, 140)
print p.__doc__
print p.x, p.y, p.z
print isinstance(p, Point)
print isinstance(p, tuple)
print p._asdict()
print isinstance(p._asdict(), dict)

"""
使用list存储数据时，按照index访问元素效率很高，但是插入和删除元素效率低
因为list是线性存储，数据量大的时候，插入和删除效率低
deque是为了高效实现插入和删除操作的双向链表，适合用于队列和栈
"""
q = deque(['a', 'b', 'c'])

q.append('x')
q.appendleft('y')
print q
print q.pop()
print q.popleft()

"""
使用dict的时候，如果引用的key不存在，则会抛出 KeyError
如果希望key不存在时，返回一个默认值，可以使用defaultdict
"""

dd = defaultdict(lambda : 'N/A')
dd['key1'] = 'test'
print dd['key1']
print dd['key2']

"""
使用dict时，key是无序的
在对dict做迭代时，我们无法确定Key的顺序
如果要保持Key的顺序，可使用 OrderedDict
"""

d = dict([('x', 1), ('y', 2), ('z', 3),])
print d
od = OrderedDict([('x', 1), ('y', 2), ('z', 3),])
print od

# OrderedDict 可以实现一个 先进先出(FIFO) 的 dict
# 当容量超出了限制的时候，先删除最早添加的key
class FIFODict(OrderedDict):
    def __init__(self, capacity):
        super(FIFODict, self).__init__()
        self._capacity = capacity   # 限制

    def __setitem__(self, k, v):
        containsKey = 1 if k in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print 'remove :[', last ,']'
        if containsKey:
            del self[k]
            print 'update:', (k, v)
        else:
            print 'add:', (k, v)

        OrderedDict.__setitem__(self, k, v)


fd = FIFODict(4)
fd['k1'] = 'a'
fd['k2'] = 'b'
fd['k3'] = 'c'
fd['k4'] = 'd'
fd['k5'] = 'e'
fd['k3'] = 'c3'
print fd

"""
Counter 是一个简单计数器
"""

c = Counter()
for char in 'how to learn python programming' :
    c[char] += 1

print c





