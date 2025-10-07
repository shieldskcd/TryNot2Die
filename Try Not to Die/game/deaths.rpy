# All death scenes in one file

# ==========================================
# LEVEL 0 DEATHS (Courtyard, Maze, Auditorium, Statue)
# ==========================================

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

label lv0_maze_auditorium_sing_death:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "There is nothing left... only music. You will keep singing as the darkness takes you."
    "The light slowly fades and so do the notes..."

    menu:
        "Try Again":
            jump start

# ==========================================
# LEVEL 1 DEATHS - Steampunk Area
# ==========================================

# --- VEIN/WALL PATH DEATHS ---

label vein_absorption_death:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "As your hand touches the pulsing wall, the veins suddenly wrap around your wrist!"
    "You try to pull away but they're too strong. More veins shoot out and grab your arms, your legs."
    "The wall is pulling you in! You feel yourself being absorbed into the organic machinery."
    "Your body becomes part of the mechanism. Your consciousness fades as you merge with the system."
    "You have died..."
    
    menu:
        "Try Again":
            jump start

label vein_compression_death:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "You push forward into the narrowing passage."
    "The walls press tighter and tighter against you. You can barely breathe."
    "You try to back out but you're wedged in too tightly."
    "The walls continue to compress. Your ribs crack under the pressure."
    "You have died..."
    
    menu:
        "Try Again":
            jump start

label vein_pulse_death:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "You listen to the rhythmic pulsing. Thump-thump. Thump-thump."
    "Your heartbeat syncs perfectly with the wall's rhythm."
    "You feel peaceful. Calm. Content to stay here forever."
    "But then your heart follows the wall's lead when the pulsing... stops."
    "Your heart stops with it. You collapse silently."
    "You have died..."
    
    menu:
        "Try Again":
            jump start

# --- BLUE GLOW PATH DEATHS (Water/Reservoir) ---

label blue_water_touch_death:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "You reach out and touch the beautiful glowing water."
    "The moment your fingers break the surface, something grabs you!"
    "You're yanked forward into the pool. The water is scalding hot!"
    "You try to scream but water fills your lungs. The glow surrounds you as you sink."
    "The machinery below pulls you down into the grinding mechanisms."
    "You have died..."
    
    menu:
        "Try Again":
            jump start

label blue_water_drink_death:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "The water looks so inviting. You cup your hands and bring some to your lips."
    "The water is boiling! It burns your hands, your lips, your throat!"
    "You stagger backward in agony, your mouth and throat blistered."
    "You collapse beside the pool, unable to breathe through your ruined throat."
    "You have died..."
    
    menu:
        "Try Again":
            jump start

label blue_water_slip_death:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "Your foot slips on the wet stone!"
    "You try to catch yourself but your momentum carries you forward."
    "You tumble into the glowing pool with a splash."
    "The scalding water envelops you as you're pulled down by unseen forces."
    "You sink into the machinery below, ground up by massive pumps."
    "You have died..."
    
    menu:
        "Try Again":
            jump start

label reservoir_approach_death:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "You approach the edge of the massive reservoir."
    "The churning water suddenly erupts in a massive geyser!"
    "Boiling water sprays everywhere. You're drenched in scalding liquid."
    "Your skin blisters instantly. You stagger backward but slip on the wet floor."
    "You fall into the churning reservoir and are pulled under by the currents."
    "You have died..."
    
    menu:
        "Try Again":
            jump start

label reservoir_touch_death:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "You reach out to touch the churning water."
    "As soon as your hand makes contact, something seizes it!"
    "You're yanked forward with incredible force. You try to resist but it's futile."
    "You're pulled into the reservoir. The machinery below sucks you down."
    "Massive turbines shred you as you're processed through the water system."
    "You have died..."
    
    menu:
        "Try Again":
            jump start

# --- GEAR PUZZLE PATH DEATHS ---

label gear_random_death:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "You hastily grab gears and start jamming them into the slots without thinking."
    "As soon as you place the third gear, you hear a terrible grinding sound."
    "The entire frame begins to rotate rapidly, and the gears you placed start spinning with incredible force."
    "Before you can pull your hand away, the gears catch your fingers and pull you toward the mechanism."
    "You scream as you're dragged into the grinding gears!"
    "The gears show no mercy. Your body is pulled into the mechanical horror."
    "You have died..."
    
    menu:
        "Try Again":
            jump start

label gear_timing_death:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "You try to time the placement of the center gear between the spinning outer gears."
    "Your hand moves forward with the gear, trying to slide it into the center slot."
    "But you misjudged the speed! An outer gear catches your wrist and yanks you forward."
    "Your arm is pulled into the mechanism as the gears interlock with brutal efficiency."
    "The gears don't stop. They never stop."
    "You have died..."
    
    menu:
        "Try Again":
            jump start

label gear_wait_trap:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "You decide to wait for the gears to stop spinning."
    "Minutes pass. The gears don't slow down. In fact, they seem to be spinning faster."
    "You notice the temperature in the room rising. The mechanism is generating heat."
    "Steam begins hissing from vents in the walls. The room is becoming an oven!"
    "You realize too late - the mechanism won't stop until it's complete or until you're dead."
    "The heat becomes unbearable. Your lungs burn with each breath."
    "You collapse as the steam fills the room completely."
    "You have died..."
    
    menu:
        "Try Again":
            jump start

label gear_burn_death:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "You grip the spinning gear tightly, ignoring the burning sensation."
    "The gear is too hot! Your skin sizzles and smoke rises from your palms."
    "But worse - the gear suddenly grabs your hand, pulling you closer."
    "Your burned hands can't let go. The mechanism drags you into the spinning assembly."
    "Pain and grinding metal are the last things you experience."
    "You have died..."
    
    menu:
        "Try Again":
            jump start

label gear_center_wait_death:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "You wait, listening to the ticking grow louder and louder."
    "Suddenly, the center gear begins spinning rapidly in reverse."
    "Spikes shoot out from the mounting frame in all directions!"
    "You try to dodge, but there are too many. Several pierce through your body."
    "The mechanism was a trap for those who hesitate."
    "You have died..."
    
    menu:
        "Try Again":
            jump start

label gear_pull_death:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "You grip the center gear with both hands and pull with all your strength."
    "The gear suddenly releases - but it's still spinning!"
    "The sharp teeth of the gear shred your palms as it spins freely in your hands."
    "You drop it in horror, but it's too late. The mechanism activates anyway."
    "Spikes burst from every surface of the mounting frame, impaling you from multiple angles."
    "You should have finished what you started."
    "You have died..."
    
    menu:
        "Try Again":
            jump start

label gear_escape_attempt:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "You turn and run from the mounting frame, heading back toward the clock room."
    "Behind you, the ticking reaches a fever pitch, then stops."
    "You hear a massive CLUNK. Then grinding. Then spinning."
    "The entire floor beneath you begins to rotate like a giant gear!"
    "You lose your footing and slide toward a gap where massive grinding gears wait below."
    "You fall into the grinding machinery below. There is no escape."
    "You have died..."
    
    menu:
        "Try Again":
            jump start

label gear_passage_rush:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "Eager to progress, you rush toward the opening in the wall."
    "You step through just as the gears complete their first full rotation."
    "Immediately, you realize your mistake. The walls of the passage are lined with more gears!"
    "They begin spinning rapidly, their teeth like saw blades."
    "You're trapped in a corridor of grinding death!"
    "The gears show no mercy to the hasty."
    "You have died..."
    
    menu:
        "Try Again":
            jump start

label gear_crawl_death:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "You drop to your stomach and begin crawling into the narrow space."
    "The spinning gears whir just inches above your back."
    "You're halfway through when you realize the space is getting narrower."
    "The gears are lowering! You try to crawl faster but you're stuck."
    "The gears descend and begin grinding against your back."
    "The crawlspace was a trap for the clever."
    "You have died..."
    
    menu:
        "Try Again":
            jump start

# --- STEAM CORRIDOR DEATHS ---

label steam_center_death:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "You try to run forward through the steam, but it's too much."
    "Superheated steam blasts up through the grating, engulfing your legs."
    "You scream in agony as your skin blisters and burns."
    "You collapse onto the grating as more steam vents catch you."
    "The steam shows no mercy. Your body is cooked by the intense heat."
    "You have died..."
    
    menu:
        "Try Again":
            jump start

label steam_wait_death:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "You press against the left wall and wait for the steam to subside."
    "But it doesn't stop. In fact, more vents open up along the corridor."
    "The entire passage is filling with superheated steam."
    "The temperature rises rapidly. You can't breathe. Your lungs burn."
    "You realize too late that staying still was the wrong choice."
    "The corridor becomes an oven. There is no escape."
    "You have died..."
    
    menu:
        "Try Again":
            jump start

label steam_right_death:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "You jump to the right, away from the steam eruption below."
    "Bad choice! You land directly next to a pipe with a red gauge."
    "As soon as you make contact with the wall, the pipe ruptures."
    "Pressurized steam blasts directly into your face and chest."
    "The pain is indescribable. Your skin melts from the heat."
    "The steam takes you quickly. Small mercy."
    "You have died..."
    
    menu:
        "Try Again":
            jump start

label steam_look_back_death:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "You turn to look back down the corridor."
    "Big mistake. A massive pressure release is happening - all the pipes are venting at once!"
    "A wall of superheated steam rushes toward you at incredible speed."
    "You try to run but it's too late. The steam wave hits you from behind."
    "Never look back in a place like this."
    "You have died..."
    
    menu:
        "Try Again":
            jump start

label steam_right_wall:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "You decide to test your luck with the right wall."
    "Maybe those red gauges are just for show?"
    "You take three steps along the right side."
    "WHOOSH! A pipe explodes right next to your head."
    "Scalding steam engulfs you completely."
    "Red gauges mean danger. Always."
    "You have died..."
    
    menu:
        "Try Again":
            jump start

# --- PENDULUM CHAMBER DEATHS ---

label pendulum_rush_death:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "You decide to just go for it and sprint across the chamber."
    "Bad idea. You make it about ten feet before a pendulum's return swing catches you."
    "The massive weight hits you with the force of a wrecking ball."
    "You're thrown across the room and hit the wall with a sickening crunch."
    "Patience is a virtue, especially around massive pendulums."
    "You have died..."
    
    menu:
        "Try Again":
            jump start

label pendulum_pressure_death:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "You activate the Pressure Release switch."
    "Immediately, you hear a loud hissing sound from above."
    "The pendulums don't stop - they speed up!"
    "The pressure release was for increasing their speed, not stopping them!"
    "Before you can react, a pendulum swings into the alcove and crushes you against the control panel."
    "Not every button should be pushed."
    "You have died..."
    
    menu:
        "Try Again":
            jump start

label pendulum_red_lever_death:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "The red lever looks important. You pull it down."
    "CLANG! The floor beneath you drops away!"
    "You fall into a pit filled with grinding gears and machinery."
    "The red lever was a trap for the curious."
    "Red levers with warning symbols should stay alone."
    "You have died..."
    
    menu:
        "Try Again":
            jump start

label pendulum_emergency_back_death:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "You turn and run back toward the entrance."
    "A pendulum you already passed has swung around and is coming at you from behind."
    "You don't see it until it's too late."
    "The massive weight crushes you against the chamber floor."
    "Never retreat in a room full of pendulums."
    "You have died..."
    
    menu:
        "Try Again":
            jump start

label pendulum_stand_death:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "You freeze in place, hoping the pendulums will miss you."
    "Bad gamble. There are too many of them."
    "One pendulum clips your shoulder, spinning you around."
    "You stumble directly into the path of another pendulum."
    "It hits you square in the chest. You fly backward and hit the wall."
    "Standing still is just waiting to die."
    "You have died..."
    
    menu:
        "Try Again":
            jump start

label pendulum_wait_death_2:
    $ death_count += 1
    scene death:
        size (1920, 1080)
    show text "{size=80}{color=#cc0000}{font=fonts/Butcherman-Regular.ttf}You Died{/font}{/color}{/size}" at Position(xalign=0.3, yalign=0.1) with dissolve
    "You wait for another cycle, being extra cautious."
    "But you've been standing here too long. The pattern is shifting slightly."
    "Pendulum 4's timing has changed - it's swinging faster now!"
    "It catches you completely off guard and slams into you."
    "The patterns don't stay consistent. Keep moving."
    "You have died..."
    
    menu:
        "Try Again":
            jump start