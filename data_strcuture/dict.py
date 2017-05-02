# -*- coding:utf-8 -*-

# python 的 dict
# list 和 tuple 可以用来表示有序集合
# dist 则是专门描述键值对的集合

d = {
    'akarin' : 14,
    'haruna' : 19,
    'kongo' : 20,
}
print d
print len(d)

d['shimakaze'] = 13

print d

if 'kongo' in d :
    # print d['kongo']
    print d.get('kongo')

print d.get('yukikaze')

# dict的特点是查询快，无序，且key无重复，但是吃内存
# list则是查找慢，有序，但是占用内存小
# list不能作为dict的key使用，因为dict的key必须是不可变化的，如string/int/float等数据类型, Tuple可以做key
test = {
    '123' : [1, 3,34],
    123 : '123',
    ('11', '2') : True,
    #[1, 3] : False # TypeError: unhashable type: 'list'
}

print test