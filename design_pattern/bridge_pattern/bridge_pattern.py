# 在一个画图程序中，常会见到这样的情况：有一些预设的图形，如矩形、圆形等，还有一个对象-画笔，调节画笔的类型（如画笔还是画
# 刷，还是毛笔效果等）并设定参数（如颜色、线宽等），选定图形，就可以在画布上画出想要的图形了。要实现以上需求，先从最抽象的
# 元素开始设计，即形状和画笔（暂时忽略画布，同时忽略画笔参数，只考虑画笔类型）。


class Shape(object):
    name = ""
    param = ""

    def __init__(self, *param):
        print("__init__")

    def getName(self):
        return self.name

    def getParam(self):
        return self.name, self.param


class Pen(object):
    shape = ""
    type = ""

    def __init__(self, shape):
        self.shape = shape

    def draw(self):
        pass


# 形状对象和画笔对象是最为抽象的形式。接下来，构造多个形状，如矩形和圆形：

class Rectangle(Shape):
    def __init__(self, long, width):
        self.name = "Rectangle"
        self.param = "Long:%s Width:%s" % (long, width)
        print("Create a rectangle:%s" % self.param)


class Circle(Shape):
    def __init__(self, radius):
        self.name = "Circle"
        self.param = "Radius:%s" % radius
        print("Create a circle:%s" % self.param)


# 紧接着是构造多种画笔，如普通画笔和画刷：

class NormalPen(Pen):
    def __init__(self, shape):
        Pen.__init__(self, shape)
        self.type = "Normal Line"

    def draw(self):
        print("DRAWING %s:%s----PARAMS:%s" % (self.type, self.shape.getName(), self.shape.getParam()))


class BrushPen(Pen):
    def __init__(self, shape):
        Pen.__init__(self, shape)
        self.type = "Brush Line"

    def draw(self):
        print("DRAWING %s:%s----PARAMS:%s" % (self.type, self.shape.getName(), self.shape.getParam()))


# 业务中的逻辑如下：

if __name__ == "__main__":
    normal_pen = NormalPen(Rectangle("20cm", "10cm"))
    brush_pen = BrushPen(Circle("15cm"))
    normal_pen.draw()
    brush_pen.draw()
