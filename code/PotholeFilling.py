"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    for i in range(3):
        go_in()
        put_99()
        go_out()
def go_in():
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
def put_99():
    for i in range(99):
        put_beeper()
def go_out():
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()

















####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
