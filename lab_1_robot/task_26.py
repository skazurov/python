#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():

    for i in range(5):
        fill_row()
        if i < 4:
            move_down(4)
        else:
            break

def fill_row():
    for i in range(1, 45, 5):
        make_cross()
        move_right(4)

    make_cross()
    move_left(36)
    
def make_cross():
    move_right()
    fill_cell()
    move_down()
    fill_cell()
    move_right()
    fill_cell()
    move_left()
    move_down()
    fill_cell()
    move_up()
    move_left()
    fill_cell()
    move_up()


if __name__ == '__main__':
    run_tasks()
