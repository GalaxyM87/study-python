#for 后面
the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

# Same as above 
for fruit in fruits:
    print(f"A fruit of types: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print("id(i): ",id(i)) #在这里是在列表中取元素，然后存入地址，我在这里查看每个元素的地址
    print(f"I got {i}")

# we can also bulid lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0,6):
    print(f"Adding {i} to the list")
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print(f"Elements was: {i}")

#for结束循环以后，会将最后一个值传给变量，那么变量的值即为遍历中最后一个值，和函数不同，函数结束后变量会被释放


#列表的地址
print("id(the_count): ", id(the_count))
print("id(fruits): ", id(fruits))
print("id(change): ", id(change))


#range(a,b)其实不是并不是列表格式，但是可以转换成列表
listrange = list(range(1,10))
print(listrange)

#string.split()默认可以消除字符串之间的空格，并写成列表
string = "a b c  n "
str_change = string.split(' ')
print(str_change)
