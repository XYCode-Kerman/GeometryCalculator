import time

import sympy

from classes import *
from read import read_expr

print('作者：MC着火的冰块\thttps://space.bilibili.com/551409211')

# 所有点的字典，通过名字对应对象
points = dict()
# 条件，里面的表达式值都为0
conditions = []

# 输入条件
print('\n添加点，每次一个，仅一个大写字母，输入ok结束')
print('样例：A')
while (tmp := input('>>>')) != 'ok':
    try:
        points[tmp] = Point(tmp)
        print(f'解析成功：添加点 {tmp}{points[tmp].coordinate()}')
    except Exception as e:
        print(f'{e.__class__.__name__}: {e}')
        print('解析失败')

print('\n添加三点共线，三点用空格分格，输入ok结束')
print('样例：A B C')
while (tmp := input('>>>')) != 'ok':
    try:
        p1, p2, p3 = [points[i] for i in tmp.split(' ')]
        expr = Line(p1, p2).k() - Line(p1, p3).k()
        expr = sympy.simplify(expr)
        conditions.append(expr)
        print(f'解析成功：添加条件 {expr} = 0')
    except Exception as e:
        print(f'{e.__class__.__name__}: {e}')
        print('解析失败')

print('\n添加平行，两线用空格分格，输入ok结束')
print('样例：AB CD\t(表示AB//CD)')
while (tmp := input('>>>')) != 'ok':
    try:
        p1, p2 = [points[i] for i in tmp.split(' ')[0]]
        p3, p4 = [points[i] for i in tmp.split(' ')[1]]
        expr = Line(p1, p2).k() - Line(p3, p4).k()
        expr = sympy.simplify(expr)
        conditions.append(expr)
        print(f'解析成功：添加条件 {expr} = 0')
    except Exception as e:
        print(f'{e.__class__.__name__}: {e}')
        print('解析失败')

print('\n添加垂直，两线用空格分格，输入ok结束')
print('样例：AB CD\t(表示AB⊥CD)')
while (tmp := input('>>>')) != 'ok':
    try:
        p1, p2 = [points[i] for i in tmp.split(' ')[0]]
        p3, p4 = [points[i] for i in tmp.split(' ')[1]]
        expr = Line(p1, p2).k() * Line(p3, p4).k() + 1
        expr = sympy.simplify(expr)
        conditions.append(expr)
        print(f'解析成功：添加条件 {expr} = 0')
    except Exception as e:
        print(f'{e.__class__.__name__}: {e}')
        print('解析失败')

print('\n添加相等关系，输入一个等式，输入ok结束')
print('样例：AB=CD\tAB=114514\tAB=2*AC\t(*不可省略，乘方运算符为**，pi代表π)')
print('     角AOB=90度\t角AOB=pi/2\t角AOB+角BOC=135度\t(带度为角度制，不带度为弧度制，不支持单个字母的简写)')
while (tmp := input('>>>')) != 'ok':
    try:
        left, right = tmp.split('=')
        expr = read_expr(left, points) - read_expr(right, points)
        expr = sympy.simplify(expr)
        print(f'解析成功：添加条件 {expr} = 0')
        conditions.append(expr)
    except Exception as e:
        print(f'{e.__class__.__name__}: {e}')
        print('解析失败')

print('\n条件读取完成')
print('请输入要求的值')
print('样例：AB\t角AOB')
while True:
    try:
        name = input('>>>')
        unknown = sympy.Symbol(name)
        expr = read_expr(name, points)
        conditions.append(expr - unknown)
        print(f'解析成功：求{expr}')
    except Exception as e:
        print(f'{e.__class__.__name__}: {e}')
        print('解析失败')
    else:
        break

print('已知条件如下：')
print('\n'.join(['{ ' + f'{str(i)} = 0' for i in conditions]))

# 所有参数
symbols = [unknown]
for i in points.values():
    symbols.extend(i.coordinate())

print('开始计算，请耐心等待...')
t1 = time.time()
result = sympy.solve(conditions, symbols)
t2 = time.time()
print('所有可能的解如下：')
print(set([i[0] for i in result]))
print(f'耗时{t2 - t1}s')
