# list_1 = []
# list_2 = ["apple"]
#
# list_1.append("car")
# list_1.append("car")
# list_1.append("car")
# print(list_1)

# list_1 = list_1 + list_2
# list_1.extend(list_2)
# print(list_1)

# list_1.pop()  # delete the last item in the list
# list_1.pop(3)
# list_1.pop(10)  # ERROR :(
# print(list_1)

# list_1.remove("car")
# print(list_1)  # only delete value "car" one time
# list_1.insert(0, "insert_test")  # insert(index, value)
# print(list_1)

# dictionary={key:value}, key CANNOT be changed, but value could be changed
# key was UNIQUE!

# book = {"name": "Three Body", "price": 58.88, "author": "Big Liu"}
# book_name = book.get("name_other", None)
# print(book_name)
#
# for key in book:
#     print(key)
#
# for value in book.values():
#     print(value)
#
# for key, value in book.items():
#     print(key, value)
#
# order_practice = (45, 12, 78, 30)
# result = sorted(order_practice, reverse=True)
# print(result)

# advance_list = [i for i in range(10)]
# advance_list = [i+2 for i in range(10)]
#
# print(advance_list)

# list_2 = ["NB", "66", "KNN", "SVM"]
# advance_list_2 = [i for i in list_2 if i.isalpha()]
# print(advance_list_2)

practice_1 = [x for x in range(1, 101)]
practice_2 = [practice_1[x:x+3] for x in range(0, len(practice_1), 3)]
print(practice_2)
