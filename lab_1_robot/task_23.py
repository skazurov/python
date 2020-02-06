#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():

    step = 0
    
    while wall_is_on_the_right() == False:
        
        move_right()
    
        D = direction()

        if (D[0] == 0 and D[3] == 1):
            go_to_hallway()

        step += 1

    for i in reversed(range(step)):

        move_left()
        step -= 1

def go_to_hallway():

    while wall_is_above() == False:

        move_up()
        fill_cell()
        
    fill_cell()
    
    while wall_is_beneath() == False:
        move_down()

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
