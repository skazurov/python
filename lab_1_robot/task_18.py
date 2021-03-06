#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():

    left_end = 0
    
    for i in range(20):

        D = direction()

        if D[0] == 0:
            goto_exit()
            break

        if (D[1] == 1 and left_end == 0):
            move_right()
            left_end = 1

        if left_end == 0:
            move_left()
            D = direction()
            if D[1] == 1:
                left_end = 1
                if (D[1] == 1 and D[0] == 0):
                    print(D)
                    goto_exit()
                    break
                
            if D[0] == 0:
                goto_exit()
                break

        if left_end == 1:
            D = direction()
            if D[0] == 0:
                goto_exit()
                break
            move_right()
            
        
def goto_exit():
    for i in range(20):
        D = direction()
        if D[0] != 1:
            move_up()
        else:
            move_left()
            D = direction()
            if D[1] == 1:
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
