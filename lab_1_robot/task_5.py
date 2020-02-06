#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_2():
    for i in range(8):
        if around() == True:
            break
        else:
            move_right()

def around():

    r = l = u = d = 0
        
    if wall_is_above() == True:
        u = 1
    if wall_is_on_the_left() == True:
        l = 1
    if wall_is_on_the_right() == True:
        r = 1
    if wall_is_beneath() == True:
        d = 1

    if u == 0 and l == 0 and r == 0 and d ==0:
        return True
    else:
        return False

if __name__ == '__main__':
    run_tasks()
