import random


def generate_verification_code(length, security_flag=True):
    verification_code_warehouse = "0123456789ABCDEFG"
    verification_code = ""
    for character in range(0, length):
        caught_single_char_index = random.randint(0, len(verification_code_warehouse) - 1)
        verification_code += str(verification_code_warehouse[caught_single_char_index])
    print(verification_code)


# generate_verification_code(5)
# generate_verification_code(20)


def bad_get_sum(a, b):
    r = a + b
    print(r)


def get_sum(*args):
    sum_result = 0
    for arg in args:
        sum_result += arg
    print(sum_result)
    print(args)
    print(type(args))


get_sum(1, 2, 3, 4, 5)
# get_sum([1, 2, 3, 4, 5])
get_sum(*[1, 2, 3, 4, 5])  # ERROR would happen without *


# a, *b, c = 1, 2, 3, 4, 5, 6, 7
# print(a)
# print(b)
# print(c)


def show_book(**kwargs):
    print(kwargs)
    print(type(kwargs))  # dict
    for key, value in kwargs.items():
        print(key, value)


show_book(book_name="Three Body", author="Big Liu")
show_book(book_name="Three Body", author="Big Liu", number=5)
show_book(**{"book_name": "Three Body", "author": "Big Liu"})


def show_book_pro(*args, **kwargs):
    print(args)  # ()
    print(kwargs)  # {}


show_book_pro(*["Zihao", "Jiayi"], **{"book_name": "Three Body", "author": "Big Liu"})

# "".format()
print("{}{}{}".format("aa", "bb", "cc"))
print("{x}{y}{z}".format(x="aa", y="bb", z="cc"))

results = "#".join(["aa", "bb", "cc"])
print(results)


# def deco(func):
#     print("--->1")
#
#     def wrapper(address):
#         # a series of new actions :)
#         print("painting")
#         print("clean the floor")
#         print("purchase furniture")
#         print("refine the house")
#
#         func(address)  #
#
#     print("--->2")
#     return wrapper
#
#
# @deco  # firstly run "deco(house_1)" in line 69 but without running inner wrapper()
# # then, house_1 =====>>>>>     house_1 = wrapper     important!
# def house_1(address):
#     print("live in house 1, where is in {}".format(address))
#
#
# house_1("Han Linyuan")  # wrapper


# A better version:)
# def deco(func):
#
#     def wrapper(*args, **kwargs):
#         print("painting")
#         print("clean the floor")
#         print("purchase furniture")
#         print("refine the house")
#
#         func(*args, **kwargs)  #
#
#     return wrapper
#
#
# @deco
# def house_2(address, area):
#     print("live in house 1, where is in {} and {} area".format(address, area))
#
#
# @deco
# def house_3(address, area, name):
#     print("live in house 1, where is in {} and {} area belonging to {}".format(address, area, name))
#
#
# house_2("Han Liyuan", "200m^2")  # *args
# house_3(address="Han Liyuan", area="200m^2", name="Robert")  # **kwargs


# what about functions with the return value
def deco(func):

    def wrapper(*args, **kwargs):
        print("painting")
        print("clean the floor")
        print("purchase furniture")
        print("refine the house")

        money = func(*args, **kwargs)  #
        money += 100
        return money
    return wrapper


@deco
def house_2(address, area):
    print("live in house 1, where is in {} and {} area".format(address, area))
    return 50


final_budget = house_2("Han Liyuan", "200m^2")  # *args
print(final_budget)
