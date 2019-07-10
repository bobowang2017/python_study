# 使用python实现适配器设计模式有多种方法。比如继承，组合，但是Python提供了一个替代方案，即使用类的内部字典。

# 先来看看“我们有什么”部分。我们的应用有一个Computer类，用来显示一台计算机的基本信息。这一例子中的所有类，包括Computer
# 类，都非常简单。在这里，execute方法是计算机可以执行的主要动作。这一方法由客户端代码调用。


class Computer(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} computer'.format(self.name)

    def execute(self):
        return 'executes a program'


# 在Synthesizer类中，主要动作由play()方法执行。
class Synthesizer(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} synthesizer'.format(self.name)

    def play(self):
        return 'is playing an electronic song'


# 在Human类中，主要动作由speak()方法执行。
class Human(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '{} the human'.format(self.name)

    def speak(self):
        return 'says hello'


# 问题是：客户端仅知道如何调用execute()方法，并不知道play()和speak()。在不改变Synthesizer和Human类的前提下，我们该如何做
# 才能让代码有效？
# 适配器是救星！我们创建一个通用的Adapter类，将一些带不同接口的对象适配到一个统一接口中。__init__方法的obj参数是我们想要
# 适配的对象，adapted_methods是一个字典，键值对中的键是客户端要调用的方法，值是应该被调用的方法。

class Adapter(object):
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)

# 下面看看使用适配器模式的方法。列表objects容纳着所有对象。属于Computer类的可兼容对象不需要适配。可以直接将它们添加到列表
# 中。不兼容的对象则不能直接添加。使用Adapter类来适配它们。结果是，对于所有对象，客户端代码都可以始终调用已知的execute()
# 方法，而无需关心被使用的类之间的任何接口差别。


if __name__ == "__main__":
    objects = [Computer('Asus')]
    synth = Synthesizer('moog')
    objects.append(Adapter(synth, dict(execute=synth.play)))
    human = Human('Bob')
    objects.append(Adapter(human, dict(execute=human.speak)))

    for i in objects:
        print('{} {}'.format(str(i), i.execute()))
        print('type is {}'.format(type(i)))
