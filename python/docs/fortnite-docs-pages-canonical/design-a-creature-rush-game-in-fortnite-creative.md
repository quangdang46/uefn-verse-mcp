## https://dev.epicgames.com/documentation/en-us/fortnite/design-a-creature-rush-game-in-fortnite-creative

# Creature Rush

Use devices like HUD Message and Creature Spawner to create a narrative-driven game with waves of enemies.

![Creature Rush](https://dev.epicgames.com/community/api/documentation/image/97d3eca1-0794-4fa7-bedd-84a225d4c377?resizing_type=fill&width=1920&height=335)

This tutorial is a single-player combat game that utilizes **HUD Messages** and **Billboard** devices to create a narrative during gameplay.

Players in this game will experience both internal and external dialogue as they shoot their way to victory, eliminating creatures that become become harder to fight over time,

Currently, only games with multiple players can set win/lose conditions for the end-of-round settings. Since this is a single-player game, players will achieve a victory even if they are eliminated.

Use this template if you want to learn how to use informational devices to creatively communicate game rules, storylines, and internal dialog to players. This template is also good for creating hoard-and-aim training games.

The sample island code for this tutorial is **9100-1332-5260**.

To play through this island, click **CHANGE** in the **Fortnite Lobby** screen. On the Discover screen, click the **Island Code** tab and enter the code for Creature Horde. Once you've seen all the gameplay features, you can explore this tutorial and recreate it on your own island.

## Devices Used

These devices were used for this island tutorial:

- 1 x [Pop-up Dialog device](https://dev.epicgames.com/documentation/fortnite/using-popup-dialog-devices-in-fortnite-creative)
- 1 x [Class Designer device](https://dev.epicgames.com/documentation/fortnite/using-class-designer-devices-in-fortnite-creative)
- 1 x [Conditional Button device](https://dev.epicgames.com/documentation/fortnite/using-conditional-button-devices-in-fortnite-creative)
- 2 x [Creature Spawner devices](https://dev.epicgames.com/documentation/fortnite/using-creature-spawner-devices-in-fortnite-creative)
- 1 x [Timer device](https://dev.epicgames.com/documentation/fortnite/using-timer-devices-in-fortnite-creative)
- 1 x [Damage Amplifier Powerup device](https://dev.epicgames.com/documentation/fortnite/using-damage-amplifier-powerup-devices-in-fortnite-creative)
- 2 x [Elimination Manager devices](https://dev.epicgames.com/documentation/fortnite/using-elimination-manager-devices-in-fortnite-creative)
- 1 x [End Game device](https://dev.epicgames.com/documentation/fortnite/using-end-game-devices-in-fortnite-creative)
- 1 x [Health Powerup device](https://dev.epicgames.com/documentation/fortnite/using-health-powerup-devices-in-fortnite-creative)
- 1 x [HUD Controller device](https://dev.epicgames.com/documentation/fortnite/using-hud-controller-devices-in-fortnite-creative)
- 4 x [HUD Message devices](https://dev.epicgames.com/documentation/fortnite/using-hud-message-devices-in-fortnite-creative)
- 4 x [Item Spawner devices](https://dev.epicgames.com/documentation/fortnite/using-item-spawner-devices-in-fortnite-creative)
- 1 x [Mutator Zone device](https://dev.epicgames.com/documentation/fortnite/using-mutator-zone-devices-in-fortnite-creative)
- 1 x [Player Spawn Pad device](https://dev.epicgames.com/documentation/fortnite/using-player-spawn-pad-devices-in-fortnite-creative)
- 2 x [Random Number Generator devices](https://dev.epicgames.com/documentation/fortnite/using-random-number-generator-devices-in-fortnite-creative)
- 5 x [Trigger devices](https://dev.epicgames.com/documentation/fortnite/using-trigger-devices-in-fortnite-creative)

## Props, Prefabs, and Galleries

A variety of **Prefab** and **Gallery** items were used to design this island. When recreating this island, test your creativity by envisioning a theme while mixing and matching items from various categories.

Be sure to fill any open areas with appealing props and terrains like grass and trees.

## Overview of Tutorial Steps

Following is an overview of the steps you'll need to recreate this island and their ideal sequence:

1. Create a new island using a [starter island](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#starter-island).
2. Customize the island settings.
3. Set up your island structure, such as an [arena](https://dev.epicgames.com/documentation/fortnite/building-arenas-in-fortnite-creative), using prefabs and galleries.
4. Set up the starting area.
5. Set up the enemy devices.
6. Set up the background devices.
7. Set up the end game devices.

## Create Your Island

To build your island, use the following steps.

The portal will automatically load and teleport you into the island.

Check out these short [video tutorials](https://dev.epicgames.com/documentation/fortnite/fortnite-creative-video-tutorials) to learn more about the beginning steps to create your island.

## Customize the Island Settings

These settings will create a single-player game where elimination stats are tracked on the HUD.

[![My Island Menus](https://dev.epicgames.com/community/api/documentation/image/6186a5fb-2f36-4d63-8226-7e8b701c8a13?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6186a5fb-2f36-4d63-8226-7e8b701c8a13?resizing_type=fit)

To modify gameplay settings, press the **TAB** key and click **MY ISLAND** at the top of the screen. From here, you can access the **GAME**, **SETTINGS**, and **UI** tabs.

### My Island - Game

| Modified Setting | Option | Explanation |
| --- | --- | --- |
| **Max Players** | 1 | There will only be one player in this game mode. |
| **Spawn Limit** | 1 | The player can only spawn one time. |
| **Default Class Identifier** | 1 | This sets the class that grants the initial weapon upon spawning. |

### My Island - Settings

| Modified Setting | Option | Explanation |
| --- | --- | --- |
| **Infinite Ammo** | On | The player will not have to pick up ammo. |
| **Allow Building** | None | There is no building in this game mode. |
| **Environment Damage** | Off | Damage from guns cannot destroy the environment. |
| **Start With Pickaxe** | No | The player will not need pickaxes for this game mode. |
| **Allow Slide** | On | The player can perform the [slide](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#slide) maneuver. |

### My Island - UI

| Modified Setting | Option | Explanation |
| --- | --- | --- |
| **HUD Info Type** | AI Enemy Elimination | The HUD will track enemy eliminations. |
| **Max Trackers On HUD** | 3 | There will be three HUD trackers. |
| **Win Condition** | Score | The end-game screen will show the player's ending score. |
| **First Scoreboard Column** | Score | The first HUD tracker will show the player's score. |
| **Second Scoreboard Column** | AI Eliminations | The second HUD tracker will show the creature eliminations. |
| **Third Scoreboard Column** | Time Alive | The third HUD tracker will show the player's time alive. |
| **Map Screen Display** | Scoreboard | The scoreboard is displayed if the player brings up the map screen. |

## Setting Up Your Island Structure

A mixture of Prefab and Gallery pieces were used to create this island. Check out [Building Arenas](https://dev.epicgames.com/documentation/fortnite/building-arenas-in-fortnite-creative) to learn more about building indoor and open arenas.

Creature Horde is an open outdoor arena with boundaries created by **Barriers**. These barriers were used along with decorative prop pieces to guide the player from one end of the island to another.

## Setting Up the Starting Area

[![Area Overview](https://dev.epicgames.com/community/api/documentation/image/cf54345a-1191-46f7-b735-a71f18e0c3e6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cf54345a-1191-46f7-b735-a71f18e0c3e6?resizing_type=fit)

*Use this image as a visual reference on device placement and creative possibilities.*

The starting area is where the player will initially spawn onto the island. When the player spawns, a pop-up displays before they can move.

In this section, you will use the following devices:

- **Player Spawn Pad**
- **Pop-Up Dialog**
- **Class Designer**
- **HUD Controller**

### Player Spawn Pad

[![Player Spawn Pad](https://dev.epicgames.com/community/api/documentation/image/1f76be62-2962-4f03-978d-e71ba47115ae?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1f76be62-2962-4f03-978d-e71ba47115ae?resizing_type=fit)

The player will initially spawn through the **Player Spawn Pad**. Once spawned, the Player Spawn Pad will transmit a signal to different devices.

To set up this device:

### Pop-Up Dialog

[![Pop-Up Dialog](https://dev.epicgames.com/community/api/documentation/image/7ec1af57-c930-41a1-8af6-6362316fe162?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7ec1af57-c930-41a1-8af6-6362316fe162?resizing_type=fit)

The **Pop-Up Dialog** displays a custom message when activated by another device. Once the player spawns, this device will display an informative message that directs a player to their objective.

To set up this device:

[![Pop-Up Message](https://dev.epicgames.com/community/api/documentation/image/96020f1c-f0ce-4d4f-8997-03a245b24a04?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/96020f1c-f0ce-4d4f-8997-03a245b24a04?resizing_type=fit)

### Class Designer

[![Class Designer](https://dev.epicgames.com/community/api/documentation/image/ad88e1fe-3867-4b2e-b62c-b9cd0643939f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ad88e1fe-3867-4b2e-b62c-b9cd0643939f?resizing_type=fit)

You can set the **Class Designer** to assign weapons to players based on their [class](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#class).

To set up this device:

**Dual Fiend Hunters** were used in Creature Horde.

### HUD Controller

[![HUD Controller](https://dev.epicgames.com/community/api/documentation/image/1635f648-4f7c-41eb-b761-8ce86adf5391?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1635f648-4f7c-41eb-b761-8ce86adf5391?resizing_type=fit)

Use the **HUD Controller** to change what information displays for players. This device can remove the minimap so the player can see enemies unobstructed.

To set up this device:

## Designer Tips

You can set the Pop-Up Dialog to send a signal once the player interacts with a dialog button. You can set both buttons to have individual text and transmit signals once interacted with.

## Setting Up Enemy Devices

[![Area Overview](https://dev.epicgames.com/community/api/documentation/image/8d4848a1-cf22-4bc1-8b48-6baefb38b705?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8d4848a1-cf22-4bc1-8b48-6baefb38b705?resizing_type=fit)

*Use the image as a visual reference on device placement and creative possibilities.*

There are various creatures that spawn for the player to eliminate. You can set these creatures to also spawn behind where the players walk so that they can battle from various directions.

In this section you will use the following devices:

- **Creature Spawner**
- **Mutator Zone**
- **Timer**

### Creature Spawners 1-2

[![Creature Spawner](https://dev.epicgames.com/community/api/documentation/image/ce4165de-1783-4e9e-b62d-0ae29f045aaf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ce4165de-1783-4e9e-b62d-0ae29f045aaf?resizing_type=fit)

Set creatures to initially spawn in small groups with a low spawn limit to match. As the game progresses, spawn creatures with various wave times in larger amounts. You can set spawn limits to control the disbursement of enemies.

To set up these devices:

### Mutator Zone

[![Mutator Zone](https://dev.epicgames.com/community/api/documentation/image/c86d22f5-7728-44e1-93e2-5bdac96343b1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c86d22f5-7728-44e1-93e2-5bdac96343b1?resizing_type=fit)

You can use the **Mutator Zone** to apply a variety of effects to players and creatures who enter the area. For this gameplay, use Mutator Zones to serve as a trigger that sends a signal to another device once the player enters it.

To set up this device:

## Designer Tips

Creature Horde uses internal dialogue that triggers when players reach a certain area. You can set the Mutator Zone to trigger HUD messages to appear on screen for the player. Set a **HUD Message** device to the same channel as the Mutator Zone to display messages or even internal dialogue.

[![HUD Message](https://dev.epicgames.com/community/api/documentation/image/e43910d7-84f9-4a1b-97b5-67e5e4ccbcf8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e43910d7-84f9-4a1b-97b5-67e5e4ccbcf8?resizing_type=fit)

### Timer

[![Timer](https://dev.epicgames.com/community/api/documentation/image/2d6f5fa9-fe7d-4ef1-abc3-6e45577d726d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2d6f5fa9-fe7d-4ef1-abc3-6e45577d726d?resizing_type=fit)

Set the Mutator Zone to the same channel as a **Timer** to make the creatures to spawn after a certain amount of time. You can set a second Creature Spawner to enable behind the player, spawning seconds after they enter the Mutator Zone. This can be done so the player must battle from multiple directions.

To set up this device:

Place a combination of the devices from this section to create [gameplay](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#gameplay) where the player encounters more enemies as they progress forward. These enemies could randomly spawn in various directions after being triggered by the player.

You can also use [Creature Placers](https://dev.epicgames.com/documentation/fortnite/using-creature-placer-devices-in-fortnite-creative) instead of Creature Spawners to place individual enemies.

## Setting Up Background Devices

[![Area Overview](https://dev.epicgames.com/community/api/documentation/image/3471fef9-0b08-43f0-b87e-2af393b12796?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3471fef9-0b08-43f0-b87e-2af393b12796?resizing_type=fit)

*Use the image as a visual reference on device placement and creative possibilities.*

The background devices for this gameplay trigger text callouts from an enemy's elimination. Through this device, there is a 33 percent chance that a creature's elimination will trigger a text. When that text appears, four options can be displayed.

Set up these devices in an isolated area where the player cannot see.

In this section, you will use the following devices:

- **Elimination Manager**
- **Random Number Generator**
- **Trigger**
- **HUD Message Device**

### Elimination Managers 1-2

[![Elimination Manager](https://dev.epicgames.com/community/api/documentation/image/cdb60a06-423e-4c18-8821-0cd528e58735?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cdb60a06-423e-4c18-8821-0cd528e58735?resizing_type=fit)

Use the **Elimination Manager** to set the conditions when a player or creature is eliminated. In this gameplay, the Elimination Manager sends a signal to a different device every time a creature is eliminated.

To set up these devices:

### Random Number Generators 1-2

[![Random Number Generator](https://dev.epicgames.com/community/api/documentation/image/61b6c1e8-6740-468d-966e-55ac3841ebf6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/61b6c1e8-6740-468d-966e-55ac3841ebf6?resizing_type=fit)

Use the **Random Number Generator** to generate random numbers that can transmit signals to receiving channels. In this gameplay, whenever a creature is eliminated, the Elimination Manager sends a signal to the Random Number Generator. A pair of these devices creates a system that rolls for a 33 percent chance of hitting a trigger that displays one out of four messages.

To set up these devices:

Place a second Random Number Generator to receive a signal when the sequencer lands on a**Trigger**. When the second RNG is activated, it will roll to activate one of the four HUD Messages.

To set up the second device:

### Triggers 1-5

[![Trigger](https://dev.epicgames.com/community/api/documentation/image/cd97e232-ceca-46a9-a2c2-15859b4b4ca5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cd97e232-ceca-46a9-a2c2-15859b4b4ca5?resizing_type=fit)

If the first Random Number Generator's sequencer lands on the third space, it will hit a Trigger that will send a signal to the second RNG device.

To set up this device:

For each space on the second Random Number Generator's sequencer, place both a Trigger and a HUD Message device. This is the last part of the system that will display a HUD message whenever a creature is eliminated. Each time the sequencer lands on one of the spaces, a trigger will signal for a customized message to be displayed.

To set up the second through fifth devices:

### HUD Message Devices 1-4

[![Creature Horde Gameplay](https://dev.epicgames.com/community/api/documentation/image/fd6aaa46-b9d7-4138-9d3d-5a0791a36317?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fd6aaa46-b9d7-4138-9d3d-5a0791a36317?resizing_type=fit)

## Setting Up End Game Devices

[![Area Overview](https://dev.epicgames.com/community/api/documentation/image/8886bab7-627d-43ba-a31f-fadad5726b58?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8886bab7-627d-43ba-a31f-fadad5726b58?resizing_type=fit)

*Use the image as a visual reference on device placement and creative possibilities.*

The gameplay ends with the two boss creatures you placed earlier. These creatures will drop **Cube Monster Parts** when eliminated. Players will insert these items into the Conditional button, which will send a signal to the **End Game** device once the items are consumed.

In this section, you will use the following devices:

- **Conditional Button**
- **End Game**

### Conditional Button

[![Conditional Button](https://dev.epicgames.com/community/api/documentation/image/156c047b-90a9-4f33-b8b5-a40b041351e5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/156c047b-90a9-4f33-b8b5-a40b041351e5?resizing_type=fit)

You can modify the **Conditional Button** to activate when players are carrying registered items. When activated, this device can transmit a signal to a receiving device.

To set up this device:

## Designer Tip

[![Designer Tip](https://dev.epicgames.com/community/api/documentation/image/f17e373c-0dba-4f71-a79d-6898ba37b97a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f17e373c-0dba-4f71-a79d-6898ba37b97a?resizing_type=fit)

To strengthen your gameplay design, use props from the **Prefabs** and **Galleries** tabs to blend with the **Conditional Button**. Place the **Conditional Button** inside a prop so that only its image will show.

### End Game Device

[![End Game](https://dev.epicgames.com/community/api/documentation/image/01b59a41-31ec-4cd4-8c3e-191aed42f93c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/01b59a41-31ec-4cd4-8c3e-191aed42f93c?resizing_type=fit)

You can set devices like the Conditional Button to transmit a signal for the End Game device to activate. Once activated, this device can end the game.

To set up this device:

You have successfully designed your own creature rush game.
