## https://dev.epicgames.com/documentation/en-us/fortnite/hud-message-device-design-example-in-fortnite-creative

# HUD Message Device Design Example

Warm, warmer, hot! Learn how to build a hot-and-cold game that features HUD Message devices!

![HUD Message Device Design Example](https://dev.epicgames.com/community/api/documentation/image/fffd79bf-f0cf-40e6-b31e-7ec41b810fce?resizing_type=fill&width=1920&height=335)

Remember the kids' game **Hot and Cold**? Want to see how you can make a digital version?

In this design example, learn how to build an a-mazing one-player mini-game using HUD Message devices along with some of the other resources available in Fortnite Creative.

The objective is for the player to enter on either side of the maze, then find the right end point by following the HUD message clues. You will also set the winning end point to change each time, making the game fun to play over and over!

You will learn how to:

- Use the HUD Message device.
- Set Color Changing Tiles to trigger messages based on game events and player locations.
- Use the Random Number Generator device to implement randomized gameplay objectives.
- See how to bind devices with other devices to trigger specific actions.

## Devices Used

- 1 x [Player Spawner](https://dev.epicgames.com/documentation/fortnite/using-player-spawn-pad-devices-in-fortnite-creative) device
- 1 x [Random Number Generator](https://dev.epicgames.com/documentation/fortnite/using-random-number-generator-devices-in-fortnite-creative) device
- 2 x [Trigger](https://dev.epicgames.com/documentation/fortnite/using-trigger-devices-in-fortnite-creative) devices
- 5 x [**HUD Message**](using-hud-message-devices-in-fortnite-creative) devices
- 5 x [**Billboard**](using-billboard-devices-in-fortnite-creative) devices (optional)
- 2 x [**Capture Area**](using-capture-area-devices-in-fortnite-creative) devices
- Multiple **[Color Changing Tile](https://dev.epicgames.com/documentation/fortnite/using-color-changing-tile-devices-in-fortnite-creative)** devices
- 4 x [Volume](https://dev.epicgames.com/documentation/fortnite/using-volume-devices-in-fortnite-creative) devices
- 1 x **[End Game](https://dev.epicgames.com/documentation/fortnite/using-end-game-devices-in-fortnite-creative)** device

## Build Your Maze

Start by building a maze that the player will have to maneuver through. You can find block shapes like the ones below in the **Primitive Shapes Gallery**, but any shapes will do as long as you can build a maze with enough space between the walls for a player to maneuver.

[![](https://dev.epicgames.com/community/api/documentation/image/b64e727b-0b60-4be8-8f84-4a4e268b12c5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b64e727b-0b60-4be8-8f84-4a4e268b12c5?resizing_type=fit)

The maze above has two entrances/exits, and multiple possible dead-end points inside of the maze.

[![](https://dev.epicgames.com/community/api/documentation/image/7803f3e5-1c19-486c-bf1d-413af3bd3912?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7803f3e5-1c19-486c-bf1d-413af3bd3912?resizing_type=fit)

If you follow this basic design, you'll be able to build in some randomized gameplay later where the end points change each round or game to encourage players to come back for a varied experience each time!

### Add a Player Spawner

Place a Player Spawner device on a side that does not have an entrance to the maze. This way, the player can select either entrance.

## Set Up the Random Number Generator Device

The **Random Number Generator** device is a powerful device that you can use to trigger other devices based on random input.

[![](https://dev.epicgames.com/community/api/documentation/image/51e36d63-3b5c-4fd8-b2b8-d66f0b872cac?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/51e36d63-3b5c-4fd8-b2b8-d66f0b872cac?resizing_type=fit)

The device can be configured to generate a random number that falls inside a range you set.
You can also customize it to generate a volume that extends off the device base. Any devices you place inside a segment of this volume will trigger when the number of that segment is rolled by the number generator.

Place the Random Number Generator device on your island, then customize it with the following settings.

[![](https://dev.epicgames.com/community/api/documentation/image/b225d4a8-95c0-43a2-b7b4-9e0bcce3956b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b225d4a8-95c0-43a2-b7b4-9e0bcce3956b?resizing_type=fit)

| Option | Value | Description |
| --- | --- | --- |
| **Value Limit 2** | 2 | The maximum number the device can roll. The minimum value defaults to 1, so with this set to 2, only a 1 or a 2 can be selected. |
| **Winning Value** | 0 | Since this isn't used to establish a win condition, you can set it to 0. |
| **Roll Time** | Instant | The result of the roll is instantly calculated. This value is set by entering 0.0. |
| **Zone Direction** | Left | Setting this to any value other than None will open a zone where devices can be placed that will be triggered. |
| **Length** | 2 | How long the zone is. The zone will be split into equal sections. |
| **Enabled During Phase** | Gameplay Only | You will only want the zone active during gameplay. |
| **Active on Phase** | Game Start | The device should become active at the start of the game. |

## Set Up Trigger Devices

You will add two **Trigger** devices, placing each one inside of a Random Number Generator device zone. The triggers will activate the color changing tile **clues** and the capture zones inside the maze.

[![](https://dev.epicgames.com/community/api/documentation/image/40ea2e3e-19bc-40f2-92f7-3b7546ba5f7d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/40ea2e3e-19bc-40f2-92f7-3b7546ba5f7d?resizing_type=fit)

Place the Trigger device fully inside the zone to ensure correct activation!

You will circle back in a later step to find out how to connect the Random Number Generator and Trigger devices with other devices used in the game.

You will set up one side of the maze fully, then copy and place the elements from one side to the other in a later step.

## Set Up the HUD Message Devices

You will use one HUD message to set the objective for the player at the start of the game, and four more to direct the player through the maze.

Setting up all of the messages ahead of time makes adding them to the maze much easier later.

You can also use **Billboard** devices to identify which HUD messages are tied to which devices. This step isn't necessary for gameplay, but it can help you to remember what the various devices are used for.

## Set Up the Capture Area Devices

You will use the Capture Area devices to set up the **end points** — one for each side of the maze.

Only one capture area is active at a time.

You will copy and place the second device in a later step.

## Set Up the Color Changing Tiles

In this example, you're placing sneaky triggers into the environment using Color Changing Tile devices to activate HUD messages as the player moves through the maze.

Using the tiles instead of standard triggers gives you an opportunity to color-code your messages as you're building your experience. As you lay out the tiles, the colors you choose can remind you where you should place your clues inside the maze.

This color-coding is for your benefit as you're building your mini-game. The tiles will not show during gameplay.

You will create two sets of these tiles. The first set will connect with **Capture Area_A** and the second with **Capture Area_B**.

[![](https://dev.epicgames.com/community/api/documentation/image/f7f945e7-e986-4b9b-9584-97e472808829?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f7f945e7-e986-4b9b-9584-97e472808829?resizing_type=fit)

- Set **Tile A1_COLD** to **light blue**.
- Set **Tile A1_WARMER** to **orange**.
- Set **Tile A1_HOT!** to **red**.

## Bind Devices for Capture Area_A

[Direct event binding](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#direct-event-binding) is how you set devices to communicate directly with other devices. Binding lets a device send a message to another device that can trigger another action or reaction. This involves setting [functions](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#function) and [events](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#event) for the devices involved.

For more on how direct event binding works, see **[Getting Started with Direct Event Binding](https://dev.epicgames.com/documentation/fortnite/getting-started-with-direct-event-binding-in-fortnite-creative)**.

All of the bindings you set here will be triggered by **Capture Area_A**.

## Place the Color Changing Tiles Inside the Maze

In the example below, Color Changing Tile devices have been placed in a sequence that follows the possible paths that a player might follow while exploring the maze.

[![](https://dev.epicgames.com/community/api/documentation/image/37165880-39c0-461b-a490-73e93f33efc4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/37165880-39c0-461b-a490-73e93f33efc4?resizing_type=fit)

The maze is in two sections that do not connect. Each has its own entry point and end point. You will set up the first section with the gameplay devices. In a later step, you will duplicate these devices and place the duplicates on the other side of the maze.

The **Cold** HUD message will display at the furthest point away from Capture Zone A. As the player gets closer to the capture point, more tiles are added that are configured to display additional clues such as **Warmer** and eventually **Hot!** closest to a capture zone.

Some of the tiles in the image above are red herrings — false leads intended to lure the player into exploring in the wrong direction! Players will have to pay attention to the HUD messages to get back on track toward the prize!

## Connect the First Area to the Random Number Generator

Next step is to set up the events that will activate the first Capture Zone device and its associated Color Changing Tile devices when this segment of the Random Number Generator device is selected.

## Set Up the B Side of the Maze

Starting with [Set Up the HUD Messages](https://dev.epicgames.com/documentation/fortnite/hud-message-device-design-example-in-fortnite-creative) section above, you will repeat the steps for the second side of the maze but name the devices with a **B** instead of an **A**.

## Finishing Touches

You're almost done!

And that's it!

You have successfully built a maze with two win-condition endpoints, one of which will be selected randomly when a player spawns into the island.

Pop-up HUD messages will appear on screen to let the player know if they are getting warmer or colder as they try to find the goal!

## Design Tip

To make the experience more intense, you could:

- Add a Timer device to the island. This puts pressure on the player to find the winning endpoint before time runs out.
- Set up team spawners, then add weapons in the maze. Teams would have an extra layer of gameplay as they hunt for the endpoint while eliminating other players!
- Add more endpoints to the Random Number Generator device for even more ways to win the game.
