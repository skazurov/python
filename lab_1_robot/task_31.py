#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    
    e = True
    
    while e:
        e = False
        while not wall_is_on_the_right():
            move_right()
            while not wall_is_beneath():
                move_down()
                e = True
        while not wall_is_on_the_left():
            move_left()
            while not wall_is_beneath():
                move_down()
                e = True

if __name__ == '__main__':
    run_tasks()
