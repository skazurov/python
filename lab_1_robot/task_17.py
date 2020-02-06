#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    
    for i in range(20):
        D = direction()
        if D[4] == 1:
            move_right()
            D = direction()
            if D[4] == 1: 
                break
            else:
                move_left(2)
                break
        if D[4] == 0:
            move_up()


def direction():
     
    up = left = right = down = fill =0

    if wall_is_above() == True:
        up = 1
        
    if wall_is_on_the_left() == True:
        left = 1
        
    if wall_is_on_the_right() == True:
        right = 1
        
    if wall_is_beneath() == True:
        down = 1

    if cell_is_filled() == True:
        fill = 1

    return (up, left, right, down, fill)    


if __name__ == '__main__':
    run_tasks()
