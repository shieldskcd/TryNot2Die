# Level 1 - Steampunk Machine Level
# This level features gear puzzles, steam corridors, and pendulum traps

# ENTRY POINT - Clock Room Hub
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

# VEIN/WALL PATH - Confusing loops with some deaths
label inspect_walls:
    scene clock_room:
        size (1920, 1080)
    "You approach the walls and run your hand along the white veins."
    "They pulse with a faint warmth. The pattern seems almost organic, like blood vessels."
    "As you trace one vein, you realize it leads deeper into the room."
    "The veins branch in three directions - left, right, and center."
    
    menu:
        "Which vein will you follow?"
        
        "Follow the left vein":
            jump vein_left_path
            
        "Follow the right vein":
            jump vein_right_path
            
        "Follow the center vein":
            jump vein_center_path
            
        "Step back":
            jump secret_door_enter

label vein_left_path:
    scene clock_room:
        size (1920, 1080)
    "You follow the left vein along the wall."
    "It leads you to a small alcove you hadn't noticed before."
    "The vein ends at a dead end. The walls here pulse more intensely."
    
    menu:
        "What now?"
        
        "Touch the pulsing wall":
            jump vein_absorption_death
            
        "Go back to the veins junction":
            jump inspect_walls
            
        "Return to the clock room":
            jump secret_door_enter

label vein_right_path:
    scene clock_room:
        size (1920, 1080)
    "You follow the right vein. It leads you through a narrow passage."
    "The passage gets tighter and tighter as you proceed."
    "You realize you're in a crawlspace now. The walls are pressing close."
    
    menu:
        "What will you do?"
        
        "Keep squeezing through":
            jump vein_compression_death
            
        "Back out carefully":
            jump vein_right_escape
            
        "Push forward aggressively":
            jump vein_compression_death

label vein_right_escape:
    scene clock_room:
        size (1920, 1080)
    "You carefully back out of the narrowing passage."
    "Smart choice. That passage was getting dangerously tight."
    "You return to where the veins branch."
    
    menu:
        "Try another path?"
        
        "Follow the left vein":
            jump vein_left_path
            
        "Follow the center vein":
            jump vein_center_path
            
        "Return to clock room":
            jump secret_door_enter

label vein_center_path:
    scene clock_room:
        size (1920, 1080)
    "You follow the center vein, which glows brightest of all."
    "It leads you to a circular chamber. The walls here pulse rhythmically."
    "The pulsing is hypnotic. You can almost feel your own heartbeat syncing with it."
    "Thump-thump. Thump-thump. Thump-thump."
    
    menu:
        "What now?"
        
        "Stay and listen to the rhythm":
            jump vein_pulse_death
            
        "Leave immediately":
            jump vein_center_escape
            
        "Touch the pulsing walls":
            jump vein_absorption_death

label vein_center_escape:
    scene clock_room:
        size (1920, 1080)
    "You tear yourself away from the hypnotic pulsing and hurry back."
    "As you leave, the rhythm fades from your mind."
    "That was close. You could feel yourself getting lost in it."
    "You return to the main clock room."
    
    menu:
        "Where to now?"
        
        "Back to the clock room hub":
            jump secret_door_enter

# BLUE GLOW PATH - Trap route leading to water reservoir deaths
label walk_forward:
    scene clock_room:
        size (1920, 1080)
    "You carefully step over the scattered gears and walk forward."
    "The room stretches on further than you initially thought."
    "In the distance, you see a faint blue glow growing brighter."
    "It's beautiful - almost inviting. Perhaps it's the way forward?"
    
    menu:
        "What now?"
        
        "Approach the blue glow":
            jump blue_glow_approach
            
        "Turn back":
            jump secret_door_enter

label blue_glow_approach:
    scene blue_glow_chamber:
        size (1920, 1080)
    "You walk toward the blue glow and enter a beautiful chamber."
    "The source of the light is a large pool of glowing blue water."
    "The water seems to shimmer and pulse with an inner light."
    "Steam rises gently from its surface. It's mesmerizing."
    "The chamber is peaceful and calm - a stark contrast to the chaos of the maze above."
    
    menu:
        "What will you do?"
        
        "Touch the water":
            jump blue_water_touch_death
            
        "Drink the water":
            jump blue_water_drink_death
            
        "Walk around the edge":
            jump blue_water_edge
            
        "Investigate the source":
            jump blue_water_source
            
        "Leave this place":
            jump walk_forward

label blue_water_edge:
    scene blue_glow_chamber:
        size (1920, 1080)
    "You decide to walk carefully around the edge of the pool."
    "The stone is slick with moisture. You move slowly."
    "You're halfway around when your foot slips slightly on the wet stone."
    
    menu:
        "Quick reaction!"
        
        "Catch your balance":
            jump blue_water_slip_death
            
        "Grab onto something":
            jump blue_water_slip_death
            
        "Jump back from the edge":
            jump blue_water_edge_escape

label blue_water_edge_escape:
    scene blue_glow_chamber:
        size (1920, 1080)
    "You jump back from the slippery edge just in time!"
    "That was close. The water seems to almost pull at you."
    "You back away from the pool entirely."
    
    menu:
        "What now?"
        
        "Investigate the source of the water":
            jump blue_water_source
            
        "Leave this chamber":
            jump walk_forward

label blue_water_source:
    scene water_reservoir:
        size (1920, 1080)
    "You look for where the water is coming from."
    "Behind the pool, you find a passage leading to a massive reservoir."
    "The reservoir is enormous - easily hundreds of thousands of gallons."
    "You realize this must be the water supply for the steam machinery above."
    "Massive pipes lead from the reservoir upward into the ceiling."
    "The water here churns and bubbles. It's not as peaceful as the chamber."
    
    menu:
        "What will you do?"
        
        "Get closer to the reservoir":
            jump reservoir_approach_death
            
        "Touch the water here":
            jump reservoir_touch_death
            
        "Go back to the glowing chamber":
            jump blue_glow_approach
            
        "Leave and try another path":
            jump walk_forward

# GEAR PUZZLE PATH - The correct but dangerous route to Level 2
label inspect_gears:
    scene clock_room:
        size (1920, 1080)
    "You kneel down and pick up one of the gears. It's surprisingly light for its size."
    "The metal is cold and engraved with tiny symbols you don't recognize."
    "You notice that some of the gears seem to still be moving, clicking slowly even though they're disconnected."
    "Around the room, you see several mounting points on the walls where gears could potentially fit."
    
    menu:
        "What now?"
        
        "Try to fit gears together":
            jump gear_puzzle_attempt
            
        "Examine the symbols more closely":
            jump gear_symbols_examine
            
        "Put the gear down and step back":
            jump secret_door_enter

label gear_symbols_examine:
    scene clock_room:
        size (1920, 1080)
    "You hold the gear up to what little light exists in this underground chamber."
    "The symbols are etched deeply into the metal - they look almost like numbers, but not quite."
    "Some symbols have dots, others have lines. You notice three gears nearby have matching symbol sets."
    "Perhaps the symbols indicate how the gears should connect?"
    
    menu:
        "What will you do?"
        
        "Try matching symbols":
            jump gear_puzzle_attempt
            
        "Look for more gears":
            jump gear_search_more
            
        "This seems too complex, go back":
            jump secret_door_enter

label gear_search_more:
    scene clock_room:
        size (1920, 1080)
    "You search through the scattered clockwork, finding several more gears of varying sizes."
    "Each one has different symbol patterns. You count at least a dozen distinct gears."
    "On the far wall, you notice a large mounting frame with five empty slots arranged in a specific pattern."
    "The frame seems to be the key mechanism for something important."
    
    menu:
        "What now?"
        
        "Approach the mounting frame":
            jump gear_mounting_frame
            
        "Keep searching for clues":
            jump gear_search_clues
            
        "Go back to the entrance":
            jump secret_door_enter

label gear_search_clues:
    scene clock_room:
        size (1920, 1080)
    "You carefully examine the walls, looking for any hints about how the gears should be arranged."
    "Behind a collapsed section of wall, you find a faded brass plaque with five symbols arranged in sequence."
    "The plaque is tarnished and hard to read, but you can make out most of the markings."
    "This must be the solution key!"
    
    menu:
        "What will you do?"
        
        "Try to match gears to the plaque sequence":
            jump gear_mounting_frame
            
        "Ignore the plaque, figure it out yourself":
            jump gear_mounting_frame
            
        "This is too risky, go back":
            jump secret_door_enter

label gear_mounting_frame:
    scene gear_puzzle_room:
        size (1920, 1080)
    "You stand before the large mounting frame. Five circular slots wait for the correct gears."
    "The slots are arranged in a cross pattern - one in the center, four surrounding it."
    "You gather the gears you think might fit. Each slot seems to be a different size."
    "You can hear a faint grinding sound coming from behind the wall - something mechanical is waiting."
    
    menu:
        "How will you proceed?"
        
        "Start with the center gear":
            jump gear_center_first
            
        "Start with the outer gears":
            jump gear_outer_first
            
        "Try random placement":
            jump gear_random_death
            
        "Walk away from this puzzle":
            jump secret_door_enter

label gear_puzzle_attempt:
    scene clock_room:
        size (1920, 1080)
    "You gather several gears and examine them closely."
    "On the far wall, you notice a large mounting frame with empty slots."
    "This must be where the gears need to go."
    
    menu:
        "What will you do?"
        
        "Examine the frame more closely":
            jump gear_mounting_frame
            
        "Try to place gears randomly":
            jump gear_random_death
            
        "Look for clues first":
            jump gear_search_clues

label gear_outer_first:
    scene gear_puzzle_room:
        size (1920, 1080)
    "You decide to start with the outer gears, placing them one by one in the surrounding slots."
    "The first gear clicks into place with a satisfying sound. So far so good."
    "The second gear also fits well. You feel confident now."
    "As you place the third outer gear, you hear clicking from within the wall."
    
    menu:
        "Continue?"
        
        "Place the fourth outer gear":
            jump gear_outer_continue
            
        "Stop and place the center gear first":
            jump gear_center_correction
            
        "Remove the gears and start over":
            jump gear_mounting_frame

label gear_center_correction:
    scene gear_puzzle_room:
        size (1920, 1080)
    "You decide to correct your approach and place the center gear before finishing the outer ones."
    "You select a heavy brass gear and place it in the center slot."
    "It clicks into place. Now you add the final outer gear."
    "All five gears begin rotating smoothly together!"
    "A section of the wall behind the frame begins to slide open."
    
    menu:
        "What now?"
        
        "Approach the opening carefully":
            jump gear_passage_careful
            
        "Rush through immediately":
            jump gear_passage_rush

label gear_outer_continue:
    scene gear_puzzle_room:
        size (1920, 1080)
    "You place the fourth outer gear confidently."
    "Immediately, all four outer gears begin spinning in place."
    "You reach for the center gear, but the spinning outer gears are moving too fast!"
    
    menu:
        "What now?"
        
        "Try to place center gear anyway":
            jump gear_timing_death
            
        "Wait for them to stop":
            jump gear_wait_trap
            
        "Pull out the outer gears":
            jump gear_removal_attempt

label gear_removal_attempt:
    scene gear_puzzle_room:
        size (1920, 1080)
    "You reach for one of the spinning outer gears, trying to pull it free."
    "It's stuck fast, locked into place by some mechanism you can't see."
    "The spinning gear is generating heat from friction. Your fingers burn as you touch it."
    
    menu:
        "What now?"
        
        "Try harder to remove it":
            jump gear_burn_death
            
        "Look for a release mechanism":
            jump gear_release_search
            
        "Try to place the center gear":
            jump gear_timing_death

label gear_release_search:
    scene gear_puzzle_room:
        size (1920, 1080)
    "You frantically search the frame for any kind of release lever or button."
    "Your fingers trace along the brass edges, feeling for anything out of place."
    "There! A small indentation near the base of the frame."
    "You press it hard. The outer gears immediately stop spinning."
    
    menu:
        "What now?"
        
        "Remove the outer gears and start fresh":
            jump gear_mounting_frame
            
        "Try to place the center gear now":
            jump gear_center_with_outer
            
        "Step back and reconsider":
            jump gear_mounting_frame

label gear_center_with_outer:
    scene gear_puzzle_room:
        size (1920, 1080)
    "With the outer gears in place but stopped, you carefully place the center gear."
    "It slides in smoothly. For a moment, nothing happens."
    "Then all five gears begin to rotate in harmony - slowly at first, then faster."
    "A section of the wall begins to slide open behind the frame!"
    
    menu:
        "What will you do?"
        
        "Approach the opening immediately":
            jump gear_passage_rush
            
        "Wait and watch":
            jump gear_passage_watch
            
        "Check if the gears are safe first":
            jump gear_passage_careful

label gear_center_first:
    scene gear_puzzle_room:
        size (1920, 1080)
    "You decide the center gear must be the key. You select what you think is the right gear."
    "The center slot is the largest, and you find a heavy brass gear that seems to match."
    "You lift it carefully - it's surprisingly heavy - and lower it into the center slot."
    "It clicks into place with a deep, resonant sound."
    
    menu:
        "What now?"
        
        "Place the outer gears":
            jump gear_center_then_outer
            
        "Wait and see what happens":
            jump gear_center_wait
            
        "Remove it and try a different approach":
            jump gear_mounting_frame

label gear_center_wait:
    scene gear_puzzle_room:
        size (1920, 1080)
    "You step back and watch the center gear."
    "It sits motionless in its slot. Nothing seems to be happening."
    "After a few moments, you hear a faint ticking sound coming from deep within the wall."
    "The ticking grows louder. Is this good or bad?"
    
    menu:
        "What will you do?"
        
        "Place the outer gears quickly":
            jump gear_center_then_outer
            
        "Remove the center gear":
            jump gear_center_removal
            
        "Keep waiting":
            jump gear_center_wait_death

label gear_center_removal:
    scene gear_puzzle_room:
        size (1920, 1080)
    "You reach for the center gear, trying to pull it free before something bad happens."
    "It won't budge! It's locked into place."
    "The ticking grows even louder. You have seconds to act!"
    
    menu:
        "Quick! What do you do?"
        
        "Place outer gears immediately":
            jump gear_center_then_outer
            
        "Pull harder on center gear":
            jump gear_pull_death
            
        "Run away from the frame":
            jump gear_escape_attempt

label gear_center_then_outer:
    scene gear_puzzle_room:
        size (1920, 1080)
    "Quickly, you grab four smaller gears and begin placing them in the outer slots."
    "First gear - click. Second gear - click. The ticking continues steadily."
    "Third gear - click. Fourth gear - CLUNK."
    "The ticking stops. All five gears begin rotating smoothly together."
    "A section of the wall behind the frame grinds open, revealing a dark passage."
    
    menu:
        "What will you do?"
        
        "Enter the passage immediately":
            jump gear_passage_rush
            
        "Examine the passage first":
            jump gear_passage_careful
            
        "Wait to see if anything else happens":
            jump gear_passage_watch

label gear_passage_watch:
    scene gear_corridor_open:
        size (1920, 1080)
    "You wait and observe the passage carefully."
    "The five gears continue rotating. After exactly three rotations, you notice something."
    "The gears lining the passage walls stop spinning for a brief moment - maybe two seconds."
    "Then they start again. This pattern repeats every three rotations of the main gears."
    "That must be your window to cross safely!"
    
    menu:
        "What now?"
        
        "Wait for the next pause and run":
            jump gear_passage_timing
            
        "Look for another way":
            jump gear_passage_alternate
            
        "Go back to the clock room":
            jump secret_door_enter

label gear_passage_alternate:
    scene gear_corridor_open:
        size (1920, 1080)
    "You search around the passage entrance for any other option."
    "Along the bottom, you notice a narrow crawlspace beneath the spinning gears."
    "It looks barely wide enough for a person to squeeze through."
    "But if the timing is off, those gears will crush you."
    
    menu:
        "What will you do?"
        
        "Try the crawlspace":
            jump gear_crawl_death
            
        "Wait for the gear pause instead":
            jump gear_passage_timing
            
        "Go back and look for another path":
            jump secret_door_enter

label gear_passage_timing:
    scene gear_corridor_open:
        size (1920, 1080)
    "You watch the main gears carefully. One rotation. Two rotations. Three..."
    "The passage gears stop!"
    "You sprint forward into the corridor. The passage is about twenty feet long."
    "You're halfway through when you hear the gears starting to spin again behind you."
    
    menu:
        "Run faster!"
        
        "Sprint to the end":
            jump gear_passage_timing_success
            
        "Dive forward":
            jump gear_passage_timing_success

label gear_passage_timing_success:
    scene gear_corridor_open:
        size (1920, 1080)
    "You push your legs as hard as they'll go!"
    "The whirring of gears grows louder behind you."
    "With a final leap, you dive through the exit just as the gears spin back to full speed."
    "You made it! You're through the gear corridor."
    "Ahead, you see what looks like a steam-filled hallway."
    
    menu:
        "What now?"
        
        "Proceed into the steam corridor":
            jump steam_corridor_entrance
            
        "Rest here a moment":
            jump gear_passage_rest
            
        "Try to go back":
            jump gear_passage_no_return

label gear_passage_rest:
    scene gear_corridor_open:
        size (1920, 1080)
    "You take a moment to catch your breath."
    "Behind you, the gear corridor continues its deadly rotation. There's no going back that way."
    "Your heart rate slowly returns to normal. The steam corridor ahead waits."
    
    menu:
        "Ready to continue?"
        
        "Yes, proceed forward":
            jump steam_corridor_entrance

label gear_passage_no_return:
    scene gear_corridor_open:
        size (1920, 1080)
    "You look back at the gear corridor you just traversed."
    "The gears are spinning at full speed now. Even if you timed it perfectly, you're not sure you could make it back."
    "The only way is forward."
    
    menu:
        "Proceed to the steam corridor":
            jump steam_corridor_entrance

label gear_passage_careful:
    scene gear_corridor_open:
        size (1920, 1080)
    "You approach the opening cautiously, peering inside before committing."
    "Smart move. You immediately see that the walls are lined with spinning gears."
    "If you had rushed in, you'd be dead already."
    "You watch carefully and notice the gears pause briefly every few seconds."
    
    menu:
        "What will you do?"
        
        "Time your crossing carefully":
            jump gear_passage_timing
            
        "Look for another way through":
            jump gear_passage_alternate
            
        "Go back to the clock room":
            jump secret_door_enter

# STEAM CORRIDOR - Second major challenge after gears

label steam_corridor_entrance:
    scene steam_corridor:
        size (1920, 1080)
    "You step into a long corridor filled with steam and heat."
    "Brass pipes line both walls, some hissing and leaking pressurized steam."
    "The air is thick and hot. Sweat immediately begins pouring down your face."
    "You can see pressure gauges on the pipes - some are in the red zone."
    "The corridor extends about thirty feet ahead to a dark doorway."
    
    menu:
        "How will you proceed?"
        
        "Walk quickly down the center":
            jump steam_center_walk
            
        "Hug the left wall":
            jump steam_left_wall
            
        "Hug the right wall":
            jump steam_right_wall
            
        "Study the pipes first":
            jump steam_study_pipes

label steam_study_pipes:
    scene steam_corridor:
        size (1920, 1080)
    "You take a moment to study the pipes more carefully."
    "The left wall pipes all have gauges in the green or yellow zones - relatively safe."
    "The right wall pipes show red gauges, and you can see steam actively venting from several ruptures."
    "The center of the corridor has grating on the floor. Below the grating, you can see more pipes."
    "Walking on the left side seems safest, but you'd be close to the wall."
    
    menu:
        "What's your choice?"
        
        "Take the left wall path":
            jump steam_left_wall_careful
            
        "Risk the center":
            jump steam_center_walk
            
        "Maybe the right wall is a bluff?":
            jump steam_right_wall

label steam_center_walk:
    scene steam_corridor:
        size (1920, 1080)
    "You walk down the center of the corridor, staying equidistant from both walls."
    "The grating beneath your feet feels sturdy enough."
    "You're about ten feet in when you hear a loud HISS from below."
    "One of the pipes under the grating has ruptured!"
    
    menu:
        "Quick reaction!"
        
        "Jump to the left":
            jump steam_left_jump
            
        "Jump to the right":
            jump steam_right_death
            
        "Keep moving forward":
            jump steam_center_death

label steam_left_jump:
    scene steam_corridor:
        size (1920, 1080)
    "You leap to the left just as scalding steam erupts through the grating!"
    "You land hard against the left wall, but you're safe from the steam."
    "Your heart pounds as you realize how close that was."
    "The left wall path seems to be the safer route after all."
    
    menu:
        "Continue along the left wall?"
        
        "Yes, proceed carefully":
            jump steam_left_wall_careful
            
        "Wait for the steam to stop":
            jump steam_wait_death

label steam_left_wall:
    scene steam_corridor:
        size (1920, 1080)
    "You decide to hug the left wall, keeping away from the dangerous right side."
    "You move carefully, placing each foot deliberately."
    "The pipes here are warm but not dangerously hot."
    "You're about halfway through when you notice the corridor ahead narrows slightly."
    
    menu:
        "What now?"
        
        "Keep going along the wall":
            jump steam_left_wall_careful
            
        "Move toward the center":
            jump steam_center_walk

label steam_left_wall_careful:
    scene steam_corridor:
        size (1920, 1080)
    "You continue carefully along the left wall."
    "The pipes here remain relatively stable, though the heat is still intense."
    "You're nearly at the end of the corridor now. Just ten more feet."
    "Suddenly, you hear a loud CLANK from behind you. The whole corridor shudders."
    
    menu:
        "What do you do?"
        
        "Run for the exit!":
            jump steam_corridor_escape
            
        "Press flat against the wall":
            jump steam_wall_press
            
        "Look back to see what happened":
            jump steam_look_back_death

label steam_wall_press:
    scene steam_corridor:
        size (1920, 1080)
    "You press yourself flat against the wall, making yourself as small as possible."
    "Steam blasts down the corridor but most of it stays near the center and right side."
    "The heat is intense but you survive it!"
    "After a few seconds, the pressure release subsides."
    "The exit is right there. Just a few more steps."
    
    menu:
        "Make a run for it?"
        
        "Yes! Sprint to the exit!":
            jump steam_corridor_escape

label steam_corridor_escape:
    scene steam_corridor:
        size (1920, 1080)
    "You sprint the final distance to the doorway!"
    "Steam hisses and pipes groan behind you, but you're faster."
    "You burst through the doorway and into the next chamber."
    "You made it through the steam corridor!"
    "You lean against the wall, gasping for clean air."
    
    menu:
        "Catch your breath and look around"
        
        "Where are you now?":
            jump pendulum_chamber_entrance

# PENDULUM CHAMBER - Final challenge before Level 2

label pendulum_chamber_entrance:
    scene pendulum_chamber:
        size (1920, 1080)
    "You find yourself in a large circular chamber with a high ceiling."
    "Massive industrial pendulums swing back and forth across the room."
    "Each pendulum is made of heavy brass and steel - probably weighing tons."
    "They swing at different speeds and heights, creating a deadly pattern."
    "Across the chamber, you can see a large iron door with a wheel valve."
    "That must be the entrance to Level 2."
    
    menu:
        "How will you cross?"
        
        "Study the pendulum pattern":
            jump pendulum_study
            
        "Run straight across":
            jump pendulum_rush_death
            
        "Look for another way":
            jump pendulum_alternate_search

label pendulum_alternate_search:
    scene pendulum_chamber:
        size (1920, 1080)
    "You search along the perimeter of the chamber for any other way across."
    "The walls are solid. No doors, no passages, no alternatives."
    "There's a small maintenance alcove to your right with some tools and a control panel."
    "Maybe you could stop the pendulums from there?"
    
    menu:
        "What will you do?"
        
        "Investigate the control panel":
            jump pendulum_control_panel
            
        "Just cross normally":
            jump pendulum_study

label pendulum_control_panel:
    scene pendulum_chamber:
        size (1920, 1080)
    "You examine the control panel in the alcove."
    "It's covered in brass switches and pressure gauges."
    "Most of the labels are worn off, but you can make out a few words: 'EMERGENCY STOP' and 'PRESSURE RELEASE'."
    "There's also a large red lever marked with a warning symbol."
    
    menu:
        "What will you do?"
        
        "Pull the Emergency Stop":
            jump pendulum_emergency_stop
            
        "Try Pressure Release":
            jump pendulum_pressure_death
            
        "Pull the red lever":
            jump pendulum_red_lever_death
            
        "Leave the panel alone":
            jump pendulum_study

label pendulum_emergency_stop:
    scene pendulum_chamber:
        size (1920, 1080)
    "You flip the switch marked 'EMERGENCY STOP'."
    "The pendulums begin to slow down gradually."
    "After about thirty seconds, they come to a complete stop."
    "Success! You can walk across safely now!"
    
    menu:
        "Cross the chamber?"
        
        "Yes, walk to the door":
            jump pendulum_emergency_cross

label pendulum_emergency_cross:
    scene pendulum_chamber:
        size (1920, 1080)
    "You walk confidently across the chamber, passing between the now-stationary pendulums."
    "Halfway across, you hear a clicking sound."
    "The emergency stop was on a timer!"
    "The pendulums suddenly swing back into motion!"
    
    menu:
        "Quick!"
        
        "Run forward!":
            jump pendulum_emergency_run
            
        "Run back!":
            jump pendulum_emergency_back_death
            
        "Stand still!":
            jump pendulum_stand_death

label pendulum_emergency_run:
    scene pendulum_chamber:
        size (1920, 1080)
    "You sprint forward toward the door!"
    "A pendulum swings just behind you - so close you feel the wind."
    "Another one ahead - you slide under it!"
    "With a final desperate dive, you reach the iron door!"
    "You made it! You're at the entrance to Level 2!"
    
    menu:
        "Open the door?"
        
        "Yes! Get out of this death trap!":
            jump level2_entrance

label pendulum_study:
    scene pendulum_chamber:
        size (1920, 1080)
    "You watch the pendulums carefully, studying their patterns."
    "There are five pendulums total. They swing at different intervals."
    "After watching for a minute, you start to see gaps in their patterns."
    "There's a safe path, but it requires precise timing."
    "You'll need to wait for the right moment, then move quickly between swings."
    
    menu:
        "Ready to attempt the crossing?"
        
        "Yes, time to go":
            jump pendulum_cross_attempt
            
        "Watch the pattern more":
            jump pendulum_study_more
            
        "Look for another option":
            jump pendulum_alternate_search

label pendulum_study_more:
    scene pendulum_chamber:
        size (1920, 1080)
    "You continue watching, committing the pattern to memory."
    "Pendulum 1: Swings every 3 seconds, low height."
    "Pendulum 2: Swings every 4 seconds, medium height."
    "Pendulum 3: Swings every 5 seconds, high height."
    "Pendulum 4: Swings every 3.5 seconds, low height."
    "Pendulum 5: Swings every 6 seconds, medium height."
    "You think you've got it figured out."
    
    menu:
        "Make your move?"
        
        "Yes, cross now":
            jump pendulum_cross_attempt
            
        "Maybe there's a control panel":
            jump pendulum_alternate_search

label pendulum_cross_attempt:
    scene pendulum_chamber:
        size (1920, 1080)
    "You take a deep breath and wait for the right moment."
    "Pendulum 1 swings past. Now!"
    "You sprint forward to the first safe zone."
    "Pendulum 2 swings overhead - you ducked just in time!"
    
    menu:
        "Continue?"
        
        "Keep moving carefully":
            jump pendulum_cross_continue
            
        "Wait here for the next opening":
            jump pendulum_wait_zone

label pendulum_wait_zone:
    scene pendulum_chamber:
        size (1920, 1080)
    "You wait in the safe zone, catching your breath."
    "Pendulum 3 swings past, then Pendulum 4."
    "You see your next opening approaching."
    
    menu:
        "Go now?"
        
        "Yes, move to the next zone":
            jump pendulum_cross_continue
            
        "Wait one more cycle":
            jump pendulum_wait_death_2

label pendulum_cross_continue:
    scene pendulum_chamber:
        size (1920, 1080)
    "You move to the second safe zone, timing it perfectly."
    "Two more zones to go. Pendulum 3 swings high - you're clear."
    "You dash to the third zone. Almost there!"
    "Pendulum 5 is approaching. You need to time this perfectly."
    
    menu:
        "Final stretch!"
        
        "Sprint to the door!":
            jump pendulum_final_sprint
            
        "Wait for Pendulum 5 to pass":
            jump pendulum_final_wait

label pendulum_final_wait:
    scene pendulum_chamber:
        size (1920, 1080)
    "You wait for Pendulum 5 to complete its swing."
    "It passes. The path to the door is clear!"
    "You walk calmly across the final distance."
    "You reach the iron door safely. You did it!"
    
    menu:
        "Open the door to Level 2?"
        
        "Yes":
            jump level2_entrance

label pendulum_final_sprint:
    scene pendulum_chamber:
        size (1920, 1080)
    "You don't wait - you sprint for the door!"
    "Pendulum 5 is coming but you're fast."
    "You reach the door just as the pendulum swings past behind you."
    "That was close! But you made it!"
    
    menu:
        "Open the door to Level 2?"
        
        "Yes":
            jump level2_entrance

# LEVEL 2 ENTRANCE - Transition to Temple of Doom aesthetic

label level2_entrance:
    scene level2_entrance:
        size (1920, 1080)
    "You turn the wheel valve on the iron door. It groans and slowly swings open."
    "Beyond the door, you see stone steps descending into darkness."
    "The mechanical sounds of the steampunk level fade behind you."
    "As you descend, the air changes - it becomes cooler, damper."
    "The walls change from brass and gears to ancient stone."
    "You've left the machine level behind."
    "Welcome to Level 2..."
    "TO BE CONTINUED..."
    
    menu:
        "Return to beginning":
            jump start