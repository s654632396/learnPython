# -*- coding:utf-8 -*-

N = 10
x = 0
while x < N :
    print x
    x += 1


x = 1
sum = 0
while x < 100:
    if 0 != x % 2:
        sum += x
    x += 1
print sum

sum = 0
x = 1
while True :
    sum += x
    x += 1
    if x > 100 :
        break
print sum

sum = 0
x = 1
counter = 0
while True :
    sum += x
    x *= 2
    counter += 1
    if counter >= 20:
        break
print sum
