#coding:utf-8

op_type={
    '1':'加法',
    '2':'减法',
    '3':'乘法',
    '4':'除法'
}#字典

def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    assert b != 0
    return a / b

def menu():
    """
    打印菜单
    :return:
    """
    print('1.加法运算')
    print('2.减法运算')
    print('3.乘法运算')
    print('4.除法运算')
    print('\n')

if __name__ == '__main__':
    while True:
        print('\n\n开启计算模式...')
        menu()
        op_type_index_str = input('请输入菜单上的数字进行运算：')
        op_type_index =int(op_type_index_str)

        if op_type_index not in [1,2,3,4]:
            print('输入的数字错误')
            continue
        print('你选择了%s运算' %op_type[op_type_index_str])
        input_a = input('请输入第一个参数a: ')
        input_a = int(input_a) #类型转换
        print('第一个参数a为： ',input_a)

        input_b = input('请输入第二个参数b: ')
        input_b = int(input_b)  # 类型转换
        print('第一个参数b为： ',input_b)
        print('运算结果：')

        if op_type_index ==1:
            print(add(input_a,input_b))
            continue
        elif op_type_index ==2:
            print(subtract(input_a,input_b))
            continue
        elif op_type_index ==3:
            print(multiply(input_a,input_b))
            continue
        elif op_type_index ==4:
            print(divide(input_a,input_b))
            continue
        else:
            continue
