#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():

    fill_row()

    while wall_is_beneath() == False:
        move_down()
        fill_row()
    
def fill_row():

        fill_cell()
    
        while wall_is_on_the_right() == False:
            
            move_right()
            fill_cell()
         
        while wall_is_on_the_left() == False:
            move_left()


if __name__ == '__main__':
    run_tasks()
