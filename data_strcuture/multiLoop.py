# -*- coding:utf-8 -*-
for y in ['1', '2', '3']:
    for x in ['A', 'B', 'C']:
        print x + y

nine = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in nine :
    for y in nine :
        if x < y :
            print x * 10 + y