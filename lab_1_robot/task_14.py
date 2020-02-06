#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_11():
    
    for i in range(36):

        D = direction()

        if (D[0] != 1 or D[3] != 1):
            fill_outside(D[0], D[3])
        if (D[0] == 1 and D[3] == 1):
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

def fill_outside(up:int, down:int):
    if up == 0:
        move_up()
        fill_cell()
        move_down()
    if down == 0:
        move_down()
        fill_cell()
        move_up()


if __name__ == '__main__':
    run_tasks()
