# -*- coding: UTF-8 -*-
__author__  = 'Kevin'

# # Hello World
# print('Hello World')

# #数字求和
# num1 = input("第一个数字是: ")
# num2 = input("第二个数字是: ")
# sum = float(num1) + float(num2)
# print("你输入的数字和为: {}".format(sum))

# #平方根
# import cmath
# import math
# yournumber = float(input('你输入的数字是: '))
# if yournumber >= 0:
#     print('你输入的数字平方根为: {}'.format(math.sqrt(yournumber)))
# else:
#     comp = cmath.sqrt(yournumber)
#     print('你输入的数字平方根为: {} + {}j'.format(comp.real, comp.imag))

# #二次方程: ax**2 + bx + c = 0
# import cmath
#
# a = float(input('a: '))
# b = float(input('b: '))
# c = float(input('c: '))
#
# delta = b ** 2 - 4 * a * c
#
# sol1= (- b - cmath.sqrt(delta) / (2 * a))
# sol2= (- b + cmath.sqrt(delta) / (2 * a))
#
# print("answer for this function is : \n solution1: {} and solution2: {}".format(sol1, sol2))

#三角形的面积
# import math
# try:
#     a = float(input('a: '))
#     b = float(input('b: '))
#     c = float(input('c: '))
#
#     sp = (a + b + c) / 2 #semi_perimeter
#
#     area = math.sqrt(sp * (sp - a) * (sp - b) * (sp - c))
#
#     print(area)
# except:
#     print("这三边不构成三角形!")

# #求圆的面积
# import math
# def findArea(r):
#     area = math.pi * r ** 2
#     return area
# print("圆的面积为: {}".format(findArea(6)))

# #生成随机数
# import random
#
# print(random.randint(0, 10))

# #摄氏度转华氏度
# def CtoF():
#     c = float(input("输入摄氏度: "))
#     f = (c * 1.8) + 32
#     print("{}℃对应的华氏度为: {}℉".format(c, f))
#     return
#
# print(CtoF())

# #交换变量
# x = int(input('输入x: '))
# y = int(input('输入y: '))
#
# temp = x
# x = y
# y = temp
#
# print('交换后 \n x: {} \n y: {}'.format(x, y))

# #if 判断数字是正负或者0
# def judge(x):
#     x = int(x)
#     if x > 0:
#         print("x is a positive number.")
#     elif x < 0:
#         print("x is a negative number.")
#     else:
#         print("x equal to 0.")
#     return
#
# print(judge(56))

# #判断字符串是否为数字
# def is_number(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         pass
#
#     try:
#         import unicodedata
#         for i in s:
#             unicodedata.numeric(i)
#         return True
#     except (TypeError, ValueError):
#         pass
#
#     return False
#
# print(is_number("五六七"))

# # 判断奇偶数
# def oddoreven(x):
#     x = int(x)
#     if x % 2 == 0:
#         print('This number is a even.')
#     else:
#         print('Tis number is a odd.')
#     return

# def Leap_year():
#     year = int(input("Year: "))
#     if (year % 4 == 0):
#         if (year % 100 ==0):
#             if (year % 400 == 0):
#                 print('{} year is Leap year!'.format(year))
#             else:
#                 print('{} year is not Leap year!'.format(year))
#         else:
#             print('{} year is Leap year!'.format(year))
#     else:
#         print('{} year is not Leap year!'.format(year))
#     return

# #获取最大值函数
# print(max(2452, 363, 6346, 23426, 6346))
# print(max([32, 5235, 523, 642, 624]))
# print(max((235, 262, 23, 643 ,262, 626)))
# print('2532, 462, 62342, 373, 57347 中的最大值为 {}'.format(max(2532, 462, 62342, 373, 57347)))

# #质数判断
# try:
#     num = int(input('请输入一个数字: '))
#
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 print('{} is not a prime number.'.format(num))
#                 break
#         else:
#              print('{} is a prime number.'.format(num))
#
#     else:
#         print('{} is not a prime number.'.format(num))
#
# except ValueError:
#     print('command is not a number.')

# #输出指定范围内的素数
# lower = int(input('输入区间最小值: '))
# upper = int(input('输入区间最大值: '))
#
# for num in range(lower, upper + 1):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num, end=", ")

# #阶乘实例
# def factorial():
#     fac = 1
#     num = int(input('请输入一个数: '))
#     if num < 0:
#         print('负数没有阶乘')
#     elif num == 0:
#         print('0 的阶乘为1')
#     else:
#         for i in range(1, num + 1):
#             fac = fac * i
#     print('{} 的阶乘为 {}'.format(num, fac))

# # 九九乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print("{}*{}={}".format(i, j, i * j), end=" ")
#     print()

# #斐波那契数列
#
# num = int(input('你需要几项？'))
#
# n1 = 0
# n2 = 1
# count = 2
#
# if num <= 0:
#     print('请输入一个正数')
# elif num == 1:
#     print('斐波那契数列: {}'.format(n1))
# elif num == 2:
#     print('斐波那契数列: {}, {}'.format(n1, n2))
# else:
#     print('斐波那契数列: 0, 1', end=", ")
#     while num > count:
#         nth = n1 + n2
#         print(nth, end=', ')
#         n1 = n2
#         n2 = nth
#         count += 1

# #阿姆斯特朗数
# num = int(input("请输入一个数字: \n"))
# numstr = str(num)
# n = len(numstr)
# sum = 0
#
# if num > 0:
#     for i in range(0, n):
#         while i != n:
#             x = int(numstr[i]) ** n
#             sum += x
#             break
#     if num == sum:
#         print('This number is an armstrong number.')
#     else:
#         print('This number is not an armstrong number.')
# else:
#     print('This number is not an armstrong number.')

# # 十进制转二进制、八进制、十六进制
# num = int(input("Input an number: \n"))
#
# print("The decimal number is: ", num)
# print("The binary number is: ", bin(num))
# print("The octal number is: ", oct(num))
# print("The hexadecimal number is: ", hex(num))

# #ASCII码与字符相互转换
#
# character = input("Enter a character: ")
# ASCII = int(input("Enter the ASCII:"))
# print('The ASCII of {} is {}'.format(character, ord(character)))
# print('The character of {} is {}'.format(ASCII, chr(ASCII)))

# # Greatest common divisor
# def gcd(a, b):
#     if a > b:
#         smaller = b
#     else:
#         smaller = a
#
#     for i in range(1, smaller + 1):
#         if (a % i == 0) and (b % i == 0):
#             gcd = i
#     return gcd
#
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# print("The greatest common divisor of {} and {} is {}".format(num1, num2, gcd(num1, num2)))

# #lowest common multiple
# def lcm(a, b):
#     if a > b:
#         greater = a
#     else:
#         greater = b
#
#     while True:
#         if (greater % a == 0) and (greater % b ==0):
#             lcm = greater
#             break
#         else:
#             greater += 1
#     return lcm
#
# num1 = int(input('Enter the first number: '))
# num2 = int(input('Enter the second number: '))
# print('The lowest common multiple of {} {} is {}'.format(num1, num2, lcm(num1, num2)))
# #简单计算器实现
# def add(a, b):
#     result = a + b
#     return result
#
# def sub(a, b):
#     result = a - b
#     return result
#
# def mul(a, b):
#     result = a * b
#     return result
#
# def div(a, b):
#     result = a / b
#     return result
#
# print('1. addition\n2. substraction\n3. multiplication\n4. division')
#
# method = int(input('What method do you choose(1/ 2/ 3/ 4)?\n'))
# if method in range(1, 5):
#     num1 = int(input('Enter the first number: '))
#     num2 = int(input('Enter the second number: '))
#
#     if method == 1:
#         print('{} + {} = {}'.format(num1, num2, add(num1, num2)))
#     elif method == 2:
#         print('{} - {} = {}'.format(num1, num2, sub(num1, num2)))
#     elif method == 3:
#         print('{} * {} = {}'.format(num1, num2, mul(num1, num2)))
#     elif method == 4:
#         print('{} / {} = {}'.format(num1, num2, div(num1, num2)))
# else:
#     print('Illegal input!')

# #生成日历
# import calendar
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
#
# print(calendar.month(year, month))

# #使用递归斐波那契数列
# def recur_fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return (recur_fibo(n - 1) + recur_fibo(n - 2))
#
# nterms = int(input('How many terms of fibonacci sequence you want?'))
# list = []
#
# if nterms >= 0:
#     for i in range(nterms):
#         list.append(recur_fibo(i))
#     print(list)
# else:
#     print('Please enter and positive integer')

# #文件 IO
# with open("tes.txt", "wt") as out_file:
#     out_file.write("该文本会写入到文件中\n看到我了吧！")
#
# with open("tes.txt", "rt") as in_file:
#     text = in_file.read()
#
# print(text)

# #字符串判断
# str = str(input('Enter an string: '))
# print(str.isalnum())
# print(str.isalpha())
# print(str.isdigit())
# print(str.islower())
# print(str.istitle())
# print(str.isspace())
# print(str.isupper())
# print(str.isascii())

# # 字符串大小写转换
# str = "I love you, Lorraine!"
# print(str.lower())
# print(str.upper())
# print(str.title())
# print(str.capitalize())

# # 计算每个月天数
# import calendar
# monthdays = calendar.monthrange(2021, 3)
# month_days = calendar.mdays[3]
# print(monthdays)
# print(month_days)

# #获取昨天日期
# import datetime
# def getyesterday():
#     today = datetime.date.today()
#     one_day = datetime.timedelta(days=1)
#     yesterday = today - one_day
#     return yesterday
#
# print(getyesterday())

# #约瑟夫生者死者小游戏
# dic = {}
# for i in range(1, 31):
#     dic[i] = 1
#
# count = 1
# out_person = 0
# i = 1
# while True:
#     if i == 31:
#         i = 1
#     elif out_person == 15:
#         break
#     else:
#         if dic[i] != 0:
#             if count == 9:
#                 dic[i] = 0
#                 print('{}号下船'.format(i))
#                 i += 1
#                 out_person += 1
#                 count = 1
#             else:
#                 count += 1
#                 i += 1
#                 continue
#         else:
#             i += 1
#             continue

# #五人分鱼
#
# def main():
#     fish = 1
#     while True:
#         total, enough = fish, True
#         for _ in range(5):
#             if (total - 1) % 5 == 0:
#                 total = (total - 1) // 5 * 4
#             else:
#                 enough = False
#                 break
#         if enough:
#             print("The total fish are {}".format(fish))
#             break
#         fish += 1
#
# if __name__ == '__main__':
#     main()

# # #实现秒表功能
# import time
# print('Press Enter to start the timer, and press ctrl+C to stop it.')
# while True:
#     input('')
#     start_time = time.time()
#     print('START')
#     try:
#         while True:
#             print('Timing: ', round(time.time() - start_time, 5), 'secs', end='\r')
#             time.sleep(0.00001)
#     except KeyboardInterrupt:
#         print('End')
#         end_time = time.time()
#         print('Total secs: ', round(end_time - start_time, 6), 'secs')
#     break

# #Python 计算 n 个自然数的立方和
#
# def Sumofserious(n):
#     sum = 0
#     for i in range(1, n + 1):
#         sum += i ** 3
#     return sum
#
# print(Sumofserious(5))

# #计算数组元素之和
#
# def _sum(arr, n):
#     return (sum(arr))
#
# arr = [2, 4, 6, 67, 32]
#
# n = len(arr)
# ans = _sum(arr, n)
# print(ans)

# #数组翻转指定个数的元素
# def Arr(arr, n):
#     for i in range(n):
#         x = arr.pop(0)
#         arr.append(x)
#     return arr
#
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# newarr = Arr(arr, 5)
#
# for i in range(len(arr)):
#     print("%d" % newarr[i], end=' ')

# #将列表中的头尾两个元素对调
# def swaplist(arr):
#     size = len(arr)
#     a = arr[0]
#     b = arr[size - 1]
#     arr[0] = b
#     arr[size - 1] = a
#     return arr
#
# arr = [1, 2, 3, 4, 5, 6, 7]
# print(swaplist(arr))

# #将列表中的指定位置的两个元素对调
# def swaplist(arr, pos1, pos2):
#     a = arr[pos1]
#     b = arr[pos2]
#     arr[pos2] = a
#     arr[pos1] = b
#     return arr
#
# arr = [1, 2, 3, 4, 5, 6, 7]
# print(swaplist(arr, 3, 6))

# #翻转列表
# def Reverse(list):
#     list.reverse()
#     return list
#
# list = [1, 2, 3, 4, 5, 6, 7]
# print(Reverse(list))

# #判断元素是否在列表中存在
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for i in list:
#     if i == 4:
#         print('exist')

# #清空列表
# list = [1, 2, 4, 5, 5, 6]
# list.clear()
# print(list)

# #复制列表
# list1 = [1, 2, 3, 4, 5, 5, 6, 7]
# list2 = list1.copy()
# print(list2)

# # 计算元素在列表中出现的次数
# def countx(list, x):
#     times = list.count(x)
#     return times
#
# list = [1, 2, 3, 4, 5, 6, 7, 4, 2, 6, 7, 1, 3, 2, 6]
# print(countx(list, 4))

# #计算列表元素之和
# list = [1, 2, 3, 5, 6, 6, 7, 8]
# _sum = sum(list)
# print(_sum)

# #计算列表元素之积
# list = [1, 2, 3, 4, 5, 6, 7 ,8, 9]
# def mul(list):
#     result = 1
#     for i in list:
#         result *= i
#     return result
#
# print(mul(list))


# #查找列表中最小元素
# list = [4, 6, 2, 4, 6, 8, 1, 4, 3, 3, 2]
# print(min(list))

# #查找列表中最大元素
# list = [2, 4, 6, 7, 1, 2, 3, 6, 7, 3, 2, 1]
# print(max(list))

# #移除字符串中的指定位置字符
#
# str = 'Kevin'
# def removeEle(str):
#     newstr = ''
#     for i in range(0, len(str)):
#         if i != 2:
#             newstr += str[i]
#     return newstr
# print(removeEle(str))

# #判断字符串是否存在子字符串
# def checksubstr(str, substr):
#     if str.find(substr) == -1:
#         print('not exist')
#     else:
#         print('exist')
#
# str = 'I love Lorraine.'
# substr = 'Kevin'
# print(checksubstr(str, substr))

# #判断字符串长度
# str = "I love Lorraine"
# print(len(str))



