# Courtyard and surrounding areas

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

# FOUNTAIN AREA
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

label find_button:
    scene secret_door:
        size (1920, 1080)
    "Just when you feel like you will be drawn into the blackness, your hand grazes a small button in the floor of the pool."
    "The fountain drains and you see a large door rise up from the fountain's base."
    
    menu:
        "What now?"
        
        "Go Inside":
            jump secret_door_enter

# BENCH AREA
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