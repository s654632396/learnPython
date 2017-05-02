# coding=utf-8

import random

start = random.randint(0, 100)

while True:
    try :
        guess = int(raw_input('Enter 1~100:'))
    except ValueError, e:
        guess = int(raw_input('please retry enter 1~100:'))

    if guess > start:
        print 'guess bigger:', guess
    elif guess < start:
        print 'guess smaller:', guess
    else:
        print 'you guess right ,game clear!'
        break
    print '\n'
