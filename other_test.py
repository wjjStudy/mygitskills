import heapq
import bisect
import random
import operator
import itertools
'''
heapq:在集合中找出最大或者最小的N个元素
'''
print('==========heapq=========')
nums = [2, -4, 44, 5, 65, -55, 45]
heapq.heapify(nums)
print(nums)  # [-55, -4, 2, 5, 65, 44, 45]  堆的顺序排列？？
print(heapq.nlargest(2, nums))  # [65, 45]
print(heapq.nsmallest(3, nums))  # [-55, -4, 2]
print(sorted(nums))
print(sorted(nums)[5:])
print(sorted(nums)[-5:])
prices = {
    "apple": 45.23,
    "pillow": 2.05,
    "potato": 22.36,
    "egg": 1.01,
    "meat": 12.56
}
print(zip(prices.values(), prices.keys()))   # <zip object at 0x0000022EFF1E20C8>
print(min(zip(prices.values(), prices.keys())))   # (1.01, 'egg')
print(min(prices.values()))  # 1.01
print(min(prices))  # apple
print(min(prices, key=lambda k: prices[k]))  # egg
print(max(zip(prices.values(), prices.keys())))   # (45.23, 'apple')
print(max(zip(prices.keys(), prices.values())))   # ('potato', 22.36)

print('==========bisect.insort=========')
nums1 = [1, 5, 6, 8, 12, 44, 65]
for i in range(5):
    new_num = random.randint(1, 100)
    bisect.insort(nums1, new_num)   # 在保持原nums1的大小排列顺序不变的情况下，插入新元素
    print(new_num, "--->", nums1)

print('==========sorted=========')
dict1 = {'a': 2, 'e': 3, 'f': 8, 'd': 4}
dict2 = sorted(dict1)
print("dict2: ", dict2)  # ['a', 'd', 'e', 'f']
dict22 = sorted(dict1.keys())
print("dict22: ", dict22)  # ['a', 'd', 'e', 'f']
dict3 = sorted(dict1, key=lambda k: dict1[k])
print("dict3: ", dict3)  # ['a', 'e', 'd', 'f']
dict33 = sorted(dict1.items(), key=lambda k: k[1])
print("dict33: ", dict33)  # [('a', 2), ('e', 3), ('d', 4), ('f', 8)]
dict333 = sorted(dict1.items(), key=lambda k: k[0])
print("dict333: ", dict333)  # [('a', 2), ('d', 4), ('e', 3), ('f', 8)]
dict4 = sorted(dict1.items(), key=operator.itemgetter(1))
print("dict4: ", dict4)   # [('a', 2), ('e', 3), ('d', 4), ('f', 8)]
# dict44 = sorted(dict1:dict1[k], key=operator.itemgetter(1))
# print("dict44: ", dict44)   # [('a', 2), ('e', 3), ('d', 4), ('f', 8)]


print("========== str.casefold() ========")
str1 = "WORLD"
print(str1.casefold())

print("==========itemgetter ========")
'''
itemgetter:根据元组或者列表的某个字段给元 组列表排序
'''

metro_data = [('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
              ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
              ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
              ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
              ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))]

metro_data2 = (['Tokyo', 'JP', 36.933, (35.689722, 139.691667)],
              ['Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)],
              ['Mexico City', 'MX', 20.142, (19.433333, -99.133333)],
              ['New York-Newark', 'US', 20.104, (40.808611, -74.020386)],
              ['Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)])
# for city in sorted(metro_data2, key=operator.itemgetter(0)):
#     print(city)
# print(sorted(metro_data2, key=operator.itemgetter(0)))

my_dic = {"aplle": 4.5, "balana": 5.99, "orange": 2.77, "egg": 4.75, "meat": 10.44, "potato": 7.43}
print("价格由高到低排列")
dic1SortList = sorted(my_dic.items(), key=lambda x: x[1], reverse=True)  # result： [('meat', 10.44), ('potato', 7.43), ('balana', 5.99), ('egg', 4.75), ('aplle', 4.5), ('orange', 2.77)]
my_dicSorted = sorted(my_dic.items(), key=operator.itemgetter(1))  # result：[('orange', 2.77), ('aplle', 4.5), ('egg', 4.75), ('balana', 5.99), ('potato', 7.43), ('meat', 10.44)]
print(dic1SortList)
print(my_dicSorted)
for item in my_dic.items():
    print(item)

my_dic2 = [{'name': 'aplle', 'price': 4.5}, {'name': 'balana', 'price': 5.99}, {'name': 'orange', "price": 2.77},
           {'name': 'egg', "price": 7.43}, {'name': 'meat', "price": 6.43}]
print("价格由低到高排列")
for product in sorted(my_dic2, key=operator.itemgetter("price")):
    print(product)

alist = [{'name': 'a', 'age': 20}, {'name': 'b', 'age': 30}, {'name': 'c', 'age': 25}]


def sort_by_age(list1):
    return sorted(alist, key=lambda x: x['age'], reverse=True)
print("sort_by_age结果： ",sort_by_age(alist))
print("operator.itemgetter结果： ", sorted(alist, key=operator.itemgetter("age"), reverse=True))
print("==========iter and  generator ========")

ll = (i for i in range(8))
print(type(ll))
print(next(ll))


def fun():
    for i in range(9):
        yield i
        print("第{}次取值".format(i))


# for j in fun():
#     print(j)
gen = fun()
print(gen)  # <generator object fun at 0x000001AF7231C408>
print(next(gen))  # 0
print(next(gen))  # 第0次取值  1

print("==========itertools========")

# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC', 'XYZ'):
    print(c)  # 迭代效果：'A' 'B' 'C' 'X' 'Y' 'Z'

print(itertools.chain('ABC', 'XYZ'))  # <itertools.chain object at 0x0000014EA4672E10>


