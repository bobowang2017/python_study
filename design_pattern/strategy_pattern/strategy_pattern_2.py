import types


class People(object):
    def __init__(self, hand=None):
        self.name = "人手"
        if hand:
            self.execute = types.MethodType(hand, self)

    def execute(self):
        print(self.name)


# 创造猪手
def pig_hand(self):
    print(self.name + " 用猪手")
    print("拱你")


# 创造猫爪
def cat_hand(self):
    print(self.name + " 用猫爪")
    print("抓你")


if __name__ == '__main__':
    hand0 = People()
    # 用猪手替换人手
    hand1 = People(pig_hand)
    hand1.name = "猪手"

    # 用猫爪替换人手
    hand2 = People(cat_hand)
    hand2.name = "猫爪"

    hand0.execute()
    hand1.execute()
    hand2.execute()
