#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_1():
    while wall_is_on_the_right() != True:
        move_right()
    move_left()
    move_right()

if __name__ == '__main__':
    run_tasks()
