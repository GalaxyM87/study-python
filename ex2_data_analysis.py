#定义一个阶乘函数，他将对列表里面每个元素进行阶乘，并放在另一个列表中
def factorial(x):
    """
    函数可以处理整数或者列表对象,最终返回一个整数或者ndarray类型
    """
    import math as m
    if type(x) == int:
        return(m.factorial(x))
    else:
        import numpy as np
        xx = []
        for i in range(len(x)):
            final = m.factorial(x[i])
            xx.append(final)
        xx = np.array(xx)
    return xx

def binomial_distribution(x,n,p):
    """
    x:需要计算成功的实验次数
    n:二项分布的总试验次数
    p:每次实验成功的概率
    最后返回值为概率
    
    """
    probability = factorial(n) / (factorial(x) * factorial(n-x)) * p**x * (1-p)**(n-x)
    return(probability)