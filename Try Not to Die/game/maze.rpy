# Maze navigation system

label lv0_maze_1:
    scene lv0_maze:
        size(1920, 1080)
    "You swallow your fear and realize that you don't have much choice but to keep walking through the maze."
    "One of the most unsettling things about this place besides its state of disrepair is the sheer quiet."
    "You have heard the phrase 'silence is deafening' but didn't realize what that meant until now."
    "Even your footsteps are partially muffled by the silence. You can even hear your own heartbeat."
    "It looks like you can go right or left into the maze."

    menu:
        "Where do you turn?"

        "Turn right":
            jump lv0_maze_1_right

        "Turn left":
            jump lv0_maze_1_left

# RIGHT PATH
label lv0_maze_1_right:
    scene lv0_maze:
        size(1920,1080)
    "You head to the right but are dismayed that there is not much to see."
    "You can continue right down the path you are on or head back to the left."

    menu:
        "Which way do you go?"

        "Keep going right...":
            jump lv0_maze_2_right
        
        "Head back left":
            jump lv0_maze_1

label lv0_maze_2_right:
    scene lv0_maze:
        size(1920, 1080)
    "The path to the right looks very much like the last section you just came from."
    "You can continue to move down this right path or head back to the left."

    menu:
        "Which direction?"

        "Keep going right...":
            jump lv0_maze_3_right

        "Head left.":
            jump lv0_maze_1_right

label lv0_maze_3_right:
    scene lv0_maze:
        size(1920,1080)
    "As you continue right, you get a sinking feeling that you are becoming lost in this maze. Everything seems to look the same."
    "A short walk down this right path, you are relieved to see something different - a path leading north and a path leading south."

    menu:
        "Which Direction?"

        "Turn to the north":
            jump lv0_maze_3_right_north

        "Turn to the south":
            jump lv0_maze_3_right_south

        "Go Back left":
            jump lv0_maze_2_right

label lv0_maze_3_right_north:
    scene lv0_maze_birds:
        size(1920,1080)
    "In this section of the maze, there is a large open clearing. You feel a strange wind rustling the grass at your feet."
    "Above you, you see a strange sight - birds. Or at least they look like birds."
    "Small bird-like creatures flit in and out of the sky aroud you. They rarely come close enough to be seen, but when they do, you notice they are partially transluscent."
    "The air is filled with the sounds of a strange birdsong. It's ethereal and calming at the same time. Almost like human voices, but more distant."
    "You feel yourself relax as though all the chaos of this labyrinth was somehow far away. Maybe this is a safe place."

    menu:
        "What do you want to do?"

        "Listen to the song longer...":
            jump lv0_birds_01
        
        "Head back to where you came from":
            jump lv0_maze_3_right

label lv0_maze_3_right_south:
    scene lv0_maze_deadend:
        size(1920,1080)
    "As you turn to the south, you find that the maze does not continue further."
    "Although the walls spread out a bit, there does not appear to be any other way out but the way you came."

    menu:
        "Go Back":
            jump lv0_maze_3_right

label lv0_birds_01:
    scene lv0_maze_birds:
        size(1920,1080)
    "You decide to listen longer to the singing of the birds. It's the first chance you have had to relax since you arrived."
    "Their song grows louder amidst the deep silence of the rest of the maze."
    "You start to find yourself getting a bit tired. Perhaps you could stay a little longer and rest?"

    menu:
        "Listen Longer?"

        "Yes":
            jump lv0_birds_02
        
        "No":
            jump lv0_maze_3_right

label lv0_birds_02:
    scene lv0_maze_birds:
        size(1920,1080)
    "You continue to listen to the birds sing. The sound is so soothing that you find yourself lying down in the grass as the ethereal birds fly around overhead."
    "Soon, your body is so heavy that you can't move it anymore. You don't want to leave and you now realize that you can't."

    menu: 
        "Sleep":
            jump lv0_bird_death

# LEFT PATH
label lv0_maze_1_left:
    scene lv0_maze:
        size(1920,1080)
    "The maze path is old, unkept, and covered with vines. Despite this disrepair, the path itself is paved with cobbles and is walkable."
    "The path continues to wind off to the left for what seems like a long distance."
    "You can continue walking left or turn back to the right."

    menu:
        "Where do you want to go?"

        "Keep going left":
            jump lv0_maze_2_left

        "Go back":
            jump lv0_maze_1

label lv0_maze_2_left:
    scene lv0_maze:
        size(1920, 1080)
    "The path winds on to the left but the scenery does not change much."
    "What strikes you as the most unusual thing besides the disrepair of the place is the sheer silence."
    "You have heard the term 'silence is deafening' but this is the first time you understood what it meant."
    "You can continue heading left or turn back."

    menu:
        "Where do you want to go?"

        "Continue left.":
            jump lv0_maze_3_left

        "Head back.":
            jump lv0_maze_1_left

label lv0_maze_3_left:
    scene lv0_maze:
        size(1920,1080)
    "The left path ends here but there are two paths ahead. One path turns to the north and the other to the south."
    "You may choose to go north, south, or back the way you came."

    menu:
        "Which way?"

        "Turn north.":
            jump lv0_maze_3_left_north

        "Turn south.":
            jump lv0_maze_3_left_south

        "Go back.":
            jump lv0_maze_2_left

# NORTH PATH FROM LEFT
label lv0_maze_3_left_north:
    scene lv0_maze:
        size(1920,1080)
    "This path appears to meander slowly north and west with a small upward slope."
    "The place is so quiet that you swear you can hear your heart beating."
    "You can continue north or go back where you came from."

    menu:
        "Which way?"

        "Keep going north.":
            jump lv0_maze_3_left_north_2

        "Head back.":
            jump lv0_maze_3_left

label lv0_maze_3_left_north_2:
    scene lv0_maze:
        size(1920,1080)
    "The path continues heading to the north and west but appears to have flattened out slightly."
    "You are starting to feel like you have lost all sense of direction."
    "From here you can continue going north or head back."

    menu:
        "Which way?"

        "Keep going north.":
            jump lv0_maze_3_left_north_3

        "Head back.":
            jump lv0_maze_3_left_north

label lv0_maze_3_left_north_3:
    scene lv0_maze:
        size(1920,1080)
    "The path continues to travel north but is now almost heading straight north."
    "At least, that's how it feels to you, your own internal compass is completely muddled now."
    "You can keep heading north or head back."

    menu:
        "Which way?"

        "Keep going north.":
            jump lv0_maze_3_left_north_4

        "Head back.":
            jump lv0_maze_3_left_north_2

label lv0_maze_3_left_north_4:
    scene lv0_maze:
        size(1920,1080)
    "Much to your dismay, this path continues onward with no real change in the scenery."
    "You have begun to lose all sense of time and direction."
    "You can continue going north or head back."

    menu:
        "Which way?"

        "Keep going north.":
            jump lv0_maze_3_left_north_5

        "Head back.":
            jump lv0_maze_3_left_north_3

label lv0_maze_3_left_north_5:
    scene lv0_maze:
        size(1920,1080)
    "At this junction, the path branches two ways."
    "You can continue heading north or head to the left."
    
    menu:
        "Which way?"

        "Keep going north.":
            jump lv0_maze_3_left_north_6

        "Head left":
            jump lv0_maze_3_left_north_5_left

        "Go Back":
            jump lv0_maze_3_left_north_4
            
label lv0_maze_3_left_north_5_left:
    scene lv0_maze:
        size(1920,1080)
    "Nothing new is visible in this section of the maze. Everything looks exactly the same."
    "You can go back where you came from or you can keep heading left."

    menu:
        "Which way?"

        "Go Back":
            jump lv0_maze_3_left_north_5

        "Keep Going Left":
            jump lv0_maze_3_left_north_5_left_2

label lv0_maze_3_left_north_5_left_2:
    scene lv0_maze_deadend:
        size(1920,1080)
    "You find that the path dead ends here. There is no where else to go but back the direction you came."

    menu:
        "Go Back":
            jump lv0_maze_3_left_north_5_left

label lv0_maze_3_left_north_6:
    scene lv0_maze:
        size(1920,1080)
    "The scenery does not change much. Just as the rest of this god-foresaken maze, you feel like it's just vines, hedges, and cobbles."
    "The only directions you can go are north or back where you came"

    menu:
        "Keep Going North":
            jump lv0_maze_3_left_north_7
        
        "Go Back":
            jump lv0_maze_3_left_north_5

label lv0_maze_3_left_north_7:
    scene lv0_maze:
        size(1920,1080)
    "The path seems to widen out a bit here. Though the maze still feels enclosed and tight, you can't shake the feeling that things are bigger here."
    "Up ahead, the path opens to what appears to be a large space with decrepit but functional walls."
    "You can keep heading to this open air space or head back the way you came."

    menu:
        "Head to the open space ahead.":
            jump lv0_maze_auditorium

        "Go back the direction you came":
            jump lv0_maze_3_left_north_6

label lv0_maze_3_left_south:
    scene lv0_maze_deadend:
        size(1920,1080)
    "You turn south and follow the winding path. The hedges here seem even more overgrown than before."
    "As you come around the corner, you find that it is just a dead end. There is nowhere to go but back the way you came."
    
    menu:
        "Go Back":
            jump lv0_maze_3_left