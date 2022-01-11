#运行时在命令行输入python ex13.py 参数1，参数2，参赛3
#argv得到一个参数向量，里面第一个为脚本的名称，后面的为输入的参数
#和input()不同的地方是argv要在命令行把参数给定，input()是在它出现的地方输入参数
from sys import argv
#read the WYSS section for how to run this
script, first, second, third = argv
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print(argv)