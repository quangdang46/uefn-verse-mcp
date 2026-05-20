## https://dev.epicgames.com/documentation/en-us/fortnite/design-a-prop-hunt-game-in-fortnite-creative

# Prop Hunt Game Tutorial

Learn how to use devices like the Class Designer to create a game where players must either disguise themselves as props or search for hidden players.

![Prop Hunt Game Tutorial](https://dev.epicgames.com/community/api/documentation/image/b30928d6-1395-4c42-a015-d59b6611042b?resizing_type=fill&width=1920&height=335)

In this gameplay, teams of Hunters and Props will compete to be the last team standing before the timer runs out. The Prop team will use the **Prop-O-Matic** weapon to disguise themselves as props while the Hunter team searches. This tutorial will teach you how to use devices like the **Player Counter** to track how many players are left alive on a team.

The island code for this tutorial is **3556-6223-1265**.

To play through this island, click **CHANGE** on the **Fortnite Lobby** screen. On the **Discover** screen, click the **Island Code** tab and enter the code for **Design a Prop Hunt Game**. Once you've seen all the gameplay features, you can explore this tutorial and recreate it on your island.

## Props, Prefabs, and Galleries

A variety of [Prefab](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#prefab) and [Gallery](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#gallery) items were used to design this island. When recreating this island, test your creativity by envisioning a theme while mixing and matching items from various categories.

Be sure to fill any open areas with appealing props that matches your island's theme.

Read the prerequisite tutorials to learn how to use Gallery pieces to build pre-game lobbies and arenas.

## Overview of Tutorial Steps

The following is an overview of the steps you'll need to recreate this island and its ideal sequence:

1. Create a new island using a [starter island](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#starter-island).
2. Set up your island structure, such as an [arena](https://dev.epicgames.com/documentation/fortnite/building-arenas-in-fortnite-creative).
3. Set up the [pre-game lobby](https://dev.epicgames.com/documentation/fortnite/building-pregame-lobbies-in-fortnite-creative).
4. Set up the Hunter class.
5. Spawn Hunters onto the map.
6. Spawn Props onto the map.
7. Set up the Collectible Objects.
8. Set up the game ending devices.
9. Customize the island settings.

## Set up the Hunter Class

[![Area Overview](https://dev.epicgames.com/community/api/documentation/image/d0295b76-7fa6-46ce-8cbb-26839f3f81cd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d0295b76-7fa6-46ce-8cbb-26839f3f81cd?resizing_type=fit)

*Use the photo as a visual reference on device placement and creative possibilities.*

Use **Class Selectors** to change Hunters to their team on spawn. The **Class Designer** will give Hunters their loadout.

In this section, you will use the following devices:

- 3 x [Class Selector devices](https://dev.epicgames.com/documentation/fortnite/using-class-selector-devices-in-fortnite-creative)
- 1 x [Class Designer device](https://dev.epicgames.com/documentation/fortnite/using-class-designer-devices-in-fortnite-creative)

### Class Selector #1 - 3

[![Class Selector](https://dev.epicgames.com/community/api/documentation/image/e1c5a441-4276-4aac-b2c2-2086a6c1947d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e1c5a441-4276-4aac-b2c2-2086a6c1947d?resizing_type=fit)

Use a Class Selector to designate a class for your players.

To set up this device:

### Class Designer #1

[![Class Designer](https://dev.epicgames.com/community/api/documentation/image/e43aef09-4bb2-4119-a664-595cf6622fc7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e43aef09-4bb2-4119-a664-595cf6622fc7?resizing_type=fit)

You can use a Class Designer to designate a loadout for each class.

To set up this device:

## Spawn Hunters onto the Map

[![Area Overview](https://dev.epicgames.com/community/api/documentation/image/a0a7934b-f15a-43bc-8d20-16e5b0170539?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a0a7934b-f15a-43bc-8d20-16e5b0170539?resizing_type=fit)

*Use the photo as a visual reference on device placement and creative possibilities.*

Create an area like a pre-game lobby for Hunters to spawn and read the game rules. This will be the area where Hunters while they wait for Props to hide. After a designated amount of time, Hunters will teleport to the main arena to begin their hunt.

In this section, you will use the following devices:

- 3 x [Player Spawn Pad devices](https://dev.epicgames.com/documentation/fortnite/using-player-spawn-pad-devices-in-fortnite-creative)
- 3 x [Player Reference devices](https://dev.epicgames.com/documentation/fortnite/using-player-reference-devices-in-fortnite-creative)
- 2 x [Timed Objective devices](https://dev.epicgames.com/documentation/fortnite/using-timed-objective-devices-in-fortnite-creative)
- 3 x [Teleporter devices](https://dev.epicgames.com/documentation/fortnite/using-teleporter-devices-in-fortnite-creative)

### Player Spawn Pad #1 - 3

[![Player Spawn Pad](https://dev.epicgames.com/community/api/documentation/image/9fbd6013-e66d-42d6-a81b-2c785691b3cc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9fbd6013-e66d-42d6-a81b-2c785691b3cc?resizing_type=fit)

Use **Player Spawn Pads** to spawn Hunters in the pre-game lobby.

To set up this device:

### Player Reference

[![Player Reference](https://dev.epicgames.com/community/api/documentation/image/ebb3ed27-8c99-4a80-97e5-81defb22243a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ebb3ed27-8c99-4a80-97e5-81defb22243a?resizing_type=fit)

Use the **Player Reference** to pair with the Player Spawn Pads, allowing Hunters to teleport from the pre-game lobby to the arena with a single device.

To set up this device:

## Timed Objective #1

[![Timed Objective](https://dev.epicgames.com/community/api/documentation/image/d0dbc5aa-99ee-4448-9feb-6121b0d2315a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d0dbc5aa-99ee-4448-9feb-6121b0d2315a?resizing_type=fit)

Use a **Timed Objective** to keep Hunters in their pre-game lobby until the Porps have time to hide, triggering a teleport on completion.

To set up this device:

### Teleporter #1 - 3

[![Teleporter](https://dev.epicgames.com/community/api/documentation/image/52bceaa3-3eaf-4d7c-b246-8a7e6b23ab3a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/52bceaa3-3eaf-4d7c-b246-8a7e6b23ab3a?resizing_type=fit)

Assign **Teleporters** to the Hunters to bring them into the arena once the 30-second timer elapses.

To set up this device:

## Spawn Props onto the Map

[![Area Overview](https://dev.epicgames.com/community/api/documentation/image/353e30fd-7d54-4468-bdc7-6062a11f2766?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/353e30fd-7d54-4468-bdc7-6062a11f2766?resizing_type=fit)

*Use the photo as a visual reference on device placement and creative possibilities.*

Place Player Spawn Pads in a central location for Props to move out and begin blending in.

In this section, you will use the following devices:

- 8 x [Player Spawn Pad devices](https://dev.epicgames.com/documentation/fortnite/using-player-spawn-pad-devices-in-fortnite-creative)
- 1 x [HUD Message device](https://dev.epicgames.com/documentation/fortnite/using-hud-message-devices-in-fortnite-creative)
- 1 x [Class Designer device](https://dev.epicgames.com/documentation/fortnite/using-class-designer-devices-in-fortnite-creative)

### Player Spawn Pad #4 - 11

Use Player Spawn pads to spawn Props in the arena.

To set up this device:

### HUD Message

[![HUD Message](https://dev.epicgames.com/community/api/documentation/image/07b8aeb7-846d-4bfc-9428-ef9b9cec8f86?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/07b8aeb7-846d-4bfc-9428-ef9b9cec8f86?resizing_type=fit)

Use a **HUD Message** to onboard Props when they load into the game.

To set up this device:

### Class Designer

Use a Class Designer to grant Props the Prop-O-Matic weapon and adjust health, movement, speed, and other core options.

To set up this device:

## Designer Tips

[![Designer Tips](https://dev.epicgames.com/community/api/documentation/image/cf7a55ea-45cc-4749-89a6-d7feda6c0045?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cf7a55ea-45cc-4749-89a6-d7feda6c0045?resizing_type=fit)

Surround the maps with **Barriers** for a visual aesthetic and to keep players in the arena.

### Set up the Collectible Objects

[![Area Overview](https://dev.epicgames.com/community/api/documentation/image/541cf5d9-53db-4270-a3d1-0588dd97fdd7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/541cf5d9-53db-4270-a3d1-0588dd97fdd7?resizing_type=fit)

*Use the photo as a visual reference on device placement and creative possibilities.*

Spread collectibles throughout the arena to give an alternative win condition to players. These items can only be picked up by Props, cause a mild debuff to Props, and make the other coins unavailable for a time. It takes 10 collectibles to win.

In this section, you will use the following devices:

- 10 x [Collectible Object devices](https://dev.epicgames.com/documentation/fortnite/using-collectibles-object-devices-in-fortnite-creative)
- 1 x [Movement Modulator device](https://dev.epicgames.com/documentation/fortnite/using-movement-modulator-devices-in-fortnite-creative)
- 2 x [Timed Objective devices](https://dev.epicgames.com/documentation/fortnite/using-timed-objective-devices-in-fortnite-creative)

### Collectible Object

[![Collectible Object](https://dev.epicgames.com/community/api/documentation/image/3ccbed8a-6432-483e-a629-6df6e3eb4644?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3ccbed8a-6432-483e-a629-6df6e3eb4644?resizing_type=fit)

Use **Collectible Objects** for Props to collect in your arena.

To set up this device:

### Movement Modulator

[![Movement Modulator](https://dev.epicgames.com/community/api/documentation/image/bbac2715-8fae-432f-a28b-ffa3f50e79d3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bbac2715-8fae-432f-a28b-ffa3f50e79d3?resizing_type=fit)

Use a **Movement Modulator** to debuff Props when a Coin is picked up.

To set up this device:

### Timed Objective 2 - 3

Use **Timed Objective** devices to activate and reset coins.

To set up this device:

## Designer Tips

Large groupings of the same or similar props can create inconspicuous areas for Props to hide. This allows more interplay when the hunter is close.

[![Designer Tips](https://dev.epicgames.com/community/api/documentation/image/7c4d2998-b1c9-4cac-b7c7-4fd0a13708ab?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7c4d2998-b1c9-4cac-b7c7-4fd0a13708ab?resizing_type=fit)

You can also assemble large groups of props that fit your theme to make it easier to select and build your level out seamlessly. Make sure to find a balance between density and variety to make sure you have a level playing field.

## Set up the Game Ending Devices

[![Area Overview](https://dev.epicgames.com/community/api/documentation/image/97f1f19e-e4b2-473b-ae99-76d4a1370afc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/97f1f19e-e4b2-473b-ae99-76d4a1370afc?resizing_type=fit)

*Use the photo as a visual reference on device placement and creative possibilities.*

The **End Game** and **Player Counters** will end the game if either team has zero players left.

In this section, you will use the following devices:

- 2 x [Player Counter devices](https://dev.epicgames.com/documentation/fortnite/using-player-counter-devices-in-fortnite-creative)
- 2 x [End Game devices](https://dev.epicgames.com/documentation/fortnite/using-end-game-devices-in-fortnite-creative)

### Player Counter #1 - 2

[![Player Counter](https://dev.epicgames.com/community/api/documentation/image/933df9a6-72f2-442d-8000-f95b3eea8abf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/933df9a6-72f2-442d-8000-f95b3eea8abf?resizing_type=fit)

Use a **Player Counter** to determine how many players are in the game.

To set up this device:

### End Game #1 - 2

[![End Game](https://dev.epicgames.com/community/api/documentation/image/9fc10f72-c7bd-46f2-a881-7fc5ada624a7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9fc10f72-c7bd-46f2-a881-7fc5ada624a7?resizing_type=fit)

Use the **End Game** device to end the game when receiving a signal from the Player Counter.

To customize this device:

## Customize the Island Settings

These settings will create dynamic teams of two where players switch every round.

[![My Island Menus](https://dev.epicgames.com/community/api/documentation/image/a86a7ae5-8812-488c-8e1c-2aaace722109?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a86a7ae5-8812-488c-8e1c-2aaace722109?resizing_type=fit)

To modify gameplay settings, press the **TAB** key and click **MY ISLAND** at the top of the screen. From here, you can access the **GAME**, **SETTINGS**, and **UI** tabs.

### My Island - Game

| Modified Setting | Option | Explanation |
| --- | --- | --- |
| **Max Players** | 11 | The maximum number of players will be 11. |
| **Max Teams** | 2 | This gameplay will have two teams. |
| **Team Size** | Dynamic | Allows devices to set team sizes to allow for asymmetric teams. |
| **Default Class Identifier** | 2 | The default class identifier is 2. |
| **Spawn Limit** | 1 | Players can only spawn one time. |
| **Total Rounds** | 5 | There will be 5 rounds in this gameplay. |
| **Team Rotation** | Every Round | The teams will rotate every round. |
| **Time Limit** | 5 Minutes | The gameplay will last 5 minutes. |
| **Game Win Condition** | Most Round Wins | The team with the most rounds win the game. |
| **Collect Items to End** | 10 | 10 Collectible Objects must be collected to win. |

### My Island - Settings

| Modified Setting | Option | Explanation |
| --- | --- | --- |
| **Allow Building** | None | Building will not be allowed in this gameplay. |
| **Start With Pickaxe** | No | Players will not need pickaxes in this gameplay. |
| **Allow Mantling** | Off | Players will not mantle in this gameplay. |
| **Self-Damage On Hit Amount** | 3 | Players will take three points of self-damage when hitting an object. |
| **Self-Damage Only On Non-Zero Damage** | Yes | Zero damage hits will not trigger self-damage. |
| **Self-Damage Target Filter** | Non-Players | When hitting non-players, Hunters will take damage. |

### UI

| Modified Setting | Option | Explanation |
| --- | --- | --- |
| **Game Winner Display Time** | 3 Seconds | The game winner will be displayed for three seconds. |
| **Game Score** | 7 Seconds | The game score will be displayed for seven seconds. |
| **Round Winner** | 3 Seconds | The round winner will be displayed for three seconds. |
| **Round Score** | 7 Seconds | The round score will be displayed for seven seconds. |
| **Round Win Condition** | Collect Items | The game will be won when items are collected. |
| **Tiebreaker 1** | Time Alive | The tiebreaker among teams will be the time alive. |
| **First Scoreboard Column** | Collect Items | The first column in the scoreboard will track the items collected. |
| **Second Scoreboard Column** | Time Alive | The second column in the scoreboard will track the time alive. |
| **Third Scoreboard Column** | Eliminations | The third column in the scoreboard will track eliminations. |
