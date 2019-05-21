import re
import time
import sys

def reg(data,port):
    #匹配任意的非空字符\S,第一个单词和第二个之间有空格
    pattern=r'^\S+'
    re_obj=re.compile(pattern)
    try:
        head_word=re_obj.match(pattern,data).group()
    except Exception:
        return None
    if port==head_word:
        #.是特殊字符要使用转义
        #通过分组来获取正则表达式里面的值
        pattern=r'address is (\w{4}\.\w{4}\.\w{4})'
        try:
            match_obj=re.search(pattern,data)
            return match_obj.group(1)
        except Exception:
            return None    
    else:
        return None

def main(port):
    fd=open('1.txt','r')
    #文本的前两行没啥用先跳过
    fd.readline()
    fd.readline()
    fd.readline()
    while True:
        data=''
        while True:
            s=fd.readline()
            if s=='\n':
                break
            #break只能跳出当前循环，return跳出当前函数
            if s=='':
                print('search over')
                return
            data+=s
        #讲每段数据传入函数进行匹配
        result=reg(data,port)
        if result:
            print('address is:',result)
            return

if __name__=='__main__':
    if len(sys.argv)<2:
        print('argv error')
        sys.exit(1)
    main(sys.argv[1])

