#coding:utf-8
"""
这是一个标准结构的hello world
"""
#导入模块
import os
#全局变量
g_var=100
class FooClass(object):
    """
    这是一个示例类
    """
    def __init__(self):
        self.a=1
        self.b=2
    def add(self):
        return self.a + self.b

def add_fun(a,b):
    print(a)
    print(b)
    return a + b

def get_current_path():
    path=os.path.abspath('.')
    return path
if __name__ == '__main__':
    print('hello world')
    c = add_fun(3,24)
    print(c)

    cur_path = get_current_path()
    print(cur_path)
