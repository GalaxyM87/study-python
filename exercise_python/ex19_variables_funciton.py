#函数中的变量和脚本里的变量之间是没有联系的
#函数中的变量只在这个函数里面有意义，函数外面没有任何意义，不能被打印，也不可以被操作，它只在它自己的世界里
#定义一个函数，包含两个参数，然后利用这两个参数进行一系列操作
import numpy as np
def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print(f"<<<<< cheese_count= {cheese_count},boxes_of_crackers= {boxes_of_crackers}")
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party")
    print("Get a blanket. \n")
    print(">>>> exit")

#直接输入两个参数给函数用
print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

#这里创建了两个全局变量amount_of_cheese,amount_of_crackers，然后将这两个全局变量传进函数
#这两个变量在函数之外，我传进函数以后，这个函数复制他们两个变量的值，传给另外两个函数中的变量，函数运行结束就会重置函数的参数变量
#尽量避免像amount_of_cheese,amount_of_crackers这样的全局变量和函数中的变量名字相同，这样就会导致两个混淆
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)


print("And we can combine the two, variables and math:")
#我们发现在运行这个函数的时候，cheese_count变成了110，boxes_of_crackers变成了1050
#这告诉我们函数在运行时只是提取了两个全局变量的值，然后经过运算把他们赋值给了函数中的变量cheese_count和boxes_of_crackers
#不会影响函数外面的全局变量，也不会产生新的全局变量
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)
#》》》》》》》》》注意：不可以打印函数中的变量，它只在函数中才有意义
#》》》》》》》》》print(cheese_count)

#换一种方式运行这个函数
#try1 = int(input("Please write a number from 0-10\t"))
#try2 = int(input("Please write a number from 10-20\t"))
#cheese_and_crackers(try1,try2)
#注意这一点，函数中参数的名称最好不要和定义的全局变量一样，这样就会让人迷惑到底是全局变量还是函数的参数
#def f(x):
#    return(x**2)
#a=np.arange(1,10,1)
#print(a)
#print(f(a))