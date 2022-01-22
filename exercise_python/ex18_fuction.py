#this one is like you scripts with argv
#将arg1，arg2赋值为args里面的两个参数，然后分别打印
#*args是告诉python将里面所有的参数都接受进来
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
#直接使用（）里面的arg1,arg2作为变量名
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothin'.")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("Frist!")
print_none()