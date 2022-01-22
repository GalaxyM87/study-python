#在input()中写字符串内容可以在输入时提示
age = input("How old are you? ")
#我们还可以将上面的变量，用到下面的格式化字符串中
height = input(f"You're {age}? Nice. How tall are you? ")
weight = input("How much do you weight? ")
#不要忘记格式化f-strings

print(f"So, you're {age} old, {height} tall and {weight} heavy.")