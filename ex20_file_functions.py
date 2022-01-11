#不同函数间空行是个好习惯喔
#与上一节不同的是，上一节中函数中的变量和全局变量没有关系，只对这个函数有影响，但是对于文件来说，就好像一个真实的磁带机
#我读取文件后磁头就会往后移动，文件并不会复制，它是真实的东西，所以我们在函数中读取后它的磁头就会到相应位置
from sys import argv
#熟悉的argv命令，在命令行给它赋值，然后将argv的参数传给script和input_file
script, input_file = argv
#这里里面的f同样是一个参数（变量）
def print_all(f):
    print(f.read())
#seek(0)为倒带，转到文件的一开始，因为上一个函数读取了整个文件，等于录像带转完了一圈，我需要回到一开始才可以接着读。
#如果不运行这个函数，就会导致从第三行继续往后读，就会输出空白
def rewind(f):
    f.seek(0)
#readline会读取文件的一行，然后将“磁头”移动到这一行\n的后面，在继续往后读
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole life:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

#current_line = current_line + 1 
#等价于 current_line +=1

current_line += 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)