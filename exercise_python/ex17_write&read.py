from sys import argv
from os.path import exists
#从命令行输入的两个文件名中读取我需要复制的文件名和需要复制到的文件名
script, from_file, to_file = argv
#从from_file的文件复制到to_file的文件中
print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line,how?
#in_file是指针，指向from_file这个文件，我可以有任何一个名称的指针，比如把峻烽插到腾云里
in_file = open(from_file,'r',encoding='UTF-8')
#把from_file文件内容存进indata
indata = in_file.read()
print(">>>>indata:",repr(indata))
print(f"The input file is {len(indata)} bytes long")
#检测我要复制到的文件存不存在，exists(to_file)给出结果Ture of False
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
#又是一个用户友好的命令，继续就随便打一个字符，不继续就CTRL-C终止
input()
#添加一个指针指向to_file这个文件，然后将indata内容写进to_file这个文件里
out_file = open(to_file, 'w', encoding='UTF-8')
out_file.write(indata)

print("Alright, all done.")
#跟关闭保存时一个意思
out_file.close()
in_file.close()
#注意运行的时候要创建一个txt文件，命令行：echo"This is a text file.">text.txt
#用cat命令显示这个文件
# 文件或者本来就有一个txt文件