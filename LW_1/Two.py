class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def input_point():
    x = int(input("x: "))
    y = int(input("y: "))
    return Point(x, y)


def g(a: Point, b: Point, d: Point):
    return (d.x - a.x) * (b.y - a.y) - (d.y - a.y) * (b.x - a.x)


def f(a: Point, b: Point, c: Point, d: Point):
    return g(a, b, c) * g(a, b, d) >= 0


def two():
    print("A")
    a = input_point()
    print("B")
    b = input_point()
    print("C")
    c = input_point()
    print("D")
    d = input_point()
    if f(a, b, c, d) and f(b, c, a, d) and f(c, a, b, d):
        print("Yes")
    else:
        print("No")
