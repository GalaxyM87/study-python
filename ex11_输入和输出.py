#ex11:输入和输出
#在print后面加上end=''是提醒两个print之间不要换行
print("How old are you?",end=' ')
#input()默认格式为字符串格式
#我们要格式化输入的话，就要满足我的预设条件，如果我int(input())，那么我输入的就要是整数
# int()要把input默认的字符串转化为整数型
age = int(input())
#我们可以用repr()函数来及时查看我的age格式，这里为整数型
print(">>>>>> age=", repr(age))
print("How tall are you?",end=' ')
height = str(input())
#我们在这里发现height为字符串型
print(">>>>> height=",repr(height))
print('How much do you weight?',end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy")


