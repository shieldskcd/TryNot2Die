# Try Not to Die - Ren'Py Adventure Game
# Main initialization file

# Initialize the death counter
default death_count = 0

# Screen overlay to show death counter
screen death_counter():
    text "Deaths: [death_count]" xalign 0.02 yalign 0.02 size 30 color "#ffffff"

# Game start
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