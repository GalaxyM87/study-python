#创建一个函数，功能是生成一个列表，步长为i, 起始值为a, 终止值为b。
def test(a, b, i):
    numbers = []
    while i < a:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + b
        print("Numbers now: ",numbers)
        print(f"At the bottom i is {i}")

    return(numbers)
np_arange = test(100, 2, 0)
print(np_arange)