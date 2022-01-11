def add(a,b):
    print(f"ADDING {a} + {b}")
    return a + b
def subtract(a,b):
    print(f"SUBSTRACTING {a} - {b}")
    return a - b 
def multiply(a,b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b 
def divide(a,b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


#A Puzzle for the extra credit, type it in anyway
print("Here is a puzzle.")


#a+(b-c*(d/2))
#python从左向右读，先运行add(),但是遇到了subtract(),subtract()里面又有multiply(),multiply里面又有divide()
#所以python需要先调用divide,然后向外层传递参数，直到最外层，很复杂的嵌套
#注意要变成整数或者浮点型
a = int(input("a = "))
b = int(input("b = "))
c = float(input("c = "))
d = float(input("d = "))

what = add(a, subtract(b, multiply(c, divide(d,2))))

print("That's becomes: ",what, "Can you do it by hand?")


#a+(b/c-d*3)
why = add(age, subtract(divide(height, weight), multiply(iq, 2)))

print("That's becomes: ",why, "Can you do it by hand?")