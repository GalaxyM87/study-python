from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
#txt.read()命令告诉txt执行read命令
print(txt.read())

print("Type the filename again:")
#和argv相比，用input命令传入file_name
file_again = input("> ")
#再次打开ex15_sample.txt
txt_again = open(file_again)
#打印txt_again读取的内容
print(txt_again.read())
txt.close()
txt_again.close()