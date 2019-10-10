#coding:utf-8

def egg_take():
    """
    一篮鸡蛋：
    一次拿4个，最后剩下1个
    一次拿5个，最后剩下4个
    一次拿6个，最后剩下3个
    一次拿7个，最后剩下5个
    一次拿8个，最后剩下1个
    一次拿9个，最后刚好拿完
    请问：一篮鸡蛋最少有几个？
    :return:
    """
    res_file = open('egg.txt','w')
    for i in range(1000):
        if i % 4 != 1:
            continue
        if i % 5 != 4:
            continue
        if i % 6 != 3:
            continue
        if i % 7 != 5:
            continue
        if i % 8 != 1:
            continue
        if i % 9 != 0:
            continue
        print(i)
        res_file.write('%d\n' % i)
    res_file.close()
if __name__ == '__main__':
    # debug_demo()
    egg_take()


