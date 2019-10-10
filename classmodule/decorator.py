#!/usr/bin/env python
#encoding=UTF-8


import time


@time_count
def loop_time(x,y):
    temp_result=0
    for i in range(x,y):
        time.sleep(random.choice(0.1,0.2,0.3))
        temp_result=x+y
        return temp_result

loop_time(1,10)
loop_time(1,10)
loop_time(1,10)