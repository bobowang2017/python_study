class A:
    def get_value(self):
        print("return value of A ")

    def show(self):
        print('show A')


class B(A):
    def get_value(self):
        print("return value of B ")


class C(A):
    def get_value(self):
        print("return value of C ")

    def show(self):
        print("show C")


class D(B, C):
    pass


d = D()
d.get_value()
d.show()
print(D.__mro__)
