#我自己写了一个脚本，✌
#函数下面的"""    """是对于这个函数的注释
def break_words(stuff):
    """This fuction will break up words for us."""
    print(">>>>>sentence: ", stuff)
    words = stuff.split(' ')  #将字符串中间的空格全部去掉,将值赋给words后，外面的变量是没有变化的
    print(">>>>>sentence: ", words)
    return words

def sort_words(words):
    """Sorts the words"""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)         #但是这一步确实对于外面的变量是有作用，删除了第一个元素
    print("words: ",words)
    print(word)
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
