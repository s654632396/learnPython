# -*- coding:utf-8 -*-

range(1, 11)
# 1 - 10 的 list

L = []
for x in range(1, 11) :
    L.append(x * x)

print L

# 使用一行语句即可以生成！
print [x * x for x in range(1, 11)]

print [x * (x+1) for x in range(1, 100, 2)]

print 'hello, %s, ni %s' % ('world' , 'hao')


d = {'akarin' : 89, 'kongo' : 96, 'haruna' : 100 , 'shimakaze' : 56,}

def generate_tr(name, score) :
    if score < 60 :
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)

tds = [ generate_tr(name, score) for name, score in d.iteritems()]
print '<table>'
print '<tr><th>name</th><th>score</th></tr>'
print '\n'.join(tds)
print '</table>'

# 在加入条件筛选
print [x * x for x in range(1, 11) if x % 2 == 0]

# 编写一个函数， 接受一个list
# 然后吧list 中的所有字符串都变成大写后返回， 非字符串忽略
# isinstance(x, str) 可以判断x是否是字符串

def uc_str(l) :
    L = []
    L = [x.upper() for x in l if isinstance(x, str)]
    return L
print uc_str(['hello', 'world', 101])

# for 可以嵌套，因此在列表生成中，也可以用多层for来生成
print [m + n for m in 'ABCD' for n in '123456']

print [m*100+n*10+o for m in range(1,10) for n in range(1,10) for o in range(1, 10) if m == o]












