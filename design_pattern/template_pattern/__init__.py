# 模板模式定义如下：定义一个操作中的算法的框架，而将一些步骤延迟到子类中，使得子类可以不改变一个算法的结构即可重新定义该
# 算法的某些特定的步骤。子类实现的具体方法叫作基本方法，实现对基本方法高度的框架方法，叫作模板方法。

# 模板模式的优点：
# 1、可变的部分可以充分扩展，不变的步骤可以充分封装；
# 2、提取公共代码，减少冗余代码，便于维护；
# 3、具体过程可以定制，总体流程方便掌控。
#
# 使用场景：
# 1、某超类的子类中有公有的方法，并且逻辑基本相同，可以使用模板模式。必要时可以使用钩子方法约束其行为。具体如本节例子；
# 2、比较复杂的算法，可以把核心算法提取出来，周边功能在子类中实现。例如，机器学习中的监督学习算法有很多，如决策树、KNN、
# SVM等，但机器学习的流程大致相同，都包含输入样本、拟合（fit）、预测等过程，这样就可以把这些过程提取出来，构造模板方法，
# 并通过钩子方法控制流程。

# 缺点
# 1、模板模式在抽象类中定义了子类的方法，即子类对父类产生了影响，部分影响了代码的可读性。
# 2、调试和理解模板方法中的流程序列有时会令人困惑。
# 3、维护难度大