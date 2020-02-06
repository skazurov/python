#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_7():

    for i in range(36):

        move_right()

        D = direction()

        if sum(D) == 0:
            break
        
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
