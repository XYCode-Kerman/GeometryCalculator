import re

import sympy
from sympy import pi

from classes import *


def read_expr(expr: str, points: dict):
    # 处理线段长度
    pattern = r'\b([A-Z])([A-Z])\b'
    repl = r"distance(points['\1'],points['\2'])"
    expr = re.sub(pattern, repl, expr)
    # 处理角
    pattern = r'\b角([A-Z])([A-Z])([A-Z])\b'
    repl = r"Angle(points['\1'],points['\2'],points['\3']).val"
    expr = re.sub(pattern, repl, expr)
    # 角度制转弧度制
    pattern = r'\b(\d+)度\b'
    repl = r'sympy.rad(\1)'
    expr = re.sub(pattern, repl, expr)
    return eval(expr)


if __name__ == '__main__':
    pass
