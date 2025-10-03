# Statue area and interactions

label level0_left:
    scene level0_left:
        size(1920,1080)
    "You are now in what appears to be an old hedgerow. It is overgrown and in disrepair like the rest of the environment so far."
    "You can't help but wonder what this place must have looked like back when it was maintained. Perhaps it was a grand outdoor theatre?"
    "Along all sides, you can see more overgrown trees and vines strangling the old stone facades."
    "You can inspect the statue if you'd like."
    "You can also continue on the path beyond the statue."

    menu:
        "What do you want to do?"

        "Inspect the Statue":
            jump lv0_statue

        "Head Past the Statue":
            jump lv0_statue_behind

label lv0_statue:
    scene level0_statue:
        size(1920, 1080)
    "You approach the statue, it is old and worn down by time. It depicts a man in armor holding a spear. He wears a helmet with an open spot for his eyes."
    "His eyes have been worn down over time and there are two small holes where his eyes used to be."
    "The man's body is covered with armor from a different time including pauldrons, a breastplate, a belt, chainmail pants, and covered boots"
    "His appearance reminds you of the pictures you had seen of a Roman guard from ancient history."
    "It looks like you could touch the statue, poke its eyes, or walk past it."

    menu:
        "What will you do?"

        "Touch the Statue":
            jump lv0_statue_touch

        "Poke the statues eyes":
            jump lv0_statue_poke_eyes

        "Walk Past the Statue":
            jump lv0_statue_behind

        "Leave now.":
            jump labyrinth_entrance

label lv0_statue_touch:
    scene level0_statue:
        size(1920,1080)
    "You don't know why you are inclined to push this statue but you do so. It offers all the resistance one might expect from a statue."
    "Your actions don't even cause the statue to move at all. It is as though it is far stronger and heavier than one might expect from a derelict statue."
    "Why would you want to push the statue anyway?"

    menu:
        "What next?"

        "Poke the statue's eyes":
            jump lv0_statue_poke_eyes

        "Walk behind the Statue":
            jump lv0_statue_behind

        "Go Back":
            jump lv0_statue

label lv0_statue_poke_eyes:
    scene level0_statue:
        size(1920,1080)
    "Why would you do such a thing to an ancient statue? Are you some kind of monster? This statue has been standing here forever and never hurt you."
    "Your fingers gently touch the eye sockets of the statue, it feels like cold stone. However, there is a strange warmth at the very center."

    menu:
        "Take your fingers out?"
            
        "Yes":    
            jump lv0_statue

        "No":
            jump lv0_statue_eyes_death

label lv0_statue_eyes_death:
    scene lv0_statue_arm:
        size(1920, 1080)
    "You leave your fingers in the eye sockets of the statue. The warmth you had felt now begins to tingle up your arm through your hand."
    "To your horror, a gray mist climbs up your arm from the eyes of the statue. As it climbs your arm, you feel your senses dulling."
    "Try as you may, your arm will not come loose from the eye sockets. You start to feel pain and agony grow throughout your body."
    "All you can do is scream..."

    menu:
        "Scream":
            jump lv0_statue_eyes_death_2

label lv0_statue_eyes_death_2:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "You try to scream but nothing comes out because your insides are now becoming stone just like your outsides."
    "In a moment of clarity, you realize that you will become a statue now."
    "You have died.."
    
    menu:
        "What now?"
        
        "Try Again":
            jump start

label lv0_statue_behind:
    scene lv0_statue_behind:
        size(1920,1080)
    "You walk behind the statue and see an open archway in a rear wall. The archway has become overgrown with vines, but you feel like you could go through the arch if you wanted."
    "The time-worn statue stands behind you, unmoving."
    "Would you like to turn back now? Or go through the archway?"

    menu:
        "Where will you go?"

        "Turn back":
            jump lv0_statue
        
        "Go through the archway":
            jump lv0_garden_arch

label lv0_garden_arch:
    scene lv0_maze:
        size(1920, 1080)
    "You pass through the stone archway. The vines tear at your clothes and prick you with thornes, but you find you are only a little worse for wear."
    "Beyond the arch, you find an overgrown hedge maze. It seems to wind on forever. Perhaps it's not too late to go back?"
    "You can try to go back through the arch or you can head forward into the maze."

    menu: 
        "Where do you want to go?"

        "Go Back...":
            jump lv0_maze_no_backwards

        "Move foward.":
            jump lv0_maze_1

label lv0_maze_no_backwards:
    scene lv0_maze:
        size(1920,1080)
    "Your blood chills as you realize that the archway you came through is gone. There is no turning back now."

    menu:
        "Head Forward":
            jump lv0_maze_1