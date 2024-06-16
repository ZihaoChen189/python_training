"""
int, float, string, boolean
"""

money = 28
print(type(money))

money = 2.8
print(money)
print(type(money))

money = "280"
print(type(money))

triple_quotation_str = """abc"a'b'c"abc"""
print(triple_quotation_str)
print(type(triple_quotation_str))

format_saved_test_str = """
        abc, abc
        abc, abc"""  # for triple quotation marks
print(format_saved_test_str)
print(type(format_saved_test_str))

isLogin = True
print(isLogin)
print(type(isLogin))

money = input("Enter the *integer* amount: ")
# print(money+10)  # ERROR:(
print(int(money)+0.81)

# a = "1.5"
# print(int(a))  # ERROR:(

number_a = 0
print(bool(number_a))  # False
number_b = -1
print(bool(number_b))  # True
number_c = 3
print(bool(number_c))  # True

str_a = ""
print(bool(str_a))  # False
str_b = "str_b"
print(bool(str_b))  # True

name = "Daenerys Targaryen"
age = 18

print("I love " + name + ", who is " + str(age))
"""
%s: str, %d: digit, %f: float
"""
print("I love %s, who is %d years old." % (name, age))
gold = 123.4567
print("%s has %f kg gold." % (name, gold))
print("%s has %.2f kg gold." % (name, gold))

for i in range(0, 2):
    print(str(i)+"---")
    for j in range(5, 10):
        print(str(j)+"inner")
        if j == 7:
            break  # break inner for loop :)

# BUT "while" loop could be used when you cannot ensure the times of loops
