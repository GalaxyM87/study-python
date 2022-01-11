class Song(object):
#self是个函数
    #对新创建的空对象进行初始化
    def __init__(self,lyrics):
        #用self.xxx设置一个实例变量
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        #对这个实例变量操作
        for line in self.lyrics:
            print(line)

#将类实例化，意思就是说调用起来，右边的操作是将类实例化，然后赋给左边的变量
happy_bday = Song(["Happy birthday to you",
                    "I dont't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
