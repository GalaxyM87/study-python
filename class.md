# python中class（类）的学习

## 1.字典
- python存储数据就是以字典形式，globals()本质上就是以字典形式返回所有的变量
- 那么我们想创建一个新的变量自然可以在globals()这个字典对象里创建key，value，key即为变量名，value即为变量值

```python
x = 1
y = 1
globals()['a'] = 12
```

- 之前词汇统计实例代码为：

```python
type=['NOUN','VERB','ADJ','ADV','CCONJ','PROPN']
    for ty in type:                                          
        globals()['astro'+ty]=  []                              
        globals()['astro'+ty+'ct']=[]                           
        words = wordcount[ty]                                   
        wordlist = list(words.items())                          
        wordlist.sort(key=lambda x:x[1],reverse=False)          
        i = wordlist.__len__()
        if i > 10 : i = 10
        while i > 0:
            globals()['astro'+ty].append(wordlist[-i][0])        
            globals()['astro'+ty+'ct'].append(wordlist[-i][1])   
            i = i-1 
```

## 2.继承

### 隐式继承

如果我有一个父类，我可以完全继承我的父类，我在子类里不需要定义任何东西，这成为隐式继承

```python
class Parent(object):
    
    def implict(self):
        print("PARENT implicit()")
        
class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implict()
son.implict()
```

结果会输出

```console
PARENT implicit()
PARENT implicit()
```

这时候son完全继承了Parent()中的函数，Parent()也叫做基类，我们可以把一些共性的函数放到里面，所有子类将自动获得这些属性，但也要慎重。



### 显式覆盖

如果我希望子类中的函数覆盖父类中的函数，我可以在子类中定义一个跟它同名的函数，这样我在利用我子类这个函数的时候，就不会调用我父类中那个同名的函数。

```python
class Parent(object):
    
    def override(self):
        print("PARENT override()")

class Child(Parent):
    
    def override(self):
        print("CHILD override()")
        
dad = Parent()
son = Child()

dad.override()
son.override()
```

结果会输出

```console
PARENT override()
CHILD override()
```



## super()

如果说我希望在父类中定义的内容运行之前或者之后在调用子类中的内容，就可以用super()

```python
class Parent(object):
    
    
    def __init__(self):
        self.initial = "THERE IS A VOCABULARY"
        
    def altered(self):
        print("PARENT altered()")
        print(self.initial)
        
class Child(Parent):
    
    def __init__(self)
    	self.initial = "2222"
        
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super.altered()
        print("CHILD, AFTER PARENT altered()")
        
dad = Parent()
son = Child()

dad.altered()
son.altered()
```

预计结果：

```console
PARENT altered()
THERE IS A VOCABULARY
CHILD, BEFORE PARENT altered()
PARENT altered()
2222
CHILD, AFTER PARENT altered()
```

实际结果：

```console
PARENT altered()
THERE IS A VOCABULARY
CHILD, BEFORE PARENT altered()
PARENT altered()
2222
CHILD, AFTER PARENT altered()
```

结果分析：

```console
son = Child()
son.altered()
```

将类Child实例化，然后调用类Child中的altered函数，以self为参数，需要注意的一点是我们利用的self.initial是在子类中定义的initial，并不是父类中的initial。



三种方式的混合应用

```python
class Parent(object):
    
    def override(self):
        print("PARENT override()")
        
    def implict(self):
        print("PARENT implict()")
        
    def altered(self):
        print("PARENT altered()")
    
class Child(Parent):
    
    #覆盖了父类中的override()函数
    def override(self):
        print("CHILD override()")
        
    #覆盖了父类中的altered()函数
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        
        #调用父类中的altered()函数
        #在python3中直接输入super().即可调用父类
        super().altered()
        print("CHILD, AFTER PARENT altered()")

#将类Parent，和类Child实例化
dad = Parent()
son = Child()

dad.implict()
son.implict()

dad.override()
son.override()

dad.altered()
son.altered()
```





## super()和 __init__ 配合使用

```python
class Parent(object):
    
    def __init__(self):
        self.int1 = "INT1"
        self.int2 = "INT2"
        
class Child(Parent):
    
    #记住一点，在__init__(self, stuff)中的stuff是传进去的参数，但是self.stuff中的stuff可以说是一个	key，self就像一个字典，和python存储数据的格式十分相似。
    def __init__(self,stuff):
        self.stuff = stuff
        #虽然说在子类中的__init__()覆盖了父类中的__init__()，
        #但通过super()我们依旧可以实现父类中的初始函数__init__()
        super().__init__()
    def printf(self):
        print(self.int1)
        print(self.int2)
        print(self.stuff)
name = Child("Andy")
name.printf()
```

预期结果：

```python
INT1
INT2
Andy
```

## 组合

两个类的组合，并非继承，不是子类继承父类，比如A是B，A = class(B)，而是A里有B。

```python
class Other(object):
    
    def override(self):
        print("OTHER override()")
        
    def implict(self):
        print("OTHER implict()")
        
    def altered(self):
        print("OTHER altered()")
        
class Child(object):
    
    def __init__(self):
        self.other = Other()
     
    def implict(self):
        self.other.implict()
    
    #和类Other中的override()函数没有关系
    def override(self):
        print("CHILD override()")
    
    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")
        
#son为Child的一个实例
son = Child()

son.implict()
son.override()
son.altered()
```

以上 Other 和 Child 关系就是一个组合关系，Child里面有一个Other来实现它的功能，通过组合我们也能够实现另一个类中的函数功能，当然继承也可以。

预计结果：

```console
OTHER implict()
CHILD override()
CHILD, BEFORE OTHER altered()
OTHER altered()
CHILD, AFTER OTHER altered()
```



核心思想：**代码复用**

继承和组合都可以实现代码复用，但要避免多重继承，这会让代码更复杂，比如A = class(B, C)。
