def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():
        if right_is_clear():
            turn_right()
            move()
        else:
            move()
    elif wall_in_front():
        if right_is_clear():
            turn_right()
            move()
        else:
            turn_left()

#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json