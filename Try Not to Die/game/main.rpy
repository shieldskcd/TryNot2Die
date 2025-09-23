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