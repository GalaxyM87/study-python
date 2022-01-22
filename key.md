# 关键词的用法

## as

1.优雅的读取文件

之前用的方法:

```python
f = open("test.txt")
data = f.read()
f.close()
```

现在可以通过with + as实现,最后自动关闭文件，就算存在异常也可以关闭文件。

```python
with open("test.txt") as file:
	data = file.read()
print(data)
```

2.调用一个包，并给他一个别的名字

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

## assert

python是一行一行的读取代码，assert碰到False就会报错，报错的内容可以自己设置
例如：

```python
a = 2
assert a == 1, 'a not equal to 1.'
```

这样我就可以清晰的知道程序到哪一步不满足我的条件，并且后面的内容可以帮助我们了解错误的是什么,很有利于我们测试代码。

还有一个比较好的例子，我想看一个文件里是否是空的，空文件即为False

```python
with open("test1.txt") as file:
    data = file.read()
assert data,"This is a emtpy file"
```

## break

break用于while和for循环中，终止最深层次的循环，如果是嵌套函数，最深层次""终止""，外面的循环继续

```python
for i in range(0,3):
    for j in range(0,4):
        print(f"({i},{j})")
        if j == 1:
            break
```

预期结果：（0,0）(0,1) (1,0) (1,1) (2,0) (2,1)

第二个循环1后面的数字全部go die

## continue

continue也用于while和for循环中，最深层次的循环不是终止，而是跳出某一次循环，外面的循环继续

```python
for i in range(0,3):
    for j in range(0,4):
        print(f"({i},{j})")
        if j == 1:
            continue
```

预期结果：(0,0) (0,1) (0,2) (0,3) (1,0) (1,1) (1,2) (1,3) (2,0) (2,1) (2,2) (2,3)，和没有continue没区别

因为打印后才跳出去，不改变打印的结果，需要更换打印和判断的顺序

```python
for i in range(0,3):
    for j in range(0,4):
        if j == 1:
            continue
        else:
            print(f"({i},{j})")
```

预计结果：(0,0) (0,2) (0,3) (1,0) (1,2) (1,3) (2,0) (2,2) (2,3)

这样调换顺序以后就会影响j == 1那次循环的print

## pass

创建一个空的代码块，供我们以后使用，对于我们搭框架应该是有帮助的

```python
def empty():
    pass
```

## finally

不管是否发生异常，都运行此处代码
下面为示例代码，不论怎样最后都关闭文件

```python
try:
    f = open("test.txt")
    data = int(f.read())
    print(data)
finally:
    f.close()
    print("The file is closed")
```


预期结果：会在data = data = int(f.read())报错，但是finally中的句子会被执行，会打印"The file is closed"。


我们在try后面加入except，在try中出现错误后，会跳到except中执行代码，但不会影响finally中的代码，会继续运行

```python
try:
    f = open("test.txt")
    data = int(f.read())
    print(data)
except:
    print("The file is not a int")
finally:
    f.close()
    print("The file is closed")
```

## try + except + else + finally

try的工作原理是，当开始一个try语句后，python就在当前程序的上下文中作标记，这样当异常出现时就可以回到这里，try子句先执行，接下来会发生什么依赖于执行时是否出现异常。

1. 如果当try后的语句执行时发生异常，python就跳回到try并执行第一个匹配该异常的except子句，异常处理完毕，控制流就通过整个try语句（除非在处理异常时又引发新的异常）。
2. 如果在try后的语句里发生了异常，却没有匹配的except子句，异常将被递交到上层的try，或者到程序的最上层（这样将结束程序，并打印默认的出错信息）。
3. 如果在try子句执行时没有发生异常，python将执行else语句后的语句（如果有else的话），然后控制流通过整个try语句。

总结一下，try中没有错误执行下面的else，有错误执行它旁边最近的except。

### except捕获某种特定的错误

- 使用try-except语句可以让try无论出现哪种错误都执行except中的操作，但我们并不知道具体是哪种错误，

  这样就可以确定抓取的是某一种类型的错误


```python
a = "xyz"
try:
    data = int(a)
except ValueError:
    print("you are not a int string")
else:
    print("type(data)")

```
- 使用except语句也可以捕获多种错误，满足其一就执行except语句，利用except(a,b,.....):

```python
a = "xyz"
try:
    data = int(a)
except (ValueError,IndexError):
    print("you are not a int string")
else:
    print("type(data)")

```

- except + as 将异常赋值
  
```python
a = "2.4"
try:
    data = int(a)
except (ValueError,IndexError) as e:
    print(f"{e} are not a int string")
else:
    print("type(data)")

```
- 当然也可以接受所有的异常值

```python
a = "2.4"
try:
    data = int(a)
except Exception as e:
    print(f"{e} are not a int string")
else:
    print("type(data)")

```

### 利用raise手动触发异常

- raise Exception

```python
x = 10
if x > 5:
    raise Exception(f'''
    x 不能大于 5,
    x 的值为: {x}.
    ''')
```
- raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类，即可以触发特定类型的异常

```python
x = 10
if x > 5:
    raise ValueError(f'''
    x 不能大于 5,
    x 的值为: {x}.
    ''')
```

- 在try中触发异常

```python
try:
    raise Exception
```

### 一个完整的测试结构

```python
try:
    runoob()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('这句话，无论异常是否发生都会执行。')
```

## global

- 如果需要在函数中修改某一个全局变量，可以使用 global 变量名

```python
a = 13
def test(a):
    global b
    b = a**13
test(a)
print(b)
```

预期结果 ： 169

- 其实等价于在函数中的return,在函数外面赋值

```python
a = 13
def test(a):
    return(a**2)
b = test(a)
print(b)
```
- 但感觉return不会混淆局部变量和全局变量，会更加清晰

## lambda

- 短匿名函数，用的很少，但是语法比较简洁

```python
d = lambda x : x/2
print(d(3))
```

- 等价于def函数
  
```python
def divide(x):
    return(x / 2)
print(divide(3))
```