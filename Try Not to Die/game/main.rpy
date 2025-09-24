# Try Not to Die - Ren'Py Adventure Game
# A death-loop puzzle adventure

# Initialize the death counter
default death_count = 0

# Screen overlay to show death counter
screen death_counter():
    text "Deaths: [death_count]" xalign 0.02 yalign 0.02 size 30 color "#ffffff"

# Setup animation for the eyes
#image overlook_animated = Movie("overlook_animated.webm", loop=True)

# Show the counter on all screens
label start:
    show screen death_counter
    scene forest:
        size (1920,1080)
    "You fought your way through the massive forest and now find yourself staring at a labyrinth."
    "According to your sensors, this is the place where you last saw the energy signal."
    
    menu:
        "Will you Enter the Labyrinth? OR Turn Back?"
        
        "Enter the Labyrinth":
            jump labyrinth_entrance
            
        "Turn Back":
            jump cannot_turn_back

label cannot_turn_back:
    "You cannot turn back! The path through the forest has already disappeared. You cannot pass that way now."
    jump labyrinth_entrance

label labyrinth_entrance:
    scene courtyard:
        size (1920, 1080)

    "You pass through the stone archway and into the courtyard of the labyrinth."
    "Up ahead you see a decrepit fountain."
    "To your right, you see a stone bench."
    "To your left, you see a worn pathway out of the courtyard."
    
    menu:
        "Where will you go?"
        
        "To the Fountain":
            jump fountain_area
            
        "To the Bench":
            jump bench_area

        "To the Left":
            jump level0_left
            
        "Go Back":
            jump cannot_turn_back

label fountain_area:
    scene fountain:
        size (1920, 1080)
    "You walk up to a decrepit fountain. It's murky brown water reeks of dead fish."
    "The water flow has long since stopped."
    
    menu:
        "Where do you go?"
        
        "Back to the Courtyard":
            jump labyrinth_entrance
            
        "Look at the Fountain":
            jump look_at_fountain

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
            jump lv0_maze_3_left_north_1

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
            

label look_at_fountain:
    "You see the murky brown water in front of you. Your nose fills with the stench of death and rot."
    "You almost vomit at the odor but manage to compose yourself."
    "Something glows darkly below, you almost want to touch it..."
    
    menu:
        "What now?"
        
        "Step Back":
            jump fountain_area
            
        "Stick Your Hand In":
            jump stick_hand_in

label stick_hand_in:
    scene fountain_vortex:
        size(1920,1080)
    "You reach into the water with the smell of filth boring into your nose."
    "Your entire arm grows cold but you feel your hand drawn to the floor of the pool."
    
    menu:
        "Keep Going?"
        
        "No, pull your hand out!":
            jump death_pulled_in
            
        "Yes! No turning back now!":
            jump find_button

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

label find_button:
    scene secret_door:
        size (1920, 1080)
    "Just when you feel like you will be drawn into the blackness, your hand grazes a small button in the floor of the pool."
    "The fountain drains and you see a large door rise up from the fountain's base."
    
    menu:
        "What now?"
        
        "Go Inside":
            jump secret_door_enter
            # This is where the rest of the adventure continues

label bench_area:
    scene fountain:
        size (1920, 1080)
    "You find a stone bench. It was once white marble but now is sepia brown."
    "Pieces of the bench have cracked and fallen off."
    "Near the bench is an overlook into some dark space below."
    
    menu:
        "What now?"
        
        "Go to the overlook":
            jump overlook_area
            
        "Go to the Courtyard":
            jump labyrinth_entrance

label overlook_area:
    scene overlook:
        size(1920, 1080)
    "You approach the overlook. Over the railing, you see a pit of the blackest pitch below."
    "However, it is mysteriously dotted with red lights that seem to move about."
    "You feel an overwhelming sense of dread and a strange desire to jump."
    
    menu:
        "Now What?"
        
        "Go Back":
            jump bench_area
            
        "Jump!":
            jump death_jumped

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

# Placeholder for the secret door content
# Secret room content
label secret_door_enter:
    scene clock_room:
        size (1920, 1080)
    "You step through the secret door..."
    "You enter a strange room that seems deep underground even though you didn't feel yourself walk downward."
    "The room looks like a long disused room. The walls are dark but a pattern of white veins spreads out across all the walls."
    "The floor is littered with what appear to be broken gears from long-destroyed technology."
    "They lay about the ground in disarray with clumps of clockwork gears jutting out in random places."
    
    menu:
        "What will you do?"
        
        "Inspect the white walls":
            jump inspect_walls
            
        "Inspect the gears":
            jump inspect_gears
            
        "Walk forward in the room":
            jump walk_forward

# Placeholder labels for the new choices
label inspect_walls:
    "TO BE CONTINUED..."
    
    menu:
        "What now?"
        
        "Play Again":
            jump start
            
        "Quit":
            return

label inspect_gears:
    "TO BE CONTINUED..."
    
    menu:
        "What now?"
        
        "Play Again":
            jump start
            
        "Quit":
            return

label walk_forward:
    "TO BE CONTINUED..."
    
    menu:
        "What now?"
        
        "Play Again":
            jump start
            
        "Quit":
            return