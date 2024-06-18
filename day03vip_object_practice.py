# class Phone(object):
#     def __init__(self, brand, price, type, note):
#         print(self)
#         self.brand = brand
#         self.price = price
#         self.type = type
#         self.note = note
#
#     def call(self):
#         print("calling......")
#         print("brand:", self.brand)
#         print("price:", self.price)
#         print("type:", self.type)
#         print("note:", self.note)
#
#
# phone_1 = Phone("Apple", 3000, "12 pro", "good")
# phone_1.call()
# phone_2 = Phone("Hua Wei", 1000, "mate 66", "very good")
# phone_2.call()

# class Dog(object):
#     nickname = "pass the code"
#
#     def __init__(self, nickname):
#         self.nickname = nickname
#
#     def run(self):  # self = object
#         print("{} is running...".format(self.nickname))
#
#     def eat(self):
#         print("eating")
#         self.run()
#
#     @classmethod
#     def test(cls):  # cls = class
#         print(cls)
#         print(cls.nickname)
#         # cls.run()  # ERROR :( since run was based on "self" (passed object)
#
#
# animal_1 = Dog("Big Yellow")
# animal_1.run()
# animal_1.test()
#
# Dog.test()

class Cat(object):
    type = "cat"

    def __init__(self, nickname, age, color):
        self.nickname = nickname
        self.age = age
        self.color = color

    def eat(self, food):
        print("{} likes eating {}".format(self.nickname, food))

    def work(self, mouse_color, mouse_weight):
        print("{} catches {} g {} mouse".format(self.nickname, mouse_weight, mouse_color))

    def sleep(self, hour):
        if hour < 5:
            print("continue sleep please")
        else:
            print("work!")

    def show(self):
        print("cat details:", self.nickname, self.age, self.color)


# cat_1 = Cat("Potter", 2, "yellow")
# cat_1.work("black", 20)
# cat_1.sleep(8)
# cat_1.eat("fishes")
# cat_1.show()


class Person(object):
    def __init__(self, name):
        self.name = name
        print("init", self)

    def __new__(cls, *args, **kwargs):  # apply for the space for the address
        print("new")
        # return object.__new__(cls, *args, **kwargs)  # apply for the address and pass it to the __init__
        position = object.__new__(cls)  # python 3.6 update
        print(position)
        return position

    # def __call__(self, name):
    #     print("execute __call__")
    #     print(name)


p = Person("Robert")
# print(p)

# p("call aaaaa")
