# def changeme(mylist):
#     mylist.append([1, 2, 3, 4])
#     print(" 函数内取值:", mylist)
#     return
#
# mylist = [10, 20, 30]
# print(id(mylist))
# changeme(mylist)
# print(mylist)
# print(id(mylist))

# def people(name:str, age:int):
#     print("name:", name)
#     print("age:", age)
#     return
# a = "Kevin"
# b = 19
# print(people(a, b))

# def function(a, *varible):
#     print(a)
#     print(varible)
#     return
# print(function(1, 2))
#
# def function2(a, **dictionary):
#     print(a)
#     print(dictionary)
#     return
# print(function2(1))

# x = lambda a, b: a + b
# print(x(1, 2))

# def sum( arg1, arg2 ):
#    # 返回2个参数的和."
#    total = arg1 + arg2
#    print ("函数内 : ", total)
# #    return total
#
# total = sum( 10, 20 )
# print("函数外 : ", total)

# numbers = [1, 3, 6]
# newNumbers = tuple(map(lambda x: x , numbers))
# print(newNumbers)

# from _collections_abc import Iterable

# a = "lwx"
# b = ["doinb", "wandehaoa"]
# c = ["lwxnb", "The shy nb"]
# b.append(c)
# print(b)

# vec = [1, 2, 3, 4]
# print([x*2 for x in vec])
# print([(x, x**2) for x in vec])

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# transposed = []
# for i in range(4):
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)
#
# print(transposed)

# x = [1, 2, 3, 4]
# x.pop(1)
# print(x)

# print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
#

# class Stack:
#     def __init__(self):
#         self.__data = []
#
#     def isEmpty(self):
#         """判断栈是否为空"""
#         return self.__data == []
#
#     def push(self, data):
#         """在栈顶添加元素"""
#         self.__data.append(data)
#
#     def pop(self):
#         """弹出顶部元素"""
#         return self.__data.pop()
#
#     def peek(self):
#         """返回栈顶元素"""
#         # 先判断是否为空
#         if self.isEmpty():
#             return
#         else:
#             return self.__data[-1]
#
#     def size(self):
#         """判断长度"""
#         return len(self.__data)
#
#     def travel(self):
#         """遍历所有元素"""
#         self.__data = self.__data[::-1]
#         for i in self.__data:
#             print(i)
#
# def doMath(op, op1, op2):
#     if op == "*":
#         return op1 * op2
#     elif op == "/":
#         return op1 / op2
#     elif op == "+":
#         return op1 + op2
#     else:
#         return op1 - op2
#
# def postfixEval(postfixExpr):
#     operandStack = Stack()
#     tokenList = postfixExpr.split()
#     for token in tokenList:
#         if token in "0123456789":
#             operandStack.push(int(token))
#         else:
#             operand2 = operandStack.pop()
#             operand1 = operandStack.pop()
#             result = doMath(token, operand1, operand2)
#             operandStack.push(result)
#     return operandStack.pop()
#
# print(postfixEval("1 + 5 * 9"))

# if __name__ == '__main__':
#    print('程序自身在运行')
# else:
#    print('我来自另一模块')imp
# import os
# print(os.name)
# print(os.sep)
# print(os.getenv('path'))
# print(os.getcwd())

# def f(n):
#     if n == 1:
#         return 1
#     else:
#         return (f(n - 1) + 1) * 2
# print(f(10))

# from datetime import date
# now = date.today()
# birthday = date(2002, 1, 1)
# age = now - birthday
# print(age.days)

# def abc(x, y):
#     x = int(x)
#     y = int(y)
#     if x > y:
#         return y
#     else:
#         return x + y
# print(abc(3, 2) + abc(-4, 1))impor

# first_pixel = input('Enter the first pixel value: ')
# second_pixel = input('Enter the second pixel value: ')
# number = input('Enter the number of pixels to generate in between: ')
# print('Colours:')
# R_gap = round(second_pixel[2:])


