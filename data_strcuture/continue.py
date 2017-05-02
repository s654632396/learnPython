# -*- coding:utf-8 -*-

L = [75,98, 59, 81, 66, 43, 69, 85]
sum = 0.0
for score in L :
    sum += score
print sum / len(L)

sum = 0
n = 0
for score in L :
    if score < 60 :
        continue
    sum += score
    n += 1
print sum / n
