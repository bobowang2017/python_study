# -*- coding: utf-8 -*-
from copy import copy, deepcopy


class SimpleLayer:
    """
    　　设计一个图层对象，用background表示背景的RGBA，简单用content表示内容，除了直接绘画，还可以设置透明度。
　　"""
    background = [0, 0, 0, 0]
    content = "blank"

    def getContent(self):
        return self.content

    def getBackground(self):
        return self.background

    def paint(self, painting):
        self.content = painting

    def setParent(self, p):
        self.background[3] = p

    def fillBackground(self, back):
        self.background = back

    def clone(self):
        return copy(self)

    def deep_clone(self):
        return deepcopy(self)


if __name__ == "__main__":
    dog_layer = SimpleLayer()
    dog_layer.paint("Dog")
    dog_layer.fillBackground([0, 0, 255, 0])
    print("Background:", dog_layer.getBackground())
    print("Painting:", dog_layer.getContent())
    another_dog_layer = dog_layer.clone()
    # 通过复制（clone）这个动作实现画一只同样的狗
    print("Background:", another_dog_layer.getBackground())
    print("Painting:", another_dog_layer.getContent())
