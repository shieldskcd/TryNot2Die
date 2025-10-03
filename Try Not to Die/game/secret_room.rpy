# Secret room and clock room content

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

label inspect_walls:
    scene clock_room:
        size (1920, 1080)
    "You approach the walls and run your hand along the white veins."
    "They pulse with a faint warmth. The pattern seems almost organic, like blood vessels."
    "As you trace one vein, you realize it leads deeper into the room."
    
    menu:
        "What now?"
        
        "Follow the vein":
            "TO BE CONTINUED..."
            jump secret_door_enter
            
        "Step back":
            jump secret_door_enter

label inspect_gears:
    scene clock_room:
        size (1920, 1080)
    "You kneel down and pick up one of the gears. It's surprisingly light for its size."
    "The metal is cold and engraved with tiny symbols you don't recognize."
    "You notice that some of the gears seem to still be moving, clicking slowly even though they're disconnected."
    
    menu:
        "What now?"
        
        "Try to fit gears together":
            "TO BE CONTINUED..."
            jump secret_door_enter
            
        "Put the gear down":
            jump secret_door_enter

label walk_forward:
    scene clock_room:
        size (1920, 1080)
    "You carefully step over the scattered gears and walk forward."
    "The room stretches on further than you initially thought. In the distance, you see a faint blue glow."
    
    menu:
        "What now?"
        
        "Approach the glow":
            "TO BE CONTINUED..."
            jump secret_door_enter
            
        "Turn back":
            jump secret_door_enter