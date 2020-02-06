#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
    for i in range(36):

        D = direction()

        if D[0] == 0 and D[3] == 1:
            fill_cell()

        if D[2] == 1:
            break
        
        move_right()

def direction():
     
    up = left = right = down = 0

    if wall_is_above() == True:
        up = 1
        
    if wall_is_on_the_left() == True:
        left = 1
        
    if wall_is_on_the_right() == True:
        right = 1
        
    if wall_is_beneath() == True:
        down = 1

    return (up, left, right, down)


if __name__ == '__main__':
    run_tasks()
