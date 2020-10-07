import math

def qiuShuGen(num):
    # print("本次求树根传入的参数num为：",num)
    num_size= len(str(num))
    # print("num_size=",num_size)
    sum=0
    for i in range(num_size):
        sum = round(sum+round( num//(math.pow( 10, i)))%10)
        # print("i=",i,"sum=",sum)
    if sum<10:
        print(num,"的最终数根为",sum)
    else:
        # print("sum最后为",sum)
        print(num, "的本次数根为", sum)
        qiuShuGen(sum)


if __name__ == '__main__':
    while True:
        input_num = input("请输入正整数：")
        if input_num.isdigit():
            qiuShuGen(int(input_num))
            break
        else:
            print("输入内容不正确!")








