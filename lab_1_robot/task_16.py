#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_22():
    
    for i in range(9):
        D = direction()
        if (D[0] == 1 and D[1] == 1):
            for i in range(9):
                D = direction()
                if D[2] == 1:
                    break
                move_right()
            break
        if (D[0] == 1 and D[2] == 1):
            for i in range(9):
                D = direction()
                if D[1] == 1:
                    break
                move_left()
            break

        move_up()


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
