# coding=utf-8

import math

class pheap(object):

    def __init__(self):
        # heap_data = self.generate(data)
        self.heap_data = None

    def generate(self, data=None):
        pass

    def append(self, item):
        if self.heap_data == None:
            self.heap_data = [item,]
            return self
        else:
            self.heap_data.append(item)
            nodeindex = len(self.heap_data) + 1

            pnode = self._getpnode(nodeindex)

    def _getpnode(self, node):
        if node == 1:
            return None
        else:
            itdepth = self.depth(node)
            pnode = int(math.pow(2, itdepth - 2) + (node - math.pow(2, itdepth - 1))// 2)
            return self.heap_data[pnode]

    def depth(self, cindex):
        lv = int(math.log(cindex, 2)) + 1
        return lv


    def pop(self):
        pass

    def find(self, item):
        return

    def dumptree(self):
        pass

def next(cindex):
    #           1
    #    2            3
    #   4    5      6     7
    #  8 9 10 11  12 13 14 15

    lv = int(math.log(cindex, 2)) + 1


if __name__ == '__main__':
    test = pheap()
    test._getpnode(12)


