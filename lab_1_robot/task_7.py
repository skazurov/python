#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():

    start = end = j = 0

    for i in range(36):

        D = direction()

        if sum(D) == 0 and end == 1:
            for i in range(j):
                move_left()
            break
        
        if sum(D) == 0 and end == 0:
            move_down()
            end = 1
       
        if (D[1] == 1 and D[3] == 1) or (D[1] == 0 and D[3] == 1):
            start = 1
            j += 1
            move_right()

        if D[3] == 0 and D[1] == 1:
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
