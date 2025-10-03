graph TD
    Start[START: Forest] --> Entrance{Labyrinth Entrance}
    
    Entrance --> Fountain[Fountain Area]
    Entrance --> Bench[Bench Area]
    Entrance --> StatueArea[Level 0 Left: Statue Area]
    
    %% FOUNTAIN PATH
    Fountain --> LookFountain{Look at Fountain}
    LookFountain --> StickHand{Stick Hand In?}
    StickHand -->|Pull Out| DeathPulled[💀 DEATH: Pulled Into Darkness]
    StickHand -->|Keep Going| FindButton[Find Button]
    FindButton --> SecretDoor[Secret Door Opens]
    SecretDoor --> ClockRoom[Clock Room]
    
    ClockRoom --> InspectWalls[Inspect Walls - TBC]
    ClockRoom --> InspectGears[Inspect Gears - TBC]
    ClockRoom --> WalkForward[Walk Forward - TBC]
    
    %% BENCH PATH
    Bench --> Overlook[Overlook Area]
    Overlook -->|Jump| DeathJump[💀 DEATH: Fall Into Pit]
    
    %% STATUE PATH
    StatueArea --> StatueClose[Inspect Statue]
    StatueArea --> StatueBehind[Behind Statue]
    
    StatueClose --> StatueTouch[Touch Statue]
    StatueClose --> StatueEyes{Poke Eyes}
    StatueEyes -->|Remove Fingers| StatueClose
    StatueEyes -->|Keep Fingers In| DeathStatue[💀 DEATH: Turn to Stone]
    
    StatueBehind --> MazeArch[Garden Archway]
    MazeArch --> MazeStart{Maze Junction 1}
    
    %% MAZE - RIGHT PATH
    MazeStart -->|Right| Maze1R[Maze Section 1R]
    Maze1R --> Maze2R[Maze Section 2R]
    Maze2R --> Maze3R{Maze Junction 3R}
    
    Maze3R -->|North| BirdClearing[Bird Clearing]
    Maze3R -->|South| DeadEnd1[Dead End]
    
    BirdClearing -->|Listen Longer| Birds2{Listen More?}
    Birds2 -->|Yes| DeathBirds[💀 DEATH: Eternal Sleep]
    
    %% MAZE - LEFT PATH
    MazeStart -->|Left| Maze1L[Maze Section 1L]
    Maze1L --> Maze2L[Maze Section 2L]
    Maze2L --> Maze3L{Maze Junction 3L}
    
    Maze3L -->|North| Maze3LN1[North Path 1]
    Maze3L -->|South| Maze3LS[South Path - TBC]
    
    Maze3LN1 --> Maze3LN2[North Path 2]
    Maze3LN2 --> Maze3LN3[North Path 3]
    Maze3LN3 --> Maze3LN4[North Path 4]
    Maze3LN4 --> Maze3LN5{Junction 5}
    
    Maze3LN5 -->|Left| Maze5L1[Left Branch 1]
    Maze5L1 --> DeadEnd2[Dead End]
    
    Maze3LN5 -->|North| Maze3LN6[North Path 6]
    Maze3LN6 --> Maze3LN7[North Path 7]
    Maze3LN7 --> Auditorium[Outdoor Theatre]
    
    %% AUDITORIUM
    Auditorium --> AudStage[Stage]
    Auditorium --> AudBalcony[Balcony]
    Auditorium --> AudOrchestra[Orchestra Pit]
    
    AudStage --> StageMemory{Enter Memory?}
    StageMemory -->|Yes| MemoryChoice{Performance Type}
    
    MemoryChoice -->|Song| MemorySong[Sing Song - Returns to Auditorium]
    MemoryChoice -->|Drama| MemoryDrama[Perform Drama - Returns to Auditorium]
    MemoryChoice -->|Leave Stage| MemoryLeave{Try to Leave}
    
    MemoryLeave -->|Insist on Leaving| Attacked[Attacked by Crowd]
    Attacked --> DeathCrowd[💀 DEATH: Overwhelmed by Phantoms]
    
    AudBalcony --> ExamineSymbols[Examine Symbols]
    AudOrchestra --> TouchInstruments[Touch Instruments]
    
    %% DEATH NODES STYLING
    classDef deathNode fill:#cc0000,stroke:#000,stroke-width:3px,color:#fff
    class DeathPulled,DeathJump,DeathStatue,DeathBirds,DeathCrowd deathNode
    
    %% INCOMPLETE NODES STYLING
    classDef incompleteNode fill:#ffaa00,stroke:#000,stroke-width:2px
    class InspectWalls,InspectGears,WalkForward,Maze3LS incompleteNode
    
    %% SAFE ZONES STYLING
    classDef safeNode fill:#00cc00,stroke:#000,stroke-width:2px
    class ClockRoom,Auditorium safeNode