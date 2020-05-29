#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import json
question_list = [[1, 2], [3, 4], [5, 6]]
new_list = [a for inside in question_list for a in inside]
# print(new_list)   # output: [1, 2, 3, 4, 5, 6]
my_list = []
for inside in question_list:
    for number in inside:
        print(number)
        my_list.append(number)
print(my_list)

dict1 = {"A": 1, "B": 2 , "C":3}
print(dict1.items())  # output : dict_items([('A', 1), ('B', 2), ('C', 3)])
result_dic = {v: k for k, v in dict1.items()}
print(result_dic)    # output : {1: 'A', 2: 'B', 3: 'C'}
print(json.dumps(dict1))  # 字典转换成json字符串
print(type(json.dumps(dict1)))  # output : str
json_str = '{"A": 1, "B": 2 , "C":3}'
print(json.loads(json_str))  # json字符串转换成字典
print(type(json.loads(json_str)))  # output : dict

dict2 = {"blana": 1, "apple": 23 , "orange":3, "egg": 33}
print(sorted(dict2))  # sorted方法对可迭代的序列排序生成新的序列
aList = ['Google', 'Runoob', 'Taobao', 'Facebook']
aList.sort()   # 使用sort()方法对list排序会修改list本身,不会返回新list(实际返回none),  sort()不能对dict字典进行排序
print("List : ", aList)  # output  List :  ['Facebook', 'Google', 'Runoob', 'Taobao']

list1 = [1, 2, 3]
list2 = [3, 4, 5]
set1 = set(list1)
set2 = set(list2)
print(set1 & set2)  # 取交集  为啥不能直接用列表需要转换成集合？
print(set1 ^ set2)  # 取并集

print("=============closure==============")


def function_outside():
    msg = 'Hello'
    my_list = []
    aa = "outter  hello"

    def function_inside():
        for i in range(5):
            # nonlocal my_list
            aa = "inner hello"
            my_list.append(i)
        print("inner fun list :", my_list)
        print("inner aa :", aa)
        return msg

    function_inside()
    print("outter fun list :", my_list)
    print("outter aa :", aa)
    return function_inside


# my_function = function_outside()
function_outside()
# print(my_function.__closure__)   # (<cell at 0x000002806C34C918: str object at 0x000002806C21E3B0>,)
# print(my_function.__closure__[1].cell_contents)  # Hello

print("============")


def add_sum(*args):
    print("*args", *args)   # 1 2 3
    print("args", args)     # (1, 2, 3)
    print(sum(args))


for i in range(-1, -5, -1):
    print("i= ", i)

for j in range(1, 5):
    print(-j)

