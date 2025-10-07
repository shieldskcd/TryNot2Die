# File Structure for RenPy

The following folder structure is used for the RenPy game.

~/
    - README.md = The ReadMe for the Game
    - FileStructure.md = This file.
    | Try Not to Die
         - auditorium.rpy (Covers actvities in the auditorium)
         - courtyard.rpy (Covers activities in the courtyard)
         - deaths.rpy (various death scenes)
         - gui.rpy
         - main.rpy (Main file)
         - maze.rpy (all actions in the maze)
         - options.rpy
         - screens.rpy
         - script.rpy
         - secret_room.rpy (the secret room area)
         - statue_area.rpy (all actions in the statue area)
            | game
                | audio
                | gui
                    (all the prebuilt images)
                | images
                     - black.png (smoky black enpty background)
                     - clock_room.png (second level room)
                     - courtyard.png (main courtyard on first floor)
                     - death.png (Grim Reaper image for Death Scenes)
                     - forest.png (First image in the game)
                     - fountain_vortex.png (Used when one sticks hand in the fountain)
                     - fountain.png (The fountain at rest)
                     - level0_left.png (Statue that appeares on the first level going left at fountatin)
                     - level0_statue.png (close up of the statue from level0_left.png)
                     - lv0_maze.png (Main background in the maze area)
                     - lv0_maze_auditorium_attacked.png (used in the auditorium in the maze and fail)
                     - lv0_maze_auditorium_memory.png (ghostly scene triggered by staying too long in the auditoroium)
                     - lv0_maze_auditorium_orchestra.png (Shows the orchestra memory)
                     - lv0_maze_auditorium_stage.png (stage in the center of the auditorium)
                     - lv0_maze_auditorium.png (first look at the auditorium)
                     - lv0_maze_bird.png (ethereal birds that attack you in the maze)
                     - lv0_maze_deadend.png (shows when you reach a dead end in the maze)
                     - lv0_statue_arm.png (starts the death scene when you poke the statue's eyes)
                     - lv0_statue_behind.png(entrance to the maze, behinance the statue)
                     - overlook.png (horror inspired red-eyes for overlook)
                     - secret_door.png (opens in the fountatin)
                     - violin_death.png (Image used when the player plays violin in the maze orchestra pit)
                | saves
                    - navigation.json
                    - persistent
                |tl
                    - common.rpym
