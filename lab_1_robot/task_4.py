#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():

    r = l = u = d = 0
        
    if wall_is_above() == True:
        u = 1
    if wall_is_on_the_left() == True:
        l = 1
    if wall_is_on_the_right() == True:
        r = 1
    if wall_is_beneath() == True:
        d = 1
      
    if u == 1 and l == 1 and r == 1 and d == 0:
        move_down()
    if u == 0 and l == 1 and r == 1 and d == 1:
        move_up()
    if u == 1 and l == 0 and r == 1 and d == 1:
        move_left()    
    if u == 1 and l == 1 and r == 0 and d == 1:
        move_right()


if __name__ == '__main__':
    run_tasks()
