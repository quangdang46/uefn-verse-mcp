## https://dev.epicgames.com/documentation/en-us/fortnite/verse-starter-05-controlling-the-npc-with-ui-in-unreal-editor-for-fortnite

# 5. Controlling the NPC with UI

Learn how to create and update a custom, dynamic in-game UI using Verse.

![5. Controlling the NPC with UI](https://dev.epicgames.com/community/api/documentation/image/1ebcd665-5a7a-4dc6-96d0-83f48df988e0?resizing_type=fill&width=1920&height=335)

The Verse Commander minigame has the following UI:

- **Character Commands**: These buttons map to commands for the NPC (Forward, Turn Left, Turn Right). Selecting one of these commands adds it to the list at the bottom of the screen.
- **Execute**: An Execute button that tells the NPC to perform the queue of commands at the bottom of the screen.
- **Remove**: A Remove button that removes the last command added to the list.
- **Reset**: A Reset button that resets the current board and clears out the command queue.
- **Command List**: A dynamic list of commands that grows when a player adds commands and shrinks when a player removes commands.

The UI is all implemented in Verse. Check out [Creating In-Game User Interfaces](https://dev.epicgames.com/documentation/fortnite/ingame-user-interfaces-in-unreal-editor-for-fortnite) to get started with Verse UI and understand how it works.

The sections below describe how to create the custom buttons and dynamic UI used in this game.

## Creating Buttons

The buttons are created in their own class, `minigame_button`, that handles their look when they’re activated or deactivated. We used a quiet button that overlays a horizontal stackbox with the text and icon, which then overlays the background. This creates the effect of a custom look for the buttons while maintaining the functionality and responsiveness that you get with the default button design in Fortnite.

The `SetEnabled()` function will set the interactivity of the button itself and swap out which textures and colors are used based on whether the button is being enabled or not.

Verse

```
# The class for storing all the widget references for a button and setting its look.
minigame_button := class:

    # Store a reference of the overlay for easy removal later.
    var Widget:overlay = overlay:

    # Store a reference of the background texture widget to change easily later.
    BackgroundImage:texture_block = texture_block:
        DefaultImage := Textures.MiniGameUI.T_UI_Button_Blue_Rounded
        DefaultDesiredSize := vector2{X := 256.0, Y := 128.0}
```

## Adding Commands to Screen

Each slot for the command list at the bottom is stored in an instance of the `command_queue` class. This class handles the look of the slot and stores any command data associated with it.

There are always two slots, even when there are no commands in the list, to represent the left and right ends of the list display. When a new command is selected by the player, the right end is updated with the command icon and a new right end slot is added. The command data representation is then stored in the variable `CommandData`.

When the player selects the remove button, the right end widget is removed from the canvas and the last command is changed to be the right end slot. The variable `CommandData` is set to false as there’s no longer a command associated with this slot.

Verse

```
# A class that stores the image (texture) that is used to represent a command in the queue on screen
# and the enum associated with that command.
command_queue := class:
    # Store a reference of the overlay for easy removal later.
    var Widget:overlay = overlay{}

    # Store a reference of the background texture block to change the image easily later.
    BackgroundImage:texture_block = texture_block:
        DefaultImage := Textures.MiniGameUI.TransparentImage512
        DefaultDesiredSize := vector2{X := 88.0, Y := 88.0}
```

## Managing Overall UI

Most of the code for the UI is in the `verse_commander_minigame_ui` class. This class sets up the look for each button and its unique text and icons, generates the UI layout and handles changes when commands are added or removed.

The custom images are textures that were exposed to Verse from UEFN. The access level for textures imported into project is defined in the [submodules.verse file](https://dev.epicgames.com/documentation/fortnite/verse-starter-07-final-result-in-unreal-editor-for-fortnite). For more details, check out [Exposing Assets to Verse](https://dev.epicgames.com/documentation/fortnite/exposing-assets-with-asset-reflection-to-verse-in-unreal-editor-for-fortnite).

This code seems longer than some of the other files because of the need to specify the position and look of every widget in the UI. Most of the behavior only exists in the three functions `ResetCommandQueue()`, `Remove()`, and `AddCommandToDisplay()`.

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

## Next Step

You can find the full list of code to create the UI in the final step [7. Final Result](https://dev.epicgames.com/documentation/fortnite/verse-starter-07-final-result-in-unreal-editor-for-fortnite).

Now that we have a custom UI, the next step shows you how to manage the game and all the pieces already created.

- [![6. Managing the Game Loop](https://dev.epicgames.com/community/api/documentation/image/d8c7cdb0-a36f-47b8-bc0a-723ebf7ac92a?resizing_type=fit&width=640&height=640)

  6. Managing the Game Loop

  Learn how to define the core behavior of the minigame in the Verse Starter Template.](https://dev.epicgames.com/documentation/fortnite/verse-starter-06-managing-the-game-loop-for-in-unreal-editor-for-fortnite)
