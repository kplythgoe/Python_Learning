def turn_right():
    turn_left()
    turn_left()
    turn_left()

#Ensuing robot doesn't end up in infinite loop
while front_is_clear():
    move()
turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        if not wall_in_front():
            move()
    elif not wall_in_front():
        move()
    else:
        turn_left()

    