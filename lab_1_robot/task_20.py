#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():

    d = k = 0
    
    for i in range(300):
      
        move_right()
        fill_cell()
        k +=1

        if k == 27:
            move_down()
            fill_cell()
            d += 1
            for i in reversed(range(k-1)):
                move_left()
                fill_cell()
            k = 1
            move_down()
            d += 1
            if d == 12:
                break 
            fill_cell()


if __name__ == '__main__':
    run_tasks()
