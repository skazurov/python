#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    

    move_down()
    make_cross()
    
    move_right(4)
    make_cross()
    move_right(4)
    make_cross()
    move_right(4)
    make_cross()
    move_right(4)
    make_cross()


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
