# Auditorium area

label lv0_maze_auditorium:
    scene lv0_maze_auditorium:
        size(1920,1080)
    "You feel a sense of relief at finally seeing something besides just overgrown hedges and cobbles."
    "Before you stands the ruins of what must have, at one time, been a stunning outdoor theatre. Though much of the ground is choked by weeds and thorns, you can imagine what it must have looked like at one time."
    "There are a few remnants of broken sitting areas and shattered balconies, but you see what appears to be the remnants of a stage in the center of this space."

    menu:
        "What do you want to do?"

        "Head to the stage":
            jump lv0_maze_auditorium_stage

        "Head to the shattered balcony":
            jump lv0_maze_auditorium_balcony

        "Visit the orchestra pit":
            jump lv0_maze_auditorium_orchestra

        "Go back":
            jump lv0_maze_3_left_north_7

label lv0_maze_auditorium_stage:
    scene lv0_maze_auditorium_stage:
        size(1920,1080)
    "This is a strange sensation. When standing on the stage, you feel like you can almost imagine what it must have been like to be an actor here."
    "You can imagine the place restored to its old glory and being surrounded by huge audiences that were the guest of whatever this place is."
    "You feel a lingering since of nostalgia for a thing that you don't believe ever happened to you."

    menu:
        "What do you do?"

        "Continue Imaging":
            jump lv0_maze_auditorium_stage_memory
        
        "Ignore the feeling and keep investigating":
            jump lv0_maze_auditorium

label lv0_maze_auditorium_stage_memory:
    scene lv0_maze_auditorium_memory:
        size(1920,1080)
    "You are there! It's like a memory you had long since forgotten! You stand before a huge crowd of people and all of them are watching you."
    "They came for a show and it is your job to give it to them! But what kind of attraction did they come to see?"

    menu:
        "What part will you play?"

        "Sing a glorius song":
            jump lv0_maze_auditorium_stage_memory_song

        "Speak the lines of a gripping drama":
            jump lv0_maze_auditorium_stage_memory_drama

        "Get off the stage":
            jump lv0_maze_auditorium_stage_memory_leave

label lv0_maze_auditorium_stage_memory_leave:
    scene lv0_maze_auditorium_memory:
        size(1920,1080)
    "You turn to leave but realize what a shame that would be. The people came here to hear for your performance! Give them something!"

    menu:
        "What do you give the people?"

        "Sing a glorious song.":
            jump lv0_maze_auditorium_stage_memory_song

        "Speak the lines of a gripping drama":
            jump lv0_maze_auditorium_stage_memory_drama

        "Get off the stage":
            jump lv0_maze_auditorium_stage_attacked

label lv0_maze_auditorium_stage_attacked:
    scene lv0_maze_auditorium_attacked:
        size(1920,1080)

    "The people are not going to leave yoy alone! Now the people have grown hostile. You were supposed to give them a show and now you are trying to leave?"
    "To your abject horror, the people begin swarming over the stage. You are attacked from every possible angle. You have no idea how you can escape."
    "You can lay down and hope you are assumed dead. You can also try to fight back. Running will get you nowhere."

    menu:
        "What do you want to do?"

        "Fight Back":
            jump lv0_maze_auditorium_stage_death
        
        "Lay Down":
            jump lv0_maze_auditorium_stage_death
        
        "Try to Run":
            jump lv0_maze_auditorium_stage_death

# STUB LABELS - Need implementation
label lv0_maze_auditorium_stage_memory_song:
    scene lv0_maze_auditorium_memory:
        size(1920,1080)
    "You open your mouth to sing, and a beautiful melody flows from your lips. The crowd is enraptured."
    "The ghostly audience applauds enthusiastically. You feel the memory beginning to fade..."
    "As the vision dissipates, you find yourself back on the ruined stage."
    
    menu:
        "What now?"
        
        "Explore more of the auditorium":
            jump lv0_maze_auditorium
            
        "Leave the auditorium":
            jump lv0_maze_3_left_north_7

label lv0_maze_auditorium_stage_memory_drama:
    scene lv0_maze_auditorium_memory:
        size(1920,1080)
    "You recite lines from a play you didn't know you remembered. Your voice echoes powerfully across the phantom crowd."
    "The spectral audience hangs on every word. As you finish your monologue, they rise in standing ovation."
    "The memory fades, and you're left alone on the crumbling stage once more."
    
    menu:
        "What now?"
        
        "Explore more of the auditorium":
            jump lv0_maze_auditorium
            
        "Leave the auditorium":
            jump lv0_maze_3_left_north_7

label lv0_maze_auditorium_balcony:
    scene lv0_maze_auditorioum:
        size(1920,1080)
    "You climb up the crumbling steps to what remains of the balcony seating."
    "From here, you have a better view of the entire theatre. The decay is even more apparent from this vantage point."
    "There really is nothing to see here except a different view of the auditorium."
        
    menu:
        "Return to the main floor":
            jump lv0_maze_auditorium

label lv0_maze_auditorium_orchestra:
    scene lv0_maze_auditorium_orchestra:
        size(1920,1080)
    "You descend into the orchestra pit. Old, broken instruments lie scattered about."
    "A violin with no strings. A flute split in two. The remains of what might have been a grand piano."
    "You hear a faint melody, as if the ghost of music still lingers here."
    
    menu:
        "What do you want to do?"
        
        "Touch one of the instruments":
            "As your fingers brush the violin, the eerie melody grows louder for a moment, then fades."
            jump lv0_maze_auditorium_orchestra_play
            
        "Leave the orchestra pit":
            jump lv0_maze_auditorium

label lv0_maze_auditorium_orchestra_play: 
    scene lv0_maze_auditorium_orchestra:
        size(1920,1080)
    "You feel as though you are being overwhelemed with a sense of some memory that you can't quite describe."
    "It feels as though you remember a life when you were a skilled musician. You were always asked to play with the orchestra when 
    a play was performed."
    "In fact, you feel like you could play something right now."

    menu:
        "What do you do?"

        "Sit and play the instrument":
            jump lv0_maze_auditorium_orchestra_play_2
        
        "Walk away, this place is just getting to you.":
            jump lv0_maze_auditorium_orchestra

label lv0_maze_auditorium_orchestra_play_2:
    scene lv0_orchestra_play:
        size(1920,1080)
    "You take a seat and find the insrument in your hands is now fully formed. It is a beautiful violin made of the finest materials."
    "All around you, you see the musicians lift their instruments as the conductor motions to start the movemnt."
    "The lights of the stage flood in and the music swells as though the actors will take the stage soon."

    menu:
        "What should you do?"

        "Keep playing":
            jump lv0_maze_auditorium_play_3
        
        "Stop Playing":
            jump lv0_maze_orchestra_cant_stop

label lv0_maze_auditorium_play_3:
    scene lv0_orchestra_play:
        size(1920,1080)
    "You feel the music swell and you feel the light notes of a solo bouncing off the piano."
    "You are slightly dizzy with the sudden events all occuring at once, yet you feel like you are doing something you love."
    "You must be good because you feel like you know that you have a solo coming up."

    menu:
        "What do you do?"

        "Play your solo":
            jump lv0_maze_auditorium_play_4
        
        "Stop playing":
            jump lv0_maze_orchestra_cant_stop

label lv0_maze_auditorium_play_4:
    scene lv0_orchestra_play:
        size(1920,1080)

    "You hit every note perfectly! Even if you don't remember being able to play the violin before, you can absolutely play it now."
    "You feel a sense of pride that you are performing so well and notice that even the other orchestra members have started playing a bit softer
    so that your solo can be heard."
    "However, your fingers are starting to hurt a little, this is a lot of activity to suddenly start after wandering through a maze."

    menu:
        "Now what?"

        "End the solo, but keep playing":
            jump lv0_maze_auditorium_play_f

        "Stop playing.":
            jump lv0_maze_orchestra_cant_stop

label lv0_maze_auditorium_play_f:
    scene violin_death:
        size(1920,1080)

    "Your fingers continue to throb as you play the instrument. You notice that some blood has begun trickling off your fingers."
    "In horror, you realize that you cannot remove your fingers from the instrument and the blood is being absorbed into the instrument from your fingers."
    "The pain in your arm intensifies and you feel your vision blurring. All the while, the blood continues to leak into the instrument."

    menu:
        "Continue playing...forver...":
            jump lv0_maze_auditorium_violin_death
