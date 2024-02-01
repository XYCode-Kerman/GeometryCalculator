import sympy


class Point:
    def __init__(self, name: str, x=None, y=None):
        """
        点
        :param name: 名字
        :param x: 横坐标
        :param y: 纵坐标
        """
        self.name = name
        if x is None:
            x = sympy.Symbol(f'x{self.name}')
        if y is None:
            y = sympy.Symbol(f'y{self.name}')
        self.x = x
        self.y = y

    def coordinate(self) -> tuple:
        """
        获取该点的坐标
        :return: 元组，点的坐标
        """
        return self.x, self.y


class Line:
    def __init__(self, p1: Point, p2: Point):
        """
        线段/射线/直线
        :param p1: 线上一点
        :param p2: 线上另一点
        """
        self.p1 = p1
        self.p2 = p2

    def k(self):
        """
        获取所在直线的一次函数的斜率(k)
        :return: 斜率
        """
        return (self.p1.y - self.p2.y) / (self.p1.x - self.p2.x)


def distance(p1: Point, p2: Point):
    """
    获取两点间距离
    :param p1: 一点
    :param p2: 另一点
    :return: 距离
    """
    return sympy.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


class Angle:
    def __init__(self, p1: Point, vertex: Point, p2: Point):
        """
        角
        :param p1: 一边上的点
        :param vertex: 顶点
        :param p2: 另一边上的点
        """
        self.p1 = p1
        self.vertex = vertex
        self.p2 = p2
        self.val = self._get_value()

    def _get_value(self):
        """
        计算这个角的角度
        :return: 角度的表达式
        """
        # 已知三点坐标：A (X1,Y1) B (X2,Y2) C (X3,Y3)
        # AB向量：(X2-X1,Y2-Y1)
        # AC向量：(X3-X1,Y3-Y1)
        # BC向量：(X3-X2,Y3-Y2)
        # COS∠A=[(X2-X1)(X3-X1)+(Y2-Y1)(Y3-Y1)]/|AB||AC|
        # 其中：|AB|=[(X2-X1)^2+(Y2-Y1)^2]^0.5
        # |AC|=[(X3-X1)^2+(Y3-Y1)^2]^0.5
        # ∠A = Arccos {[(X2-X1)(X3-X1)+(Y2-Y1)(Y3-Y1)]/|AB||AC|}
        return sympy.acos(((self.p1.x - self.vertex.x) * (self.p2.x - self.vertex.x) + (self.p1.y - self.vertex.y) * (
                self.p2.y - self.vertex.y)) / (distance(self.p1, self.vertex) * distance(self.p2, self.vertex)))


if __name__ == '__main__':
    pass
