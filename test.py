from locksmith import locked_function, locked_method


class TestClass:

    def __init__(self):
        self.x = 0
        self.y = 0

    @locked_function("x")
    def method1(self):
        self.x += 1

    @locked_method("y")
    def method2(self):
        self.x += 1

    @locked_method("y")
    def method3(self):
        self.x += 1

    @locked_method("y")
    def method4(self):
        self.x += 1


t = TestClass()
t.method2()
t.method2()


t2 = TestClass()
t2.method2()

