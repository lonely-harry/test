#coding:utf-8
"""
python 代码基础
"""
def hello_world():
    print('hello world')

def debug_demo():
    """
    断点调试示例
    :return:
    """
    a =1
    b =2
    c =a + b
    print(c)
    return c

def for_demo():
    astring ='hello tom'
    str_len = len(astring)
    print(str_len)
    for i in range(str_len):
        print(astring[i])

    file = open('aaa.txt','w')
    for i in range(20):
        a = 'your are not smart~! in Line:%d\n' % i
        file.write(a)
        print(a)
    file.close()

if __name__ == '__main__':
    # debug_demo()
    for_demo()
    print('end')

