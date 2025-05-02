from karel.stanfordkarel import *

"""
Each row starts with a stack of beepers. Karel should pick them
up, one at a time, and spread them down the row. 
Caution! Karel can't count, and starts with infinite beepers in
her bag. How can you solve this puzzle?
"""


def main():
    move()
    do_one_row()
    turn_left()
    while front_is_clear():
        move()
        turn_right()
        move()
        do_one_row()
        turn_left()
    move_to_base()
    turn_right()

def do_one_row():
    while beepers_present():
        pick_beeper() # pick one beeper
        if beepers_present():
            while beepers_present():
                move()
            put_beeper()
            move_to_base()
            move()
        else:
            fix_fench_post()


def fix_fench_post():
    if no_beepers_present():
        put_beeper()
        move_to_base()


def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def move_to_base():
    turn_around()
    while front_is_clear():
        move()
    turn_around()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
