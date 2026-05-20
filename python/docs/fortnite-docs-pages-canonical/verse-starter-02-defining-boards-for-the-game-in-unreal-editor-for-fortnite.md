## https://dev.epicgames.com/documentation/en-us/fortnite/verse-starter-02-defining-boards-for-the-game-in-unreal-editor-for-fortnite

# 2. Defining Boards for the Game

Create modular levels that you can customize in Unreal Editor for Fortnite using Verse.

![2. Defining Boards for the Game](https://dev.epicgames.com/community/api/documentation/image/5ea12925-fe12-4557-8ef2-c3d09d0f5889?resizing_type=fill&width=1920&height=335)

In the previous step, we created an NPC that can move forward, rotate left, and rotate right when it receives commands. Now in this step, we'll set up gameboards that the character can move around on.

For this game, the gameboard needs to know and manage the following:

- **Tile Size**: How big the tiles on the board are so the character knows how far to move.
- **Camera**: What camera to use when the character reaches this gameboard. For this, we use the [Fixed Point Camera](https://dev.epicgames.com/documentation/en-us/fortnite-creative/using-fixed-point-camera-devices-in-fortnite-creative) device.
- **Start Position**: The position where the character should start on the board. For this, we use a [Creative Prop](https://dev.epicgames.com/documentation/fortnite/converting-assets-into-props-in-unreal-editor-for-fortnite) so we can easily set it as an editable property and get its transform.
- **End Goal**: The end goal for the character to progress towards which signals the end of the gameboard. For this, we use a [Trigger device](https://dev.epicgames.com/documentation/en-us/fortnite-creative/using-trigger-devices-in-fortnite-creative) that signals when the character steps on it.
- **Obstacles**: Obstacles prevent the character from immediately reaching the end goal. These are explained in more detail in [Creating Obstacles](https://dev.epicgames.com/documentation/fortnite/verse-starter-02-defining-boards-for-the-game-in-unreal-editor-for-fortnite).

Each of these are tracked in the gameboard's `class`. The class has the concrete specifier so it can be an editable property on a Verse device, and each class member has an editable attribute to be able to change their values from UEFN.

Verse

```
# This class represents the gameboard and how it behaves.
# This class has the concrete specifier so it can be an editable property on a Verse device.
gameboard<public> := class<concrete>:

    # The size of each tile on the gameboard. By default set to
    # the default Fortnite tile size of 512x512x384.
    @editable
    TileSize<public>:vector3 = vector3{X:=512.0, Y:=512.0, Z:=384.0}

    # The fixed point camera that provides a top-down view of the gameboard
```

Now that the gameboard is defined with its properties, let's add its behavior:

- **Handling end goal**: When the gameboard is set up, we'll subscribe to the End Goal's `TriggeredEvent`. We use an event handler and a custom event to signal publicly that the end goal was reached when the trigger device is triggered by the character. For more details, check out [Coding Device Interactions](https://dev.epicgames.com/documentation/fortnite/coding-device-interactions-in-verse).
- **Starting gameboard**: When it's the start of the gameboard, assign the Camera device to all players.
- **Ending gameboard**: When it's the end of the gameboard, remove the Camera device from all players.

The following is the complete class for `gameboard`:

Verse

```
# This class represents the gameboard and how it behaves.
# This class has the concrete specifier so it can be an editable property on a Verse device.
gameboard<public> := class<concrete>:

    # The size of each tile on the gameboard. By default set to
    # the default Fortnite tile size of 512x512x384.
    @editable
    TileSize<public>:vector3 = vector3{X:=512.0, Y:=512.0, Z:=384.0}

    # The fixed point camera that provides a top-down view of the gameboard
```

## Creating Obstacles

Obstacles prevent the character from immediately reaching the end goal. We use Barrier devices as the obstacles in this game to block the character from moving, and Trigger devices that deactivate the barriers.

Our definition of the `obstacle` class includes:

- **IsObstaclePassed**: Data for storing whether the barriers are currently activated or deactivated. Logic type because there are only two states.
- **Barriers**: [Barrier devices](https://dev.epicgames.com/documentation/en-us/fortnite-creative/using-barrier-devices-in-fortnite-creative) associated with the obstacle. This means you can have more than one barrier device attached to a trigger that deactivates them.
- **BarrierDissolves**: [Cinematic sequences](https://dev.epicgames.com/documentation/fortnite/using-cinematic-sequence-device-in-unreal-editor-for-fortnite) to play when obstacles are passed.
- **BarrierAppears**: [Cinematic sequences](https://dev.epicgames.com/documentation/fortnite/using-cinematic-sequence-device-in-unreal-editor-for-fortnite) to play when obstacles are reset.
- **Trigger**: A [Trigger device](https://dev.epicgames.com/documentation/en-us/fortnite-creative/using-trigger-devices-in-fortnite-creative) for the character to reach to deactivate the obstacle.

The following is the complete class for representing obstacles, and the class has the concrete specifier so it can be an editable property on a Verse device.

Verse

```
# An obstacle on the gameboard, with an associated set of
# Barrier devices, Trigger devices that deactivate the barriers,
# and Cinematic Sequence devices that play sequences for barriers dissolving and appearing for visual feedback on what is happening.
# This class has the concrete specifier so it can be an editable property on a Verse device.
obstacle := class<concrete>:

    # Data for storing whether barriers are currently enabled/disabled.
    var IsObstaclePassed:logic = false

    # The array of barriers for this obstacle.
```

## Adding Gameboards

Now that the gameboard is defined, you can add an array of these gameboards to your Verse device, which you'll see later in [6. Managing the Game Loop](https://dev.epicgames.com/documentation/fortnite/verse-starter-06-managing-the-game-loop-for-in-unreal-editor-for-fortnite).

To test out specific levels, you can reorder the boards so the level you want to test is the first in the list.

## Next Step

We've defined the gameboards and shown how to add as many as you want. In the next step, you'll learn how to design the boards to develop fun puzzles and work around limitations.

- [![3. Designing Levels](https://dev.epicgames.com/community/api/documentation/image/19ab3795-416b-4ebf-a49b-4f92d594909b?resizing_type=fit&width=640&height=640)

  3. Designing Levels

  Learn how to design levels for a top-down camera and controlling a character through commands.](https://dev.epicgames.com/documentation/fortnite/verse-starter-03-designing-levels-for-in-unreal-editor-for-fortnite)
