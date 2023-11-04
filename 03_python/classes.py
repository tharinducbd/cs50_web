class Point():
    def __init__(self, coord_x, coord_y) -> None:
        self.x = coord_x
        self.y = coord_y


p = Point(2, 8)
print(p.x)
print(p.y)
print(p)
