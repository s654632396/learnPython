# coding=utf-8 

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print heapq.nlargest(3, nums)
print heapq.nsmallest(3, nums)

profiles = [
    {'name': 'IBM', 'shares': 100, 'prices': 91.1},
    {'name': 'AAPL', 'shares': 50, 'prices': 543.22},
    {'name': 'FB', 'shares': 200, 'prices': 21.09},
    {'name': 'HPQ', 'shares': 35, 'prices': 31.75},
    {'name': 'YHOO', 'shares': 45, 'prices': 16.35},
    {'name': 'ACME', 'shares': 75, 'prices': 115.64},
]

cheaps = heapq.nsmallest(3, profiles, key=lambda x: x['prices'])
print cheaps

expensives = heapq.nlargest(3, profiles, key=lambda x: x['prices'])
print expensives
