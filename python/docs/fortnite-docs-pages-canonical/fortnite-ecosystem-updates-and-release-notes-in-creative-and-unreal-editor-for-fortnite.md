## https://dev.epicgames.com/documentation/en-us/fortnite/fortnite-ecosystem-updates-and-release-notes-in-creative-and-unreal-editor-for-fortnite

# 1. Creating the NPC Behavior
Learn how to control the NPC through commands using Verse in the Verse Starter Template.
![1. Creating the NPC Behavior](https://dev.epicgames.com/community/api/documentation/image/5c2e12ba-132c-46b2-87ed-7aff8cb279ed?resizing_type=fill&width=1920&height=335)
The character in this example uses a [Custom](https://dev.epicgames.com/documentation/fortnite/npc-types-in-unreal-editor-for-fortnite) type character definition, since they only need to move around, and don't need access to the guard or wildlife API. The character's behavior is driven by a custom Verse Behavior named `verse_commander_character`.
Guards are non-playable characters (NPCs) that can move along designated paths and can become hostile to attack enemy players. Wildlife are animals, like chicken and boar, that can also move along designated paths and attack enemy players.
To get started creating the custom NPC, create a new NPC Behavior named `vese_commander_character` using Verse Explorer. For info on creating your own custom NPC behaviors, see [Create Custom NPC Behavior](https://dev.epicgames.com/documentation/en-us/uefn/create-custom-npc-behavior-in-unreal-editor-for-fortnite).
The character needs to know and manage the following properties:
  * **CommandWaitTime** : How long to wait between each command.
  * **FocusTime** : How long to force focus on a target. Turning the character left or right is handled by using the character's `focus_interface` to force them to face a particular point to their left or right. Since focusing on a target doesn't complete unless interrupted, this is set to a very low number, just enough time for the character to turn to face a direction.
  * **ReachRadius** : This is how close the character needs to get to their navigation target to consider having “reached” it.
  * **VerseCommanderMinigame** : This is a reference to the **VerseCommanderMinigame** in the level, and lets the character listen for commands coming from it.
  * **VFX and Arrow References** : These reference the different teleport in/teleport out VFX, as well as the Forward Arrow prop which makes it easier to see the character's orientation.
Verse
```
      # A Verse-authored NPC Behavior that can be used within an NPC Definition or a Character Spawner device's Behavior Script Override.
      verse_commander_character<public> := class(npc_behavior):

          # The VFX that play when the NPC teleports out.
          @editable
          CharacterTeleportOutVFX:vfx_spawner_device = vfx_spawner_device{}

          # The VFX that play when the NPC teleports in.
          @editable
          CharacterTeleportInVFX:vfx_spawner_device = vfx_spawner_device{}

```

Copy full snippet(39 lines long)
Now that we've defined the character's properties, let's define their behaviors and the functions that drive them.

##  Character Movement
The character in this game has the following behaviors:
  * **Move Forward** : The **Forward** command moves the character forward 1 tile on the gameboard.
  * **Turn Right** or **Turn Left** : The **Turn Right** and **Turn Left** commands make the character turn 90 degrees to face their right or left, respectively. This also needs to happen without moving the character from the tile they're standing on.
  * **Reset** : When the **Reset** command is issued, the character teleports back to the starting position on the gameboard.
  * **Await Commands** : Since the character's movement can't be controlled directly, they need to listen for commands coming from the **VerseCommanderMinigame** device in the level. After executing all of their commands, they'll stand still and await further commands.

The NPC in this template only has a few movement options, being able to move forward in the direction they're facing by one tile, turn right, or turn left. Each of these options is done through the `GetNavTarget()` function, which creates a new navigation target one `TileDistance` away for the character to use. This target is either to the character's local forward, right, or left depending on whether the given command is Forward, Right, or Left.
Verse
```
# Gets a new navigation target for the NPC based on the current transform and the given command.
GetNavTarget(CurrentTransform:transform, Command:command, TileDistance:vector3):transform=
    # Based on the command, get the character's local forward, right, or left (negative right).
    Direction :=
        if (Command = Commands.Forward):
            CurrentTransform.Rotation.GetLocalForward()
        else if (Command = Commands.TurnRight):
            CurrentTransform.Rotation.GetLocalRight()
        else if (Command = Commands.TurnLeft):
            -CurrentTransform.Rotation.GetLocalRight()

```

Copy full snippet(26 lines long)
When the NPC receives the Execute signal, they iterate through the list of commands they receive and pass each of them to the `ExecuteCommand()` function. First, they get the `focus_interface` and `navigatable` interface for the character, then perform different actions based on the command. For each of Forward, Right, and Left, they call `GetNavTarget()` to find the new transform for the NPC to use. Then, they either navigate forward to the new transform using `NavigateTo()` from the `navigatable` interface or use the `focus_interface` to focus on the target to their right or left.
Verse
```
# Executes the given command, either moving the NPC forward one tile or turning them left
# or right.
ExecuteCommand(Command:command, TileSize:vector3)<suspends>:void=
    if:
        # Get the Agent (the NPC).
        Agent := GetAgent[]

        # Gets the Fortnite Character interface, which gets you access to its gameplay data
        # including its AI module for navigation and focus.
        Character := Agent.GetFortCharacter[]

```

Copy full snippet(39 lines long)
##  Character VFX
When the character moves around the gameboard, an arrow prop shows their position and orientation to make visualizing the character from the top-down camera easier. This arrow needs to follow the character around and update as the character turns and moves. The `MoveArrow()` function updates the arrow's position to match the character's, copying their position and orientation. The `CreateArrow()` function spawns the arrow prop and does an initial call to `MoveArrow()` so you can see where the character is right from the start.
Verse
```
# Creates an arrow prop at the NPC's position that visually shows the orientation of the NPC.
CreateArrow(Agent:agent):void=
    if :
        Character := Agent.GetFortCharacter[]
    then:
        var Transform:transform = Character.GetTransform()
        # Spawn the arrow prop, then set the mesh and material for the prop.
        SpawnPropResult := SpawnProp(ForwardArrowAsset, Transform)
        if:
            SpawnedProp := SpawnPropResult(0)?

```

Copy full snippet(40 lines long)
When the character spawns into the board, moves to a new board, or resets to the start of the board through the Reset command, a teleporting animation plays both for teleporting in and teleporting out. To create a teleporting effect, we first call `Hide()` on the character and the arrow, then play the TeleportOutVFX by moving the VFX spawner where the character is and enabling it. Once the teleporting out VFX finishes, we then need to teleport the character to their new position and play the TeleportInVFX at that location. When all that is done, we can then call `Show()` on the character and the arrow prop to show the character in the new position.
Verse
```
# Hides the NPC and the arrow prop, then teleports both to a new position,
# playing VFX for teleporting in and teleporting out.
PlayVFXAndMoveCharacter(StartPosition:transform)<suspends>:void=
    if:
        Agent := GetAgent[]
        FortCharacter := Agent.GetFortCharacter[]
    then:
        # Hide the NPC and the arrow.
        FortCharacter.Hide()
        ForwardArrow.Hide()

```

Copy full snippet(53 lines long)
Teleporting the character is done with a helper function `MoveToTile()`, which takes the transform to move the character to and teleports them there. A small offset is added to the transform's Z value to prevent the character from clipping into the floor.
Verse
```
# Teleports the NPC to the given transform.
MoveToTile(Transform:transform)<transacts><decides>:void=
    # Get the Agent (the NPC).
    Agent := GetAgent[]

    # Gets the Fortnite Character interface, which gets you access to its gameplay data
    # including its AI module for navigation and focus.
    Character := Agent.GetFortCharacter[]

    var NewTransform:transform = Transform

```

Copy full snippet(14 lines long)
##  Processing Commands
When the character is idle on the board, they need to sit and listen for the Execute signal to know what to do next. This happens in the `AwaitCommands()` function. This function has the [suspends](https://dev.epicgames.com/documentation/en-us/uefn/specifiers-and-attributes-in-verse#effectspecifiers) specifier so it can run asynchronously since the character needs to `Await()` the `ExecuteCommandsEvent`. Since commands come in as a tuple that contains an array of commands and the TileSize used for those commands, they each need to be processed in a `for` loop by calling `ExecuteCommand()`. As each command executes, we hide the forward arrow and only show it again when the command finishes executing. Once all commands are finished executing, we signal the Verse Commander Minigame that we're done with commands and are ready for more.
Verse
```
# Waits for commands to be sent from the verse_commander_minigame, then
# executes each command.
AwaitCommands()<suspends>:void=
    if:
        Agent := GetAgent[]
    then:
        # Wait for commands to be sent from the verse commander minigame.
        ExecuteResult := VerseCommanderMinigame.ExecuteCommandsEvent.Await()

        # For each execute result tuple, execute the command and pass the tile size from the tuple.

```

Copy full snippet(22 lines long)
Instead of processing new commands, the character can also be reset back to the start of the current gameboard with the Reset button. Since resetting is immediate and doesn't use the command queue, the character needs to listen for it separately from the Execute signal. This happens in the` AwaitReset()` function, which waits for the `BoardResetEvent` to signal from the Verse Commander Minigame. When it does, it calls `PlayVFXAndMoveCharacter()` to move the character back to the starting position of the board.
Verse
```

```

# Waits for the current board to be reset, then moves the # NPC back to the starting position of the board along with VFX. AwaitReset()<suspends>:void= # Wait for the current board to be reset. # The event payload is the starting position for the board. StartPosition := VerseCommanderMinigame.BoardResetEvent.Await() spawn{PlayVFXAndMoveCharacter(StartPosition)}
Copy full snippet(7 lines long)
##  Running the Character Game Loop
Now that the different functions that process commands are set up, it's time to create the core game loop of the character. The character needs to continuously listen for the Execute signal to process a list of commands, or the Reset signal to reset back to the start of the board. Because waiting for the Execute signal and the Reset signal each need to happen asynchronously, and may occur multiple times per board, you need a separate helper function that handles looping through both. This is handled by the `CharacterCommandLoop()` function, which runs the main game loop for the character. In a race expression, it races between the `AwaitReset()` function and a loop that continuously calls `AwaitCommands()` to make sure the character is always listening for commands.
Verse
```

```

# Race between resetting the character to start of the board and awaiting commands for that character. CharacterCommandLoop()<suspends>:void= race: AwaitReset() loop: AwaitCommands()
Copy full snippet(6 lines long)
When the game begins, the character won't be present in the level until it spawns from the NPC Spawner. This means that when it spawns, it needs to find the Verse Commander Minigame in the level since it doesn't have a reference to it. It does this using `GetCreativeObjectsWithTag()` to find the object with the [Gameplay Tag](https://dev.epicgames.com/documentation/fortnite/verse-tags-in-fortnite) `verse_commander_minigame_tag`, and setting that as the `VerseCommanderMinigame`. When creating your own minigame experience, make sure to properly set your tags so characters in the level can find the objects they need to communicate with.
After finding the Verse Commander Minigame, the character needs to spawn the forward arrow that follows them around using `CreateArrow()`. To run the game loop, it needs to continuously loop the `CharacterCommandLoop()` function to restart it if a Reset signal occurs. This also needs to happen in a race expression against the `GameEndedEvent` from the Verse Commander Minigame, since if the game ends the character should immediately stop what they're doing.
Verse
```
# This function runs when the NPC is spawned in the world and ready to follow a behavior.
OnBegin<override>()<suspends>:void=

    # Get the Verse Commander Minigame Device.
    # Assumption is that there is only one device in the level.
    CreativeObjects := GetCreativeObjectsWithTag(verse_commander_minigame_tag{})
    if:
        CreativeObject := CreativeObjects[0]
        MinigameManager := verse_commander_minigame[CreativeObject]
    then:

```

Copy full snippet(43 lines long)
##  Next Step
We've defined a custom NPC that takes command data from a Verse device and uses it to move around a gameboard. You can find the full list of code to create the custom character in the final step [7. Final Result](https://dev.epicgames.com/documentation/fortnite/verse-starter-07-final-result-in-unreal-editor-for-fortnite).
In the next step, you'll learn how to create a board for the character to be able to move around on and solve its puzzle.
  * [![2. Defining Boards for the Game](https://dev.epicgames.com/community/api/documentation/image/aa8ee667-63cb-4225-aa8d-36ef417da110?resizing_type=fit&width=640&height=640) 2. Defining Boards for the Game Create modular levels that you can customize in Unreal Editor for Fortnite using Verse. ](https://dev.epicgames.com/documentation/fortnite/verse-starter-02-defining-boards-for-the-game-in-unreal-editor-for-fortnite)
