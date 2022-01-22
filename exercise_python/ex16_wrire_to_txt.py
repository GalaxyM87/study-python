from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN")
#提示用户是否确定写入文件，ctrl_c会终止文件，其他的文字都可以
input("?")

print("Opening the file...")
#以w（write）模式来打开文件，默认的是r（read）模式,还有a(append)模式
#"w"模式如果没有这个文件，它会创建filename这个文件，但是没有"w",它不会进行写入操作
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
#truncate()为清空文件
target.truncate()

print("Now I'm going to ask you for three lines.")
#将line1,2,3的值分别传入line1,2,3三个变量
line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print("I'm going to write these to the file.")
#将内容写入txt文件
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
#用一行替换掉之前的六行
target.write(f"{line1}\n{line2}\n{line3}")   #转义字符结合格式化写入

print("And finally, we close it.")
#不要忘记close()文件
target.close()