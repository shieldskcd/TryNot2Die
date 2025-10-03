# All death scenes in one file

label death_pulled_in:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "You struggle to pull your hand out but you simply cannot break free."
    "It's as though something is pulling you in."
    "Soon, all you see is black darkness. Your body grows cold and your breath ceases."
    "You have died.."
    
    menu:
        "Try Again":
            jump start

label death_jumped:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "The madness of this place has already got you! You begin falling… falling… falling…"
    "You have died.."
    
    menu:
        "What now?"
        
        "Try Again":
            jump start

label lv0_bird_death:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "Of all the ways you could have died, this was the most peaceful. You drift into eternal slumber."
    "You have died..."

    menu:
        "Try Again":
            jump start

label lv0_maze_auditorium_stage_death:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "The ghostly audience overwhelms you. Their ethereal hands grasp at you, pulling you down."
    "You feel yourself becoming part of the memory, trapped forever in this phantom performance."
    "Your screams join the eternal chorus of the damned."
    "You have died..."

    menu:
        "Try Again":
            jump start


label lv0_maze_auditorium_violin_death:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "The pain in your fingers never relents and you find yourself passing into the darkness."
    "The eerie music continues to burn your ears until all goes black."

    menu:
        "Try Again":
            jump start