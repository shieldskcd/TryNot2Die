# File Structure for RenPy

The following folder structure is used for the RenPy game.

~/
    - README.md = The ReadMe for the Game
    - FileStructure.md = This file.
    | Try Not to Die
         - gui.rpy
         - main.rpy (Main file)
         - options.rpy
         - screens.rpy
         - script.rpy
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
                     - overlook.png (horror inspired red-eyes for overlook)
                     - secret_door.png (opens in the fountatin)
                | saves
                    - navigation.json
                    - persistent
                |tl
                    - common.rpym
