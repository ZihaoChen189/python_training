import inspect


class Base:
    def test(self):
        print("Base-test")


class A(Base):
    def test(self):
        print("A-test")


class B(Base):
    def test(self):
        print("B-test")


class C(Base):
    def test(self):
        print("C-test")


class D(A, B, C):
    # def test(self):
    #     print("D-test")
    pass


d = D()
d.test()
print(inspect.getmro(D))
