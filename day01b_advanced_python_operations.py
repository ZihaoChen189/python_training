import random

str_1 = "hello"
str_2 = str_1  # just *initially* set the same address
str_3 = "hello"

print(id(str_1), id(str_2), id(str_3))  # 4366764656 4366764656 4366764656

str_1 = "world"
print(id(str_1), id(str_2), id(str_3))  # 4366795568 4366764656 4366764656

str_family = "ABCDEFG"
# [start, end)
print(str_family[:5])
print(str_family[-3:])
print(str_family[:])
print(id(str_family[:]), id(str_family))  # the same address

print(str_family[0:5:-2])  # nothing
print(str_family[5:0:-2])  # FDB

i = str_family.find("B")  # rfind() for the opposite direction
j = str_family.find("X")  # rfind() for the opposite direction
# index() would return error if it cannot find the target
print(str_family[i+1:])
print(j)

number = str_family.count("B")
print(number)


verification_code_warehouse = "0123456789ABCDEFG"
verification_code = ""
for character in range(0, 6):
    caught_single_char = random.randint(0, len(verification_code_warehouse) - 1)
    verification_code += str(verification_code_warehouse[caught_single_char])
print(verification_code)

name = "Daenerys Targaryen"
age = 18

sentence = "The queen {} was {} years old".format(name, age)
print(sentence)

sentence_2 = "The queen {name} was {age} years old".format(name="Daenerys Targaryen", age=20)
print(sentence_2)
