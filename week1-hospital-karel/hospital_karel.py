from karel.stanfordkarel import *

# Here is a place to program your Section problem

# Move while front is clear
# Condition: If beepers present call the function build hospital
# Define the function to build a hospital: for loop with 3 moves
# Decompose build hospital to a helper function of doing just one column
# After doing one column change direction

def main():
    while front_is_clear():
        move()
        if beepers_present():
            build_hospital()


def build_hospital():
    build_one_column()
    move()
    put_beeper()
    build_one_column()



def build_one_column():
    turn_left()
    for i in range(2):
        move()
        put_beeper()
    move_to_base()
    turn_left()


def move_to_base():
    turn_left()
    turn_left()
    while front_is_clear():
        move()


def turn_right():
    for i in range(3):
        turn_left()




if __name__ == '__main__':
    main()
