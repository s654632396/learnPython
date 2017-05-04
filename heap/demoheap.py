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
            self.heap_data = [item, ]
            return self
        else:
            self.heap_data.append(item)
            nodeindex = len(self.heap_data) - 1
            while True:
                if nodeindex == 0: break
                pnode,pnodeindex = self._getpnode(nodeindex + 1)
                if pnode > item:
                    self._interchange(nodeindex, pnodeindex)
                    nodeindex = pnodeindex
                else:
                    break

    def _interchange(self, pindex, nindex):
        self.heap_data[pindex],self.heap_data[nindex] = self.heap_data[nindex],self.heap_data[pindex]


    def _getpnode(self, node):
        if node == 1:
            return None
        else:
            itdepth = self.depth(node)
            pnode = int(math.pow(2, itdepth - 2) + (node - math.pow(2, itdepth - 1)) // 2)
            return self.heap_data[pnode - 1], (pnode - 1)

    def depth(self, cindex):
        lv = int(math.log(cindex, 2)) + 1
        return lv

    def pop(self):
        pass

    def find(self, item):
        return

    def dumptree(self):
        if self.heap_data == None or len(self.heap_data) == 0:
            return None
        depth = 1
        maxdepth = self.depth(len(self.heap_data))

        while maxdepth >= depth:
            start, end = int(math.pow(2, depth - 1) - 1),int(math.pow(2, depth-1) - 1 + math.pow(2, depth -1))
            print self.heap_data[start:end]
            depth += 1


def next(cindex):
    #           1
    #    2            3
    #   4    5      6     7
    #  8 9 10 11  12 13 14 15

    lv = int(math.log(cindex, 2)) + 1


if __name__ == '__main__':
    test = pheap()
    l = [12, 23, 53, 22, 44, 125, 1, 4, 66, 32, 122, 223, 34, 42, 66, 77, 563]
    for item in l:
        test.append(item)
    test.dumptree()
    # print test.heap_data
