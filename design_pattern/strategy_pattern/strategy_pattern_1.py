class Strategy:
    def algorithm_interface(self):
        raise NotImplementedError


class ConcreteStrategyA(Strategy):
    def algorithm_interface(self):
        print("算法A实现")


class ConcreteStrategyB(Strategy):
    def algorithm_interface(self):
        print("算法B实现")


class ConcreteStrategyC(Strategy):
    def algorithm_interface(self):
        print("算法C实现")


class Context:
    def __init__(self, strategy):
        self.m_strategy = strategy

    def context_interface(self):
        if self.m_strategy:
            self.m_strategy.algorithmInterface()


c = Context(ConcreteStrategyA())
c.context_interface()
