class Kls(object):
    def foo(self, x):
        print('executing foo(%s,%s)' % (self, x))

    @classmethod
    def class_foo(cls,x):
        print('executing class_foo(%s,%s)' % (cls,x))

    @staticmethod
    def static_foo(x):
        print('executing static_foo(%s)' % x)


ik = Kls()

# 实例方法
ik.foo(1)
print(ik.foo)
print('==========================================')

# 类方法
ik.class_foo(1)
Kls.class_foo(1)
print(ik.class_foo)
print('==========================================')

# 静态方法
ik.static_foo(1)
Kls.static_foo('hi')
print(ik.static_foo)

l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1)
l1.append(100)
l1[1].remove(55)
print('l1:', l1)  # l1: [3, [66, 44], (7, 8, 9), 100]
print('l2:', l2)  # l2: [3, [66, 44], (7, 8, 9)]
l2[1] += [33, 22]  #  对列表来说，+= 运算符就地修改列表
l2[2] += (10, 11)  #  对元组来说，+= 运算符创建一个新元组
print('l1:', l1)  # l1: [3, [66, 44, 33, 22], (7, 8, 9), 100]
print('l2:', l2)  # l2: [3, [66, 44, 33, 22], (7, 8, 9, 10, 11)]

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


pair = Pair(1,2)
print(pair)




