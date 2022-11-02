class Shape:
    @staticmethod
    def create(name):
        # TODO: Fill the code here
        # NOTE: Raise `ValueError("Invalid name", name)` if there is no such shape.
        if name == 'circle':
            return Circle()
        elif name == 'square':
            return Square()
        elif name == 'line':
            return Line()
        else:
            raise ValueError('Invalid name', name)


class Circle(Shape):
    def draw(self):
        print("ㅇ")


class Square(Shape):
    def draw(self):
        print("ㅁ")


class Line(Shape):
    def draw(self):
        print("ㅡ")


if __name__ == "__main__":
    x = Shape.create("circle")
    x.draw()
    x = Shape.create("square")
    x.draw()
    x = Shape.create("line")
    x.draw()
    x = Shape.create('hello world')

    # Expected Output
    # > ㅇ
    # > ㅁ
    # > ㅡ
