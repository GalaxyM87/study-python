#utf-8是一个可变字符集，根据具体字符来决定所占的字节数（分为1，2，3，4个字节）
#比如常见的英文字母，只需要占1个字节=8位，那么中文需要三个字节=24位
#utf-16与utf-8不同，只有两种分类，两个字节or四个字节，但存储中文只需要2个字节，比utf-8更省空间
import sys 
script, encoding, error = sys.argv
#只按顺序读取一行

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:  #一个判断语句，line中有内容为TURE，继续执行下面，没有内容为FALSE，跳出函数
        print_line(line, encoding,errors)
        return main(language_file, encoding, errors) #在函数中调用函数，有跳到main()函数的一开始,在这里是否加return好像没什么影响


def print_line(line, encoding, errors):
    next_lang = line.strip()  #删掉每一行结尾的\n  我得到的是字符串
    #字符串编码得到字节串（你有一堆字母abcd，你肯定要编码咯）
    #字节串以十六进制显示《=》八位的二进制数字
    raw_bytes = next_lang.encode(encoding, errors = errors)   
    cooked_string = raw_bytes.decode(encoding, errors = errors)    #字节串解码到字符串（你有一堆数字01001011，你肯定要解码咯）

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding = "utf-8")

main(languages, encoding, error)