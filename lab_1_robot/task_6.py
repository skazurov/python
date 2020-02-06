#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_3():

    start = end = 0

    for i in range(18):

        if start == 0 and around() == True:
            move_right()
        if start == 0 and around() == False:
            start = 1
        if start == 1 and around() == False:
            move_right()
        if start == 1 and around() == True:
            end = 1
        if start == 1 and end == 1:
            break

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
