#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os
import xlrd
import xlwt
import math
import re


def get_file_list(file_dir):
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if not file.endswith('.xlsx'):
                files.remove(file)
        return files


def split_xlsx(file_abs_name, num):


    '''
    :param file_abs_name: 要拆分的excel文件绝对名称
    :param num: 要拆分的小的excel中的行数
    :return: none
    '''

    print("=======现在拆分的表格是：{}=======".format(file_abs_name))
    data = xlrd.open_workbook(file_abs_name)  # 获取excel对象
    sheet_names = data.sheet_names()  # 获取所有sheet名称
    print("所有sheet名称: ", data.sheet_names())
    for sheet_name in sheet_names:
        if sheet_name in file_abs_name:
            spy_sheet = data.sheet_by_name(sheet_name)  # 获取指定名称的sheet对象
            nrows = spy_sheet.nrows   # 数据行数总数,包含表头
            print('sheet"{0}"的总行数是{1}'.format(sheet_name, nrows - 1))  # 总数不包含表头
            file_count = math.ceil((nrows-1) / num)
            last_count = (nrows-1) - num * (file_count - 1)  # 最后一个文件的行数，不包含表头
            print("最后一个文件有{}行".format(last_count))
            print('要把excel分割成每个{0}行,总共会拆分成{1}个'.format(num, file_count))

            for j in range(file_count):  # 要拆分的第j+1个文件
                book = xlwt.Workbook(encoding='utf-8')
                com = re.compile(r'^\d+')
                file_name2 = com.sub(str(num), file_name)
                new_file_name = os.path.join(os.path.dirname(file_abs_name), file_name2.split('.')[0] + '_' + str(j+1) + '.xlsx')
                for one_sheet in sheet_names:
                    book.add_sheet(one_sheet)   # 每个子表格创建各个sheet
                new_sheet1 = book.get_sheet(sheet_name)  # 获取有数据的一个同名sheet
                myRowValues = spy_sheet.row_values(0)  # 获取第一行表头的内容，列表
                for k in range(len(myRowValues)):  # 是第几列，从0开始
                    new_sheet1.write(0, k, myRowValues[k])  # 先写第一行表头的内容
                if j != file_count - 1:
                    for i in range(num):  # i是第几行，从0开始
                        myRowValues = spy_sheet.row_values(j*num+i+1)  # 获取第i+1行的数据,一行的数据是一个列表(第一行，i=0)
                        print("第{0}行的数据是{1}".format(i+1, myRowValues))
                        for k in range(len(myRowValues)):  # k是第几列，从0开始,逐个单元格写入内容
                            new_sheet1.write(i+1, k, myRowValues[k])
                else:
                    for i in range(last_count):  # i 是第几行，从0开始
                        myRowValues = spy_sheet.row_values(j*num+i+1)  # 获取第i+1行的数据,一行的数据是一个列表(第一行，i=0)
                        print("第{0}行的数据是{1}".format(i+1, myRowValues))
                        for k in range(len(myRowValues)):  # k是第几列，从0开始
                            new_sheet1.write(i+1, k, myRowValues[k])

                book.save(new_file_name)  # 保存Excel
                print("第{}个分割好了".format(j + 1), '\n')

            print("=======表格{}拆分结束=======".format(file_abs_name))


if __name__ == '__main__':
    file_dir = r'C:\wanjiaojiao_vendor\桌面\性能测试\视频源导入\split_test'
    file_list = get_file_list(file_dir)
    num = 6  # 要拆分的小的excel中的行数

    for file_name in file_list:
        # print("file_name: ", file_name)
        file_abs_name = os.path.join(file_dir, file_name)
        split_xlsx(file_abs_name, num)
        print('\n')
