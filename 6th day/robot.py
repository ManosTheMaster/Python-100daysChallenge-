def pass_a_hurlder():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while at_goal() != True:
    while front_is_clear() and at_goal() != True:
        move()

    while wall_in_front():
        pass_a_hurlder()