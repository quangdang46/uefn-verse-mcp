## https://dev.epicgames.com/documentation/en-us/fortnite/loadout-lobby-gameplay-example-in-fortnite-creative

# Loadout Lobby

Loadout Lobby is a pre-game waiting room, where players gather to load up on weapons before being spawned on the island.

![Loadout Lobby](https://dev.epicgames.com/community/api/documentation/image/23b626c4-3df7-4034-afd1-4d2f13548f27?resizing_type=fill&width=1920&height=335)

The **Loadout Lobby** acts like a waiting room, where the players gather pre-game to load up on weapons before [spawning](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#spawning) at various locations on the island. When players are eliminated, they respawn in the lobby where they can then use the teleporter to reenter the game.

[![A player in the Loadout Lobby at the start of the game](https://dev.epicgames.com/community/api/documentation/image/780befb1-e6f6-4faf-85cf-7d2d1521c9c4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/780befb1-e6f6-4faf-85cf-7d2d1521c9c4?resizing_type=fit)

*Click image to enlarge.*

This gameplay example shows how to use and coordinate the following devices:

- Barrier device
- HUD Message device
- Mutator Zone device
- Player Spawn device
- Random Number Generator device
- Teleporter device
- Timed Objective device
- Trigger device
- Vending Machine device

## Devices Used

For help with placing [props](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#prop) and using the [grid](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#grid), refer to the [Video Tutorials](https://dev.epicgames.com/documentation/fortnite/fortnite-creative-video-tutorials).

Search for the required devices in the [Devices tab](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) in the [Creative inventory](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary).

- 1 per Player x [Player Spawn Pad device](https://dev.epicgames.com/documentation/fortnite/using-player-spawn-pad-devices-in-fortnite-creative)
- 1 per Player +1 extra x [Teleporter device](using-teleporter-devices-in-fortnite-creative)
- As many as you like x [Vending Machine](https://dev.epicgames.com/documentation/fortnite/using-vending-machine-devices-in-fortnite-creative)
- 2 x [Timed Objective devices](https://dev.epicgames.com/documentation/fortnite/using-timed-objective-devices-in-fortnite-creative)
- 1 x [Random Number Generator device](https://dev.epicgames.com/documentation/fortnite/using-random-number-generator-devices-in-fortnite-creative)
- 2 x [Mutator Zone devices](https://dev.epicgames.com/documentation/fortnite/using-mutator-zone-devices-in-fortnite-creative)
- 1 x [Barrier device](using-barrier-devices-in-fortnite-creative)
- 1 less than the number of Teleporter devices x [Trigger devices](https://dev.epicgames.com/documentation/fortnite/using-trigger-devices-in-fortnite-creative)

## Prefabs Used

This example was built using the **Hangar** [prefab](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#prefab). You can use any structure from the Prefabs tab, or build your own structure from available [resources](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#resource).

To access the prefabs, open the **Creative inventory**, and click the **Prefabs** tab. Search for the Hangar prefab, or pick another prefab of your choice to use.

[![The Hangar prefab in the Prefabs tab](https://dev.epicgames.com/community/api/documentation/image/f96cdb90-9824-4cbb-88bc-d6be1f2deed9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f96cdb90-9824-4cbb-88bc-d6be1f2deed9?resizing_type=fit)

*Click image to enlarge.*

To make your lobby easily accessible, use prefabs that are spacious, like the Barn or the Hangar.

## Setting Up the Devices

Find the devices you need in the **Devices** tab of the **Creative Inventory** and add them to your **Quick Bar**.

[![Fully equipped Quick Bar](https://dev.epicgames.com/community/api/documentation/image/4dab7bd8-0c3e-4dec-a362-e4624a32023f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4dab7bd8-0c3e-4dec-a362-e4624a32023f?resizing_type=fit)

Use the **Search** option in the Creative Inventory to easily locate your devices.

When placing devices, putting all background devices in the same location minimizes the time you spend traveling between various devices.

When using multiple copies of a device on your island, it can be helpful to [rename](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#rename-a-device) them. You can choose names that relate to each device's purpose, so it's easier to remember what each one does.

### Setting Up the Player Spawn Pad Devices

The **Player Spawn Pads** are devices you use to define where the players spawn at the beginning of the gameplay, and respawn during gameplay.

### Setting Up the Mutator Zone Devices

The **Mutator Zone** devices are used to make the lobby a [safe zone](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#safe-zone), and to [teleport](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#teleport) the players into the gameplay area.

### Setting Up the Timed Objective Devices

The **Timed Objective** devices are used to count down to the players teleporting into the gameplay area.

### Setting Up the Teleporter Devices

When the initial countdown ends, the players are randomly teleported to one of the Teleporter devices set up around the island.

### Setting Up the Vending Machine Devices

Players can load up before spawning into the game using the **Vending Machine** devices you place in the lobby.

### Setting Up the Random Number Generator Device

You're going to use the Random Number Generator to ensure that each player is spawned in a different location on the island each time they spawn.

### Setting Up the Trigger Devices

The setup described below means that when the Random Number Generator is activated, a different **Trigger** device is activated for each player, which in turn transports the triggering player to the corresponding teleport location on the island.

### Setting Up the Barrier Device

The **Barrier** device keeps the teleporter in the spawn area locked during the initial loadout. It is opened at the end of the first countdown so returning players can rejoin the game whenever they choose using the teleporter.

## Putting It All Together

The final gameplay provides the player with a Loadout Lobby that can be added to any island they create. Players load up on weapons before being spawned into the game. When eliminated, players are respawned into the lobby before reentering the game through a Teleporter.
