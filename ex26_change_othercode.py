#记得导入这个包
from sys import argv
script, filename = argv


print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
#这个地方括号没有打完
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

#这里的filename打成了filenme,而且编码格式也记得改一下
txt = open(filename, encoding='utf-8')

#这里要格式化字符串
print(f"Here's your file {filename}:")

#这里少打了一个字
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

#这里为txt_again.read()
print(txt_again.read())

#如果在单引号的句子里面放单引号需要转义
print('Let\'s practice everything.')
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
#这里引号没有加全
print("--------------")
print(poem)
print("--------------")

#数字没有写全
five = 10 - 2 + 3 - 3
#print()没有写全
print(f"This should be five: {five}")

#定义函数没有加冒号
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars * 100   #这个操作无效 
    return jelly_beans, jars, crates

#函数有三个返回值，如果只赋给两个变量是不行的
start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
#少写了_
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cats = 30
dogs = 15

#这里的变量名和前面的不同，需要改正
if people < cats:
    print ("Too many cats! The world is doomed!")  #打印需要print加（）

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

#这里没有冒号
if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

#同样没有加冒号
if people <= dogs:
    print("People are less than or equal to dogs.")

#==才是判断
if people == dogs:
    print("People are equal to dogs.")
