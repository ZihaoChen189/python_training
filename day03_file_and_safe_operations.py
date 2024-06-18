import os


# stream = open("happy.txt")
# content = stream.read()
# little_flag = stream.readable()
# print(little_flag)
# print(content)
# stream.close()

# stream = open("happy.txt", "w")
# stream.close()

# copy a file:
# with open("picture_1.png", "rb") as stream:
#     container = stream.read()
#     path = os.path.dirname(__file__)
#     path1 = os.path.join(path, "picture_33.png")
#     with open(path1, "wb") as write_stream:
#         write_stream.write(container)

# print(os.path)
# print(os.path.dirname(__file__))

# os.
# os.getcwd
# os.listdir
# os.mkdir
# os.rmdir
# os.remove
# os.chdir

# os.path.
# os.path.dirname
# os.path.join
# os.path.split
# os.path.splitext
# os.path.getsize


# operations for safe code: try - except - finally

# def func():
#     try:
#         number_1 = int(input("input the first number"))  # input is string
#         number_2 = int(input("input the second number"))
#         number_result = number_1 / number_2
#         print(number_result)
#     except ZeroDivisionError:
#         # print("ZeroDivisionError")
#         raise Exception("0000000abcdefg")
#     except ValueError:
#         print("ValueError")
#     except Exception as e:
#         print("reason:", e)
#
#
# func()
# print("-----")


def register():
    username = input("Enter the username:")
    if len(username) < 6:
        raise Exception(":(")
    else:
        print("Welcome", username)


try:
    register()
except Exception as e:
    print(e)
    print("fail")
else:
    print("success")
print("---")
