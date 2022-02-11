from math import factorial
import matplotlib.pyplot as plt
import numpy as np
from sympy import oo

class Binomial(object):

    #需要发生的概率p,q作为参数初始化
    def __init__(self,p,q):
        self.p = p
        self.q = q
    
    def probability(self,n,x):
        """请输入实验次数n,和希望得到的事件次数x,可以得到发生的概率P"""
        P = factorial(n) / (factorial(x)*factorial(n-x)) * self.p**x *self.q**(n-x)
        print(f"Probability is {P}")
        return P

    def plot(self,n):
        """请输入试验次数n,可以得到二项分布图样"""
        x = np.arange(0,n+1,1)
        P = []
        for ex in x:
            p = self.probability(n,ex)
            P.append(p)
        
        xx = np.arange(0,n+1,0.01)
        PP = []
        
        plt.plot(x,P)
        plt.xlabel(f"n = {n}")
        plt.savefig("binomial.png")
        
        plt.show()
        
    def mean(self,n):
        """请输入试验次数n"""
        me = n * self.p
        print(f"平均值为{me}")

    def variance(self,n):
        """请输入试验次数n"""
        va = n * self.p * self.q
        print(f"平均值为{va}")


class  Poisson(object):

    def __init__(self,attribute):

        if type(attribute) == np.ndarray:
            self.array = attribute
            self.mean = np.mean(self.array)

        elif type(attribute) == int:
            self.mean = attribute

        else:
            print("请输入样本数据或者要拟合的泊松分布参数")
        
    def mean(self):
        """得到样本的平均数"""
        self.mean = np.mean(self.array)
        print(f"平均值为:{self.mean}")

    def possion_distribution(self,x):
        """请输入想要得到的次数,即可得到对应的概率"""

        p = (self.mean)**x / factorial(x) * np.exp(-self.mean)
        print(f"{x}的概率为{p}")
        return p

    def summed(self,x1,x2):
        """计算泊松分布的和概率，请输入起始和末尾，无穷输入'wq' """
        #生成要计算的各个次数

        if x2 != "wq":
            x = np.arange(x1,x2+1,1)
            #计算各个次数的概率
            P = 0
            for count in x:
                P = P + self.possion_distribution(count)
            print(f"{x1}到{x2}的和概率为{P}")

        elif x2 == "wq" and x1 != 0:
            x = np.arange(0,x1,1)
            P = 0
            for count in x:
                P = P + self.possion_distribution(count)
            P = 1 - P
            print(f"{x1}到无穷的和概率为{P}")

        else:
            P = 1
            print(f"{x1}到无穷的和概率为{P}")
        

    def plot(self,b=None,f=None,s=None):
        #begin,finally,step
        """如果为样本数据,请输入起始次数,终止次数,步长"""
        #如果输入的为平均数，则只画出泊松分布图样
        #横坐标为测到的次数
        #纵坐标为测到的概率
        if type(self.mean) == int:
            #计算各种可能的概率
            x = np.arange(0,3*self.mean,1)
            prob = []
            for ex in x:
                p = self.possion_distribution(ex)
                prob.append(p)

            plt.plot(x,prob)
            plt.show()

        #如果输入的为样本数据，则输出样本数据的直方图和拟合的泊松图样
        #横坐标为测得的所有情况
        #纵坐标为测得这种情况的次数
        elif type(self.array) == np.ndarray:
            print(self.array)
            count = np.arange(b,f,s)
            data = self.array

            plt.hist(data,count,width=1,color='r',alpha=0.5)

            x = np.arange(b,f,s)
            prob = []
            for ex in x:
                p = self.possion_distribution(ex)
                prob.append(p)
            prob = np.array(prob)
            #n=len(data),为实验次数，\mu=np.
            mu = len(data) * prob

            plt.plot(x,mu)

            plt.show()


class Gaussian(object):

    def __init__(self,mean=None,deviation=None) :
        self.mean = mean
        self.dev = deviation

    def mean(self,data):
        self.mean = np.mean(data)

    def gaussian_distribution(self,x):
        P = 1 / (self.dev * np.sqrt(2*np.pi)) * np.exp(-0.5 * ( (x-self.mean)/self.dev )**2)
        print(f"概率为{P}")
        return P

a = Gaussian(0.635,0.020)
b= a.gaussian_distribution(0.635)
print(b*0.01*50)
