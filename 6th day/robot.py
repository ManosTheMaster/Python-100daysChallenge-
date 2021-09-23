#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
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