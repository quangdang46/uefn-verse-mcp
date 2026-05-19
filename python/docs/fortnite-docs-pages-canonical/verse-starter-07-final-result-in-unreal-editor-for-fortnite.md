## https://dev.epicgames.com/documentation/en-us/fortnite/verse-starter-07-final-result-in-unreal-editor-for-fortnite

# 7. Final Result
Find all the Verse code used to create the Verse Starter Template.
![7. Final Result](https://dev.epicgames.com/community/api/documentation/image/d89ba987-e73b-4dd7-87f3-a2197230bc2d?resizing_type=fill&width=1920&height=335)
In this final step, you can find all the code used to create the project. Each heading below is the filename in the project where the code lives.
Try to change the code and figure out ways to add more functionality to the minigame. The following are some ideas to get you started:
  * Add more levels for the character to solve.
  * Keep track of how long it took the player to solve the puzzle or how many moves the character performed per level.
  * Add more commands for the character to make more complex puzzles, such as picking up items and placing them on the board.

##  submodules.verse
The project file **submodules.verse** sets the access level for submodules and assets in the project so they can be used in the Verse code. For more details, check out step [5. Controlling the NPC with UI](https://dev.epicgames.com/documentation/fortnite/verse-starter-template-5-controlling-npc-with-ui-in-unreal-editor-for-fortnite) and [Exposing Assets to Verse](https://dev.epicgames.com/documentation/fortnite/exposing-assets-with-asset-reflection-to-verse-in-unreal-editor-for-fortnite).
Verse
```
# This file sets the access levels for submodules in the project.
# Specifically, this file is making art assets accessible to the Verse files in the project
# so textures, meshes, and materials can be used in the UI and in the game.

# The submodule Textures.MiniGameUI below is the same as the folder
# Textures/MinigameUI that you can see in the project's Content Browser.
Textures := module:
    MiniGameUI<public> := module{}

# The submodule VerseCommander below is the same as the folder

```

Copy full snippet(15 lines long)
##  verse_starter_tags.verse
The project file **verse_starter_tags.verse** contains the definition for the [Gameplay Tag](https://dev.epicgames.com/documentation/fortnite/verse-tags-in-fortnite) `verse_commander_minigame_tag` which the Verse Commander Character NPC script can use to find the Verse Commander Minigame device and listen to its events. For more details, check out step [1. Creating the NPC Behavior](https://dev.epicgames.com/documentation/fortnite/verse-starter-template-1-creating-npc-behavior-in-unreal-editor-for-fortnite).
Verse
```

| # This file contains the Gameplay Tags for the project.

---|---

| # You can use Gameplay Tags to tag an object in the island

| # and be able to query all objects that have the tag during the game using Verse.

|

|
using { /Verse.org/Simulation/Tags }

|

| # The verse_commander_minigame_tag is for the Verse Commander Character NPC script

| # to be able to find the Verse Commander Minigame device and listen to its events.

|
verse_commander_minigame_tag := class(tag){}

```

# This file contains the Gameplay Tags for the project. # You can use Gameplay Tags to tag an object in the island # and be able to query all objects that have the tag during the game using Verse. using { /Verse.org/Simulation/Tags } # The verse_commander_minigame_tag is for the Verse Commander Character NPC script # to be able to find the Verse Commander Minigame device and listen to its events. verse_commander_minigame_tag := class(tag){}
Copy full snippet(9 lines long)
##  commands.verse
The project file **commands.verse** in the submodule **VerseCommander** contains the data representation of all the commands that the NPC can receive. For more details, check out step [4. Representing Command Data](https://dev.epicgames.com/documentation/fortnite/verse-starter-template-4-representing-command-data-in-unreal-editor-for-fortnite).
Verse
```
# This file contains the data representation of all the commands that the NPC can receive
# and utilities for the data to help with debugging and troubleshooting issues.

# Each type of command that the NPC can perform will be an instance of this class.
# The class has the unique specifier to make instances of the class comparable.
# The class has the computes specifier to be able to instantiate it at module-scope.
# The class has the abstract specifier so it cannot be instantiated directly, and
# requires subclasses to implement any non-initialized functions, like DebugString().
command := class<computes><unique><abstract>:
    DebugString():string

```

Copy full snippet(39 lines long)
##  gameboard.verse
The project file **gameboard.verse** in the submodule **VerseCommander** contains the gameboard data and behavior. For more details, check out step [2. Defining Boards for the Game](https://dev.epicgames.com/documentation/fortnite/verse-starter-template-2-defining-boards-for-game-in-unreal-editor-for-fortnite).
Verse
```
# This file contains the gameboard structure and how it works.
# The gameboard knows where the NPC is supposed to start on the board
# how many obstacles / barriers there are to getting to the end goal,
# and what the end goal is and when it has been reached.
using { /Fortnite.com/Devices }
using { /UnrealEngine.com/Temporary/SpatialMath }
using { /Verse.org/Simulation }
using { /Verse.org/Simulation/Tags }

# An obstacle on the gameboard, with an associated set of

```

Copy full snippet(128 lines long)
##  ui_manager.verse
The project file **ui_manager.verse** in the submodule **VerseCommander** contains the code for creating and modifying the look of the UI. For more details, check out step [5. Controlling the NPC with UI](https://dev.epicgames.com/documentation/fortnite/verse-starter-template-5-controlling-npc-with-ui-in-unreal-editor-for-fortnite).
Verse
```
# This file contains all the code to create and modify the UI
# in the Verse Commander minigame.
# The UI for the game contains:
#  - Buttons that map to commands for the NPC: forward, turn left, turn right.
#  - An execute button that tells the NPC to perform the queue of commands.
#  - A remove button that removes the last command added.
#  - A reset button that resets the current board and clears out the command queue.
#  - A dynamic list of commands that grows wider when a player adds commands and shrinks when a player removes commands.

using { /Fortnite.com/Devices }

```

Copy full snippet(427 lines long)
##  verse_commander_minigame.verse
The project file **verse_commander_minigame.verse** in the submodule **VerseCommander** contains the Verse device that manages the minigame. For more details, check out step [6. Managing the Game Loop](https://dev.epicgames.com/documentation/fortnite/verse-starter-template-6-managing-game-loop-in-unreal-editor-for-fortnite).
Verse
```
# This device is in charge of managing the minigame.
# In its Details panel in the editor, you can:
# - Define how many gameboards there are
# - The order you play the gameboards
# - All the details of the gameboard such as their obstacles.

using { /Fortnite.com/Devices }
using { /Fortnite.com/UI }
using { /UnrealEngine.com/Temporary }
using { /UnrealEngine.com/Temporary/Diagnostics }

```

Copy full snippet(290 lines long)
##  verse_commander_character.verse
The project file verse_commander_character.verse in the submodule VerseCommander contains the logic for the minigame’s NPC. For more details, check out step [1. Creating the NPC Behavior](https://dev.epicgames.com/documentation/fortnite/verse-starter-template-1-creating-npc-behavior-in-unreal-editor-for-fortnite).
Verse
```
# This file handles the logic for the gameboard NPC. The NPC waits for commands from
# verse_commander_minigame, then executes movement based on those commands using navigation targets.
# It also tracks the NPC's position using a visual arrow that updates after each command.

using { /Fortnite.com/AI }
using { /Fortnite.com/Characters }
using { /Fortnite.com/Devices }
using { /UnrealEngine.com/Temporary/Diagnostics }
using { /UnrealEngine.com/Temporary/SpatialMath }
using { /Verse.org/Assets }

```

Copy full snippet(328 lines long)
