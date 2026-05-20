## https://dev.epicgames.com/documentation/en-us/fortnite/using-atk-spawner-device-design-examples-in-fortnite-creative

# ATK Spawner Device Design Example

Make a collecting game where players compete with ATKs!

![ATK Spawner Device Design Example](https://dev.epicgames.com/community/api/documentation/image/b0da4ad5-2a55-4b0e-9582-8b3d49382391?resizing_type=fill&width=1920&height=335)

The **ATK Spawner** device spawns an all-terrain kart (ATK) that you can place players into directly at the start of the game, or that they can choose to drive during the game.

## The Great ATK Collectibles Race!

In this design example, you'll use several devices to create a fun multiplayer-team game. The game is constructed around a “hidden” feature of the ATK — players can use the awning on the top of the kart as a bounce pad!

This team-based mini-game can be used by up to sixteen players, balanced over four teams of four.

The teams must race to see who can gather the four collectible objects from four corners of the play space first!

## Devices Used

- 4 x [**ATK Spawner**](using-atk-spawner-devices-in-fortnite-creative) devices
- 4 x [Button](https://dev.epicgames.com/documentation/fortnite/using-button-devices-in-fortnite-creative) devices
- 16 x [Collectible Object](https://dev.epicgames.com/documentation/fortnite/using-collectibles-object-devices-in-fortnite-creative) devices
- 16 x [Player Spawner](https://dev.epicgames.com/documentation/fortnite/using-player-spawn-pad-devices-in-fortnite-creative) devices

## Build Your Own

Construct the initial play space, then continue to build it out as you place and customize the devices you'll need to create the game mechanics.

### Construct the Starting Area

Teams start in the center of the play area where ATK vehicles for each team will spawn.

### Add ATK Spawners

### Add Button Devices

Each team will have its own button. Once the game starts, players must push their team's button to spawn or respawn their ATKs.

### Add Player Spawners

Your players will spawn outside of the starting area.

[![](https://dev.epicgames.com/community/api/documentation/image/12dff34f-1756-4fee-971d-5d3a01246bd9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/12dff34f-1756-4fee-971d-5d3a01246bd9?resizing_type=fit)

Place four groups of four player spawners each. Each group will be on a different side of the starting area, with each assigned to a different team.

### Finish Constructing the Play Space

The next part of the gameplay area involves placing floating platforms that are too high for a player to jump to, but that can be reached by using an ATK awning as a bounce pad. Check the height for each floating platform to make sure that players can bounce off the roof of the ATK and reach the top in a single jump.

These platforms will hold the objects players need to collect.

You will also place assorted objects to get in the way of players traversing the area.

### Place Collectible Objects

This game uses four collectible objects for each team, configured to be picked up by one of the four teams. You will place these objects above each large floating platform.

You can place objects for a single team all on one platform, or you can put one object per team on each platform, which will force a team to go to each platform.

Objects for a single team can all be the same, or you can mix and match just to make the game a little more zany.

[![](https://dev.epicgames.com/community/api/documentation/image/f8d2dc5e-5ab4-4565-a2ae-5c8ccc377cc0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f8d2dc5e-5ab4-4565-a2ae-5c8ccc377cc0?resizing_type=fit)

A player can collect an object by coming into contact with it.

### Bind Devices

[Direct event binding](https://dev.epicgames.com/documentation/fortnite/getting-started-with-direct-event-binding-in-fortnite-creative) is how devices communicate with each other. There are several bindings you'll need to set up for the game mechanics to work correctly. With all of your devices in place, you can now bind them to work together.

### Configure the Island Settings

The final step is to customize the [Island Settings](https://dev.epicgames.com/documentation/fortnite/understanding-island-settings-in-fortnite-creative).

And there you have it! This example is a little more complex than some of the other design examples, but when you get multiple players on the island, racing and bouncing for the collectibles, it can be a riot of fun!

## Design Tips

You now have a unique 16-player game featuring the ATK vehicle! Try adding various weapons or other devices to the game to make it even more interesting.
