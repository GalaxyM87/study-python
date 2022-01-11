def f1():
    a = 2
    b = 2
    c = a + b 
    d = 4
    
    print(id(a))
    print(id(b))
    print(id(c))
    print(id(4))
def f2():
    a = 2
    print(id(a))
f2()
print(id(3))
print(id(2))
#a = 2
#print(id(a))
#f1()
#print(id(2))