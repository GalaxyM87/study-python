from sys import argv

script, file_name = argv

f = open('experiment.txt', 'w')

f.truncate()

line1 = "This is line 1."

line2 = "This is line 2."

#记得格式化字符串
f.write(f"{line1}\n{line2}")

f.close()

from_file = open(file_name)

print(from_file.read())
#如果读完一遍不回到最开始，就打印就是空的，必须加一个f.seek(0)，倒回最初

from_file.seek(0)

print(from_file.read())

from_file.close()