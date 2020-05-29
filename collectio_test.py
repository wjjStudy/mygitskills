import collections

'''
namedtuple是一个函数，它用来创建一个自定义的tuple对象，
并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
'''
print('==========namedtuple=========')
Point = collections.namedtuple('myPoint', ['x', 'y'])
Circle = collections.namedtuple('Circle', ['x', 'y', 'r'])
p = Point(1, 2)
c = Circle(45, 45, 5)
print(p.x)   # 1
print(c.r)   # 5
print(c._fields)   # ('x', 'y', 'r')

# City = collections.namedtuple('City', ['name', 'country', 'population', 'coordinates'])
# tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
# print(tokyo)
# print(tokyo.population)

'''
deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
'''
print('==========deque=========')
q = collections.deque(['a', 'b', 'c'], maxlen=4)  # maxlen ：可选参数；maxlen=4 表示队列最多有4个元素，添加第5个元素时会自动移除最老的记录
q.append('d')
print(q)  # deque(['a', 'b', 'c', 'd'], maxlen=4)
q.append('e')
print(q)  # deque(['b', 'c', 'd', 'e'], maxlen=4)
q.pop()  # e
print(q)   # deque(['b', 'c', 'd'], maxlen=4)
q.appendleft('start')
print(q)  # deque(['start', 'b', 'c', 'd'], maxlen=4)
q.appendleft('start0')
print(q)  # deque(['start0','start', 'b', 'c'], maxlen=4)
q.popleft()  # start
print(q)  # deque(['a', 'b', 'c'])  # deque(['b', 'c', 'd'], maxlen=4)



'''
使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
'''
print('==========defaultdict=========')
d = collections.defaultdict(lambda: "N/A")
d['key1'] = 1
print(d['key1'])  # 1
print(d['key2'])  # N/A

# pairs = {"b": "world", "c": 7}
# d_dict = {"a": 1, "b": "hello", "c": [3, -5, 88]}
# d_dict = collections.defaultdict(list)
# for k, v in pairs:
#     d_dict[k].append(v)
# print("d_dict", d_dict)


'''
使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序,如果要保持Key的顺序，可以用OrderedDict
注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
'''
print('==========OrderedDict=========')
od = collections.OrderedDict([('x', 1), ('z', 3), ('y', 2)])
dict1 = {'r1': 4, 's1': 5, 't1': 6}
dict2 = dict([('r2', 4), ('s2', 5), ('t2', 6)])
print(dict1)  # {'r1': 4, 's1': 5, 't1': 6}
print(dict2)
print(od.keys())  # odict_keys(['x', 'z', 'y'])


'''
Counter是一个简单的计数器，例如，统计字符出现的个数
'''
print('=========={0}========='.format("Counter"))
counter = collections.Counter()   # 获取的结果是一个空字典
s = "544455535222323333"
for i in s:
    counter[i] = counter[i] + 1
print(counter)  # Counter({'3': 6, '5': 5, '2': 4, '4': 3})

num_counter = collections.Counter(s)
print(num_counter.most_common(2))  # 出现次数最多的前2个元素及其出现次数  [('3', 6), ('5', 5)]
print(num_counter.most_common(len(s)))  # [('3', 6), ('5', 5), ('2', 4), ('4', 3)]
print(num_counter["4"])  # 3


