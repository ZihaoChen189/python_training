# import sys
#
#
# class Person(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __del__(self):
#         print("===del===")
#
#
# p = Person("Robert")
# p1 = p  # point to the same address
# p2 = p  # point to the same address
# p2.name = "Dale"
#
# print(p1.name)
# print(p2.name)
#
# print(sys.getrefcount(p))
# del p2
# print(sys.getrefcount(p))
# del p1
# print(sys.getrefcount(p))
# del p  # there was no point to the applied space address, execute __del__
#
# n = 5
# n1 = n
# print(n)


# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return self.name + " is " + str(self.age) + " years old"
#
#
# p = Person("Tom", 12)
# print(p)  # not address if we had __str__


# class Student(object):
#     # attributes:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#         self.__score = 59
#
#     def set_age(self, age):
#         if 0 < age <= 120:
#             self.__age = age
#
#     def get_age(self):
#         return self.__age
#
#     def __str__(self):
#         return str(self.__score) + self.__name + str(self.__age)


# s1 = Student("Dale", 20)
# print(s1)
# print(s1.get_age())
# s1.set_age(22)
# print(s1)
# print(s1.get_age())
#
# print(dir(Student))
# print(dir(s1))
# print(s1.__dir__())
#
# print(s1._Student__age)  # not be encouraged


# class Student(object):
#     # attributes:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#
#     # def set_age(self, age):
#     #     if 0 < age <= 120:
#     #         self.__age = age
#     #
#     # def get_age(self):
#     #     return self.__age
#
#     @property  # FIRST created
#     def age(self):
#         return self.__age
#
#     @age.setter  # SECOND created
#     def age(self, age):
#         if 0 < age <= 120:
#             self.__age = age
#         else:
#             print(str(age) + " was Invalid age range!")
#
#     def __str__(self):
#         return self.name + str(self.__age)
#
#
# s2 = Student("Dale", 12)
# print(s2)
# print(s2.__dir__())
#
# s2.age = 2000
# print(s2.age)


import random


class Road(object):
    def __init__(self, name, len):
        self.name = name
        self.len = len


class Car(object):
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def get_time(self, road):
        random_time = random.randint(1, 10)
        print("{} car has {} speed on {} for {} seconds".format(self.brand, self.speed, road.name, random_time))

    def __str__(self):
        return "{} car has {} speed".format(self.brand, self.speed)


road_1 = Road("Jing-Ha Highway", 12000)
audi = Car("Audi", 120)

print(audi)
audi.get_time(road_1)

