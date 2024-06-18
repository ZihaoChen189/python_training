# old_list = [x*3 for x in range(10)]
# print(old_list)
#
# new_list_generator = (x*3 for x in range(10))
# print(new_list_generator)  # address
# print(new_list_generator.__next__())
# print(new_list_generator.__next__())
#
# print(next(new_list_generator))  # builtins
# print(next(new_list_generator))  # builtins

# while True:
#     try:
#         print(next(new_list_generator))
#     except:
#         print("no more times")
#         break


# def func():
#     n = 0
#     while True:
#         n += 1
#         yield n  # stop the while loop for now
#
#
# g = func()
# print(g)
#
# print(next(g))
# print(next(g))


# def gen():
#     i = 0
#     while i < 5:
#         temp = yield i
#         print("temp", temp)
#         i += 1
#     return "no more data"
#
#
# g = gen()
# g.send(None)  # compulsory
# n1 = g.send("haha")
# print(n1)
# n2 = g.send("lala")
# print(n2)


def task_1(n):
    for i in range(n):
        print("aaa-", i)
        yield None


def task_2(n):
    for i in range(n):
        print("bbb-", i)
        yield None


g1 = task_1(5)
g2 = task_2(5)

while True:
    try:
        g1.__next__()
        g2.__next__()
    except:
        print("over")
        break

# iter()
# what about "iterator" not generator?
# generator is a special kind of iterator
