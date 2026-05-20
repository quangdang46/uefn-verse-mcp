## https://dev.epicgames.com/documentation/en-us/fortnite/create-a-hoverboard-race-in-fortnite-creative

# Hoverboard Race

Design a 15-lap race using Hoverboards and Race Checkpoint devices.

![Hoverboard Race](https://dev.epicgames.com/community/api/documentation/image/99f1fd3f-9a3d-40c2-babd-0b9dbe6bb3f8?resizing_type=fill&width=1920&height=335)

This tutorial is based on an island you can load in Creative, called Hoverboard Racing Island. The [island code](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#island-code) for this tutorial island is [1544-4420-3963](https://www.epicgames.com/fortnite/en-US/creative/island-codes/hover-race-island-1544-4420-3963).

This is an advanced tutorial, and it assumes you have basic knowledge of creating islands in Fortnite Creative. It is a more advanced version of the [Car Racing Tutorial](https://dev.epicgames.com/documentation/fortnite/design-a-car-racing-game-in-fortnite-creative).

## Island Description

The Hoverboard Racing Island is a race for up to eight players that are all riding hoverboards. The players cannot get off the hoverboards, and must complete 20 checkpoints (4 laps) to win the race. The track is enclosed. Players can leave the track, but to prevent players from accidentally driving off the edge of the island, [damage volumes](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#damage-volume) placed around the edge of the island will eliminate them.

While racing on the track, the players are able to collect random [power-ups](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#power-up) that can be used to help the player win the race. There are also Speed Boost tiles that increase the player's speed and Bouncer tiles that propel the player high into the air.

## Devices Used

These devices were used for this gameplay example:

- [Player Spawner Device](https://dev.epicgames.com/documentation/fortnite/using-player-spawn-pad-devices-in-fortnite-creative)
- [Barrier Device](https://dev.epicgames.com/documentation/fortnite/using-barrier-devices-in-fortnite-creative)
- [Score Manager Device](https://dev.epicgames.com/documentation/fortnite/using-score-manager-devices-in-fortnite-creative)
- [Timed Objective Device](https://dev.epicgames.com/documentation/fortnite/using-timed-objective-devices-in-fortnite-creative)
- [Trigger Device](https://dev.epicgames.com/documentation/fortnite/trigger-device-design-examples)
- [Race Manager Device](https://dev.epicgames.com/documentation/fortnite/using-race-manager-devices-in-fortnite-creative)
- [Driftboard Spawner Device](https://dev.epicgames.com/documentation/fortnite/using-driftboard-spawner-devices-in-fortnite-creative)
- [Race Checkpoint Device](https://dev.epicgames.com/documentation/fortnite/using-race-checkpoint-devices-in-fortnite-creative)
- [Tracker Device](https://dev.epicgames.com/documentation/fortnite/using-tracker-devices-in-fortnite-creative)
- [Item Granter Device](https://dev.epicgames.com/documentation/fortnite/using-item-granter-devices-in-fortnite-creative)
- [HUD Message Device](https://dev.epicgames.com/documentation/fortnite/using-hud-message-devices-in-fortnite-creative)
- [Visual Effect Powerup Device](https://dev.epicgames.com/documentation/fortnite/using-visual-effect-powerup-devices-in-fortnite-creative)
- Speed Boost
- [Bouncer Gallery Device](https://dev.epicgames.com/documentation/fortnite/using-bouncer-gallery-devices-in-fortnite-creative)
- [Damage Volume Device](https://dev.epicgames.com/documentation/fortnite/using-damage-volume-devices-in-fortnite-creative)
- [VFX Spawner Device](https://dev.epicgames.com/documentation/fortnite/using-vfx-spawner-devices-in-fortnite-creative)

## Overview of Tutorial Steps

Here is an overview of the steps you'll need to take to recreate the Hoverboard Racing Island:

1. Create a new island using a [starter island](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#starter-island).
2. Build the racetrack (not demonstrated in this tutorial).
3. Create the island boundaries.
4. Build the starting grid for the race (this includes Player Spawners).
5. Add and set up the race [checkpoints](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#checkpoint).
6. Add and set up the [Score Manager](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#score-manager) device.
7. Add and set up the [Race Manager](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#race-manager) device.
8. Add and set up the power-ups and special tiles.
9. Change My Island settings to set up the game.
10. Build the Pre-Game Lobby for the game.

There is a section with [Designer Tips](https://dev.epicgames.com/documentation/fortnite/create-a-hoverboard-race-in-fortnite-creative#designer-tips) at the end of this tutorial that gives you advice, more ideas for building your game, and even other islands you can make based on this one.

## Create Your Island

In this tutorial, you won't learn how to build the layout of the racetrack. Instead, you will learn which specific devices and settings you need to add to recreate the Hoverboard Racing Tutorial Island. If you completed the [Car Racing Tutorial](design-a-car-racing-game-in-fortnite-creative), you can build your racetrack using the same materials and methods you used in building that Island.

If you haven't completed the Car Racing Tutorial, you can look for **Galleries** in the **Creative Inventory** that have elements you can use, such as ones with the **Racetrack** or **Parkour** Category tags. You can also use the **Street Galleries**, the **Pressure Plant Gallery**, or some of the **Shape Galleries** (like the **Primitive Shape Gallery**, **Cube Gallery**, and so on). Use these to build your track layout.

Like the Car Racing Island, this island is built with a racetrack. However, regular vehicles (such as the ones used in the Car Racing Island) are not able to use power-ups. The only vehicle that allows a player to use a power-up while driving on land is the Hoverboard (also known as the **Driftboard Spawner** device), so that's the vehicle used for this race. You can also use powerups with the Surfboard vehicle; see the **Designer Tips** section for ideas on creating a Surfboard Race that takes place on water.

## Create the Island Boundaries

The island you are creating is for a race. You don't want players to drive off the edge of the island by accident. Because the race is outdoors on the island, you need to create a boundary around the race area to prevent players from accidentally falling off the island. You can use **Barrier** and **Damage Volume** devices to create this boundary.

### Place the Barriers

[![An Image of the Barrier Device](https://dev.epicgames.com/community/api/documentation/image/4af23dd0-395c-48c9-917e-8c92850b6c6c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4af23dd0-395c-48c9-917e-8c92850b6c6c?resizing_type=fit)

Follow these steps to place the Barrier devices and customize their options.

When you are positioning the boundary [Barrier](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) devices, you may want to keep the style as Translucent, and set a smaller size. If the Barrier is translucent, you can see what objects and props are being cut off by the Barrier and remove them. The smaller size makes moving the Barrier easier. Once you have it placed properly, you can open the Customize panel again to increase the size and change the style.

### Place the Damage Volumes

[![Image of Damage Volume](https://dev.epicgames.com/community/api/documentation/image/295c785e-fd1c-4f28-a13a-94166d310182?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/295c785e-fd1c-4f28-a13a-94166d310182?resizing_type=fit)

If a player crashes into the nebula Barrier or bounces off, the players will know the island isn't actually floating in space. That would ruin the fun! To prevent this, you can place Damage Volumes which will eliminate the players before they crash into the Barrier. Follow these steps to place and set up the Damage Volumes.

## Build the Starting Grid for Player Spawning

[![Image of Starting Grid](https://dev.epicgames.com/community/api/documentation/image/9ec6b89e-2b8f-4f04-9cd7-25e6f229872b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9ec6b89e-2b8f-4f04-9cd7-25e6f229872b?resizing_type=fit)

### Build the Starting Grid Boxes

You will need to create a starting place where the players and hoverboards will spawn. The race is for 8 players, so use wall and floor pieces to build a line of 4 boxes, with another 4 boxes stacked on top to create a grid of 8 boxes. Each individual box should be large enough to hold a Player Spawn device and a Driftboard Spawner device.

### Add Barrier Devices to Front and Back of Starting Grid

Now you can add Barriers for the front and back. The front Barrier will be transparent, the back Barrier will be black so the players can't see through it.

#### Place the Front Barrier

[![Image of Starting Grid Front Barrier](https://dev.epicgames.com/community/api/documentation/image/4d30e486-2d0b-408b-a7e6-6c3d4bfe7b10?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4d30e486-2d0b-408b-a7e6-6c3d4bfe7b10?resizing_type=fit)

For the front Barrier, modify the following options. Instead of the plain Transparent style, you can choose a red or blue forcefield to make it look interesting (the example uses the Blue Forcefield style). When you have finished customizing the options, click **OK** to save your changes.

[![Starting Grid Front Barrier Options](https://dev.epicgames.com/community/api/documentation/image/6e0c8262-f80b-4a55-969b-fe5f7bdadf95?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6e0c8262-f80b-4a55-969b-fe5f7bdadf95?resizing_type=fit)

*Click image for full size.*

You may want to temporarily move the front Barrier out of the way while placing the Player Spawn Pads and Driftboard Spawners. Once you have those placed, you can reposition the front Barrier.

| Option | Value | Explanation |
| --- | --- | --- |
| **Barrier Style** | Blue Forcefield | The Barrier is translucent (see-through) and looks like a blue forcefield. |
| **Enabled During Phase** | All | The Barrier will be enabled during all [game phases](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#game-phase). |
| **Zone Shape** | Box (Hollow) | Instead of the Barrier being solid, this creates a hollow box. This way the players can spawn inside of it. |
| **Barrier Width** | 4 | The Barrier is 4 tiles wide, to match the width of the starting grid. |
| **Barrier Depth** | 1 | The Barrier is 1 tile deep, so the Barrier zone covers all the boxes and has room for the Player Spawn Pad, the Driftboard Spawner, and the player. |
| **Barrier Height** | 2 | The Barrier is 2 tiles high, to match the height of the starting grid. |
| **Disable When Receiving From** | Channel 150 | When the Barrier receives a signal on Channel 150 from the starting Timed Objective (see below), the Barrier is disabled and the players can move onto the track. |

#### Place the Rear Barrier

[![Image of Starting Grid Rear Barrier](https://dev.epicgames.com/community/api/documentation/image/a5331726-9aef-4caa-8f52-7e8f29c5bdaf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a5331726-9aef-4caa-8f52-7e8f29c5bdaf?resizing_type=fit)

For the rear Barrier, modify the following options. Instead of the style used on the front Barrier, select the Gloss Black style. This will make the back solid and keep the players from seeing what is behind the Starting Grid. When you have finished customizing the options, click **OK** to save your changes.

[![Starting Grid Rear Barrier Options](https://dev.epicgames.com/community/api/documentation/image/8e855a0d-03aa-4ea0-bf12-6a2a74f81c34?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8e855a0d-03aa-4ea0-bf12-6a2a74f81c34?resizing_type=fit)

*Click image for full size.*

| Option | Value | Explanation |
| --- | --- | --- |
| **Barrier Style** | Gloss Black | This style is a solid black color, so the players can't see through it. |
| **Enabled During Phase** | All | The Barrier will be enabled during all Game Phases. |
| **Zone Shape** | Box (Hollow) | Instead of the Barrier being solid, this creates a hollow box. This way the players can spawn inside of it. |
| **Barrier Width** | 4 | The Barrier is 4 tiles wide, to match the width of the starting grid. |
| **Barrier Depth** | .05 | The rear Barrier doesn't need to be as deep, because its main purpose is to block the players' view of what is behind the starting grid. This small depth allows you to place it at the back of the boxes without overlapping the front Barrier. |
| **Barrier Height** | 2 | The Barrier is 2 tiles high, to match the height of the starting grid. |

### Add Player Spawners to Starting Grid Boxes

[![Image of Player Spawn Pads](https://dev.epicgames.com/community/api/documentation/image/127a19bf-1d68-4021-91da-77e934177e01?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/127a19bf-1d68-4021-91da-77e934177e01?resizing_type=fit)

Next, add a Player Spawn Pad to each box in the Starting Grid (8 total). Customize the Player Spawn devices by modifying the options shown below. When you have finished customizing the options, click **OK** to save your changes.

[![Player Spawn Pad Options](https://dev.epicgames.com/community/api/documentation/image/a1824e5f-97f4-4c3c-9473-c58b9e7b7066?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a1824e5f-97f4-4c3c-9473-c58b9e7b7066?resizing_type=fit)

*Click image for full size.*

| Option | Value | Explanation |
| --- | --- | --- |
| **Team** | Teams 1-8 | Assign a Team to each Player Spawn Pad (Team 1, Team 2, and so on to Team 8). |
| **Priority Group** | Primary | This determines the priority of the Spawn Pads, and in what order they will be used. This is the only group of Spawn Pads used during the game, so they are the Primary group. |
| **Use As Island Start** | No | This tutorial includes instructions for building a pre-game lobby, which is where players will spawn into the Island. |
| **Visible During Games** | No | This device must be invisible during the game. |
| **When Player Spawned Transmit On** | Pick a channel | Choose a channel the Player Spawn Pad will transmit on when a player spawns. To make it simple, choose a channel that is the same as the Player Spawn Pad's Team number (Channel 1 for Team 1, and so on). |

### Add the Triggers

[![Image of Trigger Device](https://dev.epicgames.com/community/api/documentation/image/a2ceeb96-99f8-44a9-a608-d303cf2b9c67?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a2ceeb96-99f8-44a9-a608-d303cf2b9c67?resizing_type=fit)

Place 8 Trigger devices behind the Starting Grid. These will be invisible to the players and can be placed anywhere, but placing them behind the Starting Grid is convenient. Customize the Triggers by modifying the options shown below. When you have finished customizing the options, click **OK** to save your changes.

[![Trigger Options](https://dev.epicgames.com/community/api/documentation/image/d737dc64-0bd9-47b3-97a1-751ded216922?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d737dc64-0bd9-47b3-97a1-751ded216922?resizing_type=fit)

*Click image for full size.*

| Option | Value | Explanation |
| --- | --- | --- |
| **Delay** | 1 second | This is the amount of time between the Trigger receiving a signal, and transmitting a signal. |
| **Visible During Game** | No | The device must be invisible during the game. |
| **Trigger When Receiving From** | Pick a channel | Each Trigger is associated with a Player Spawn Pad, so Trigger 1 is for Player Spawn Pad 1, Trigger 2 is for Player Spawn Pad 2, and so on. For this option, select the channel that the paired Player Spawn Pad transmits on when a player spawns. |
| **When Triggered Transmit On** | Pick a channel | Each Trigger is associated with a Player Spawn Pad, so Trigger 1 is for Player Spawn Pad 1, Trigger 2 is for Player Spawn Pad 2, and so on. For this option, select the next channel after the channel selected in the **Trigger When Receiving From** option. So for Trigger 1, it receives on channel 1 and transmits on channel 2. |

### Add Driftboard Spawners to Starting Grid Boxes

[![Image of Driftboard Spawner](https://dev.epicgames.com/community/api/documentation/image/3de168d9-5471-4a32-8b54-968d6c3e331d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3de168d9-5471-4a32-8b54-968d6c3e331d?resizing_type=fit)

Add a Driftboard Spawner device to each box in the Starting Grid (8 total). Customize the Driftboard Spawner devices by modifying the options shown below. When you have finished customizing the options, click **OK** to save your changes.

[![Driftboard Spawner Options](https://dev.epicgames.com/community/api/documentation/image/c5ed72af-82cc-4a74-a5a3-51881f0977aa?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c5ed72af-82cc-4a74-a5a3-51881f0977aa?resizing_type=fit)

*Click image for full size.*

| Option | Value | Explanation |
| --- | --- | --- |
| **Enabled During Phase** | None | The Driftboard will be enabled by a signal, so we don't need to use this setting. |
| **Owning Team** | Teams 1-8 | Assign each Driftboard to the Team number assigned to its matching Player Spawn Pad. For example, if the Player Spawn is assigned Team 1, assign the Driftboard in that box to Team 1 also. |
| **Visible In Game** | Off | Each device has a base, but for the Driftboard (and other vehicles) you don't want the players to see it so this makes it invisible. |
| **Vehicle Health** | Indestructible | This setting makes sure that the vehicle does not get destroyed by damage. Instead, the vehicle will be destroyed when the player is eliminated. This is done using a channel signal. |
| **Assign Driver When Receiving From** | Pick a channel | Each Player Spawn and Driftboard will have a corresponding Tracker device and Trigger device. For this option, select the channel this Driftboard's Trigger is transmitting on. So for Driftboard 1, if Trigger 1 is transmitting on Channel 2, you would set this option to Channel 2. |
| **Destroy Vehicle When Receiving From** | Pick a channel | This option works with the Tracker's **When Complete Transmit On** option. The channel selected for this option must match the channel for the **When Complete Transmit On** option. Each Tracker and Driftboard will have a different channel. For example, for Driftboard 1 and Tracker 1, it is channel 17; for Driftboard 2 and Tracker 2, it is channel 18, and so on. This option makes sure that when the player is eliminated, the Driftboard is also destroyed. They will both respawn together at the Starting Grid. |
| **Enable When Receiving From** | Pick a channel | Each Driftboard Spawner is listening for a signal from its own Player Spawner. For example, when Player Spawner 1 sends a signal on Channel 1, Driftboard 1 receives the signal and is enabled. For this option, pick the channel that this Driftboard's matching Player Spawner transmits on. |
| **When Player Exits Vehicle, Transmit On** | Pick a channel | This option goes with the **Assign Driver When Receiving From** option. When a player tries to get off the Driftboard (exits the vehicle), this option transmits on the channel for the **Assign Driver When Receiving From** option. In our example, if Player 1 tries to get off Driftboard 1, the Driftboard sends a signal on Channel 2, and when Driftboard 1 receives a signal on Channel 2 it assigns the player to itself. This loop keeps players on the Driftboard until the game is finished. |

### Add the Tracker Devices

[![Image of Tracker](https://dev.epicgames.com/community/api/documentation/image/6978deed-284a-4423-9f0c-a49a38c97669?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6978deed-284a-4423-9f0c-a49a38c97669?resizing_type=fit)

The Tracker device tracks whether the player is eliminated, so if the player is eliminated by a damage volume, the Tracker completes and sends a signal to the Driftboard Spawner to destroy the player's driftboard. Then the player will respawn with a new driftboard at the starting area.

Place 8 Tracker devices behind the Starting Grid. These will be invisible to the players and can be placed anywhere, but for convenience you can place them right behind the Starting Grid. Customize the Tracker Devices by modifying the options shown below. When you have finished customizing the options, click **OK** to save your changes.

[![Tracker Device Options](https://dev.epicgames.com/community/api/documentation/image/299f289b-4abe-4693-8e1f-cc3d1a0de51b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/299f289b-4abe-4693-8e1f-cc3d1a0de51b?resizing_type=fit)

*Click image for full size.*

| Option | Value | Explanation |
| --- | --- | --- |
| **Stat to Track** | Eliminations | The trackers are used to track if a player is eliminated. |
| **Target Value** | 1 | This determines the number of eliminations that are required for the Tracker to complete. |
| **Valid Team** | Teams 1-8 | Assign each Tracker the same Team number assigned to its matching Player Spawner. For example, if Player Spawner 1 is assigned Team 1, the Tracker for that Player Spawner is also assigned Team 1. |
| **Assign on Game Start** | No | The device is assigned by a channel signal. |
| **Assign When Joining In Progress** | No | The device is assigned by a channel signal. |
| **Target Team** | Team 1 | This should match the value for the **Valid Team** option. |
| **Show on HUD** | No | The player doesn't need to have this displayed. |
| **Tracker Title** | Eliminated | You can enter any label you want in this field; this is the title used in this example. |
| **Tracker Completion Ceremony** | No | This tracker is working together with other devices, and could complete multiple times. The completion ceremony isn't needed here. |
| **Self-Eliminations Count** | Yes | This is the key setting, as the tracker is being used to determine whether the player was eliminated by the damage volume at the edge of the play area. |
| **Assign When Receiving From** | Pick a channel | This assigns each Tracker to a player. Each Tracker will have a corresponding Player Spawner. For this option, select the channel the matching Player Spawner is transmitting on. For example, if Player Spawner 1 is transmitting on channel 1, you would set this option to channel 1, which then assigns Tracker 1 to Player 1. |
| **Reset Progress When Receiving From** | Pick a channel | This resets the Tracker when its assigned player respawns. For this option, select the channel the matching Player Spawner is transmitting on. |
| **When Complete Transmit On** | Pick a channel | When the Tracker is complete (in other words, when the player assigned this Tracker is eliminated), it transmits a signal on the selected channel. This option works with the Driftboard's **Destroy Vehicle When Receiving From** option. The channel selected for this option must match the channel for the **Destroy Vehicle When Receiving From** option. Each Tracker and Driftboard will have a different channel. For example, Tracker 1 transmits on channel 17 when Player 1 is eliminated by a damage volume; Driftboard 1 receives the signal on Channel 17 and destroys the spawned Driftboard. |

### Add the VFX Spawners

[![Image of VFX Spawner](https://dev.epicgames.com/community/api/documentation/image/af4343dd-f846-4063-925b-dfe38d6dc940?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/af4343dd-f846-4063-925b-dfe38d6dc940?resizing_type=fit)

Place 2 VFX Spawner devices in front of the Starting Grid, one on each side. These devices will shoot fireworks when the race starts. The second Timed Objective will transmit a signal to turn off the fireworks after 10 seconds. Customize the VFX Spawners by modifying the options shown below. When you have finished customizing the options, click OK to save your changes.

[![VFX Spawner Options](https://dev.epicgames.com/community/api/documentation/image/becd2266-a1bc-40bb-a657-1bb51fba24a6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/becd2266-a1bc-40bb-a657-1bb51fba24a6?resizing_type=fit)

*Click image for full size.*

| Option | Value | Explanation |
| --- | --- | --- |
| **Enabled During Phase** | None | The VFX Spawner will be enabled by a signal, so this is set to **None**. |
| **Enable When Receiving From** | Channel 150 | The signal to disable the Barrier transmits on this channel. When the VFX Spawner receives the signal, the device is enabled. When it is enabled, the device will begin looping the default effect, which is Fireworks. |
| **Disable When Receiving From** | Channel 149 | Timed Objective 2 will send a signal on Channel 149 when it completes its countdown. That will disable the VFX Spawner and end the Fireworks effect. |

### Add the Timed Objectives

[![Image of Timed Objective](https://dev.epicgames.com/community/api/documentation/image/959d74cc-4255-4f84-9345-036331a169c2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/959d74cc-4255-4f84-9345-036331a169c2?resizing_type=fit)

Place 2 Timed Objective devices behind the Starting Grid. Like the Tracker devices, these will be invisible to the players. Placing these behind the Starting Grid allows you to modify all of these devices at one time without going all over the island.

#### Timed Objective 1 (Start the Race)

Timed Objective 1 is used to start the race. Customize Timed Objective 1 by modifying the options shown below. When you have finished customizing the options, click **OK** to save your changes.

[![Timed Objective 1 Options](https://dev.epicgames.com/community/api/documentation/image/c5ad4eb1-ee87-4d93-9878-bef679ff4901?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c5ad4eb1-ee87-4d93-9878-bef679ff4901?resizing_type=fit)

*Click image for full size.*

| Option | Value | Explanation |
| --- | --- | --- |
| **Start When Round Starts** | Yes | As soon as the round starts, this timed objective is activated and starts counting. |
| **Time** | 10 seconds | The device counts for 10 seconds, then completes. When the device completes the count, it transmits a signal. |
| **Timer Label Text** | "Race Starts In:" | This displays text the player can see, showing the number of seconds until the game starts. |
| **Hologram Until Activated** | No | The device must be invisible during the game. |
| **Visible During Game** | No | The device must be invisible during the game. |
| **When Completed Transmit On** | Channel 150 | When the timer completes the count, it transmits on Channel 150. The Barrier device in front of the Starting Grid is disabled when it receives a signal on Channel 150. When the Barrier is disabled, the players can move onto the track and start racing. |

#### Timed Objective 2 (End Fireworks)

Timed Objective 2 is used to turn off the fireworks that go off at the start of the race. Customize Timed Objective 2 by modifying the options shown below. When you have finished customizing the options, click **OK** to save your changes.

[![Timed Objective 2 Options](https://dev.epicgames.com/community/api/documentation/image/6f41e211-8867-4f5b-a6b1-1e8b077f79f3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6f41e211-8867-4f5b-a6b1-1e8b077f79f3?resizing_type=fit)

*Click image for full size.*

| Option | Value | Explanation |
| --- | --- | --- |
| **Time** | 10 seconds | This is the amount of time on the countdown timer. |
| **Hologram Until Activated** | No | The device must be invisible during the game. |
| **Visible During Game** | No | The device must be invisible during the game. |
| **Countdown Visible on HUD** | No | The device must be invisible during the game. |
| **Start When Receiving From** | Channel 150 | Timed Objective 1 transmits on this channel when it reaches 0. This device starts counting down when it receives a signal on this channel. |
| **When Completed Transmit On** | Channel 149 | When the device ends its countdown (10 seconds), it transmits a signal to the VFX Spawner device to turn off the fireworks. |

## Add and Set Up Race Checkpoints

[![Image of Race Checkpoints](https://dev.epicgames.com/community/api/documentation/image/95190e17-f514-4625-a56e-3e3e843677bf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/95190e17-f514-4625-a56e-3e3e843677bf?resizing_type=fit)

Add 5 Race Checkpoint devices to your racetrack, as shown in the image. Customize the checkpoints by modifying the options shown below. When you have finished customizing the options, click **OK** to save your changes.

[![Race Checkpoint Options](https://dev.epicgames.com/community/api/documentation/image/4ab9d7b9-16e8-4d0e-97b9-467e440d031e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4ab9d7b9-16e8-4d0e-97b9-467e440d031e?resizing_type=fit)

*Click image for full size.*

| Option | Value | Explanation |
| --- | --- | --- |
| **Checkpoint Number** | Checkpoint 1–5 | Each checkpoint number is incremented when you place them down. Make sure the Checkpoint numbers are in order that you want them to be driven through for the race. |
| **Allow Players to Pass without Vehicle** | No | Even though the devices are set up to keep players on their hoverboards, it's best to set this to No. |
| **Enabled During Phase** | Gameplay Only | The checkpoint appears only when the game starts, not in the pre-game lobby. |
| **When Checkpoint Completed Transmit On** | Channel 25 | Use this channel for scoring. Whenever players pass through the checkpoint, it transmits on this channel and the Score Manager receives the signal and assigns a score. |

## Add and Set Up the Score Manager

[![Image of Score Manager](https://dev.epicgames.com/community/api/documentation/image/0e58c57e-df1a-4cab-b819-a08f2a058104?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0e58c57e-df1a-4cab-b819-a08f2a058104?resizing_type=fit)

Add a Score Manager device. It defaults to being invisible, so you can place it anywhere. But it is more convenient to place it with the other devices behind the Starting Grid. Customize the Score Manager by modifying the options shown below. When you have finished customizing the options, click **OK** to save your changes.

[![Score Manager Options](https://dev.epicgames.com/community/api/documentation/image/4088bcc5-2dbd-427e-b647-0d3d928a1735?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4088bcc5-2dbd-427e-b647-0d3d928a1735?resizing_type=fit)

*Click image for full size.*

| Option | Value | Explanation |
| --- | --- | --- |
| **Score Value** | 1 | This grants 1 score to players as they pass through each checkpoint. |
| **Activate When Receiving From** | Channel 25 | This channel matches the channel the checkpoints transmit on. |

## Add and Set Up the Race Manager

[![Image of Race Manager](https://dev.epicgames.com/community/api/documentation/image/ad368c91-199b-496d-91ce-fbd0244fbca7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ad368c91-199b-496d-91ce-fbd0244fbca7?resizing_type=fit)

Add a Race Manager device. Again, you can place this with the other devices behind the Starting Grid. Customize the Race Manager by modifying the options shown below. When you have finished customizing the options, click **OK** to save your changes.

[![Race Manager Options](https://dev.epicgames.com/community/api/documentation/image/69227663-0dc7-44a9-ad43-7aef69efa1f1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/69227663-0dc7-44a9-ad43-7aef69efa1f1?resizing_type=fit)

*Click image for full size.*

| Option | Value | Explanation |
| --- | --- | --- |
| **Number of Laps** | 4 | Players must complete 4 laps to win the race. |
| **Start Race on Game Start** | No | The race will start under certain conditions, so set this to No. |
| **Start Race When Receiving From Channel** | Channel 149 | The second Timed Objective will transmit on Channel 149 when it completes, and this will start the race. |

## Add and Set Up the Powerups and Special Tiles

There are multiple devices that you need to place on the racetrack. There are special powerup tiles on certain parts of the track, and there are also visual effects (VFX) powerups that grant items to players when driven over.

### Speed Boost Tiles

[![Image of Speed Boost Tile](https://dev.epicgames.com/community/api/documentation/image/db9967d6-ccdc-41c5-85f2-ac6dd1f800e9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/db9967d6-ccdc-41c5-85f2-ac6dd1f800e9?resizing_type=fit)

If you look at the tutorial Island, you'll notice that there are Speed Boost tiles on several parts of the racetrack. You don't have to place them exactly like the track in the example Island. You could place them before a powerup or Bouncer tile, to make it either easier or harder to get that powerup or special tile effect. Or you could place them right before a checkpoint, to help improve the player's overall time.

The Speed Boost tile has one option you can modify. Customize the option as shown below, then click **OK** to save your changes. Remember, you can customize one and then copy-paste as many tiles as you need.

| Option | Value | Explanation |
| --- | --- | --- |
| **Impulse** | High | This setting determines how much the tile boosts the player's speed. Setting this to High is a suggestion; depending on the kind of racetrack you have built and how you want to use the tiles, you can experiment with the values on each tile until you get the effects you want. |

### Bouncer Tiles

[![Image of Bouncer Tile](https://dev.epicgames.com/community/api/documentation/image/b2d3ab5e-6a8c-4792-b61b-cd4c4918aa55?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b2d3ab5e-6a8c-4792-b61b-cd4c4918aa55?resizing_type=fit)

The Bouncer tile causes the player to be launched into the air. It can be placed to either benefit the player, or make the race more challenging. Bouncer tiles are traps, which means you cant customize any options for them.

### Visual Effects Powerup

[![Image of VFX Powerup](https://dev.epicgames.com/community/api/documentation/image/086df948-c6c5-43b4-8e9d-a95382682ba1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/086df948-c6c5-43b4-8e9d-a95382682ba1?resizing_type=fit)

The VFX powerup works together with the Item Granter, to give players certain items when they drive over the VFX powerup. Customize the VFX powerups by modifying the options shown below. When you have finished customizing the options, click **OK** to save your changes. Then place the VFX powerups all over the racetrack, so the players have many opportunities to drive over them.

You can see a video example for how to connect the VFX powerup to the Item Granter below.

You can modify the first powerup, and then copy-paste that one to make a lot more. That way you won't have to customize the options for each one.

[![VFX Powerup Options](https://dev.epicgames.com/community/api/documentation/image/77cd443a-d8c3-4096-964d-e25c07acb655?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/77cd443a-d8c3-4096-964d-e25c07acb655?resizing_type=fit)

*Click image for full size.*

| Option | Value | Explanation |
| --- | --- | --- |
| **Color** | Gold | Sets the color of the glow around the powerup. |
| **Pickup Radius** | .75 | How close the player needs to be to collect the powerup. |
| **Time to Respawn** | 5 seconds | The amount of time it takes for the powerup to respawn after a player collects it. |
| **When Item Picked Up Transmit On** | Channel 26 | When it is picked up, the powerup transmits a signal on this channel. |

### Item Granter

[![Image of Item Granter](https://dev.epicgames.com/community/api/documentation/image/c5dac353-56b6-4bac-8184-c754260ef433?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c5dac353-56b6-4bac-8184-c754260ef433?resizing_type=fit)

The players will get items when they drive over the VFX powerup. These items are actually stored and granted by the Item Granter device. Register the items you want the players to receive by dropping them on the Item Granter. Customize the Item Granter by modifying the options shown below. When you have finished customizing the options, click **OK** to save your changes.

[![Item Granter Options](https://dev.epicgames.com/community/api/documentation/image/76f0265e-9662-421c-8c4a-2d46e646e816?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/76f0265e-9662-421c-8c4a-2d46e646e816?resizing_type=fit)

*Click image for full size.*

| Option | Value | Explanation |
| --- | --- | --- |
| **On-Grant Action** | Keep All | When the device grants an item to a player, everything in the player's inventory will be kept. |
| **Grant Condition** | Only If Space | The device will only grant an item to the player if they have space in their inventory. |
| **Spare Weapon Ammo** | 0 | If the item granted is a weapon, the device will not give the player bonus ammunition. |
| **Cycle Behavior** | Wrap | When the device gets to the end of the list of items registered, it will start over at the beginning of the list and grant that item. |
| **Cycle to Random Item When Receiving From** | Channel 26 | The device randomly chooses a registered item to grant when the device receives a signal on this channel. This is the same channel that the VFX powerup transmits on when the player picks it up. |
| **Restock Items When Receiving From** | Channel 26 | The device restocks all registered items when it receives a signal on this channel. This is the same channel that the VFX powerup transmits on when the player picks it up. |

## Change Island Settings

There are some island-level settings that need to be customized to make this race game work. Press **M** to get to the Island Settings screen. Any setting that is not listed in the sections below should be left at the default value.

### Mode Settings

#### Structure Subcategory

| Option | Value | Explanation |
| --- | --- | --- |
| **Max Players** | 8 | Sets the maximum number of players for the game. The race is set up for 8 players. |
| **Teams** | 8 | Each player is their own team, so there are 8 teams. |
| **Team Size** | 1 | Team size is 1 player. |
| **Matchmaking Type** | Off | Turning this off means each player joining is assigned to any open team. Since Team Size is set to 1, each player is assigned one player to a team. |
| **Total Rounds** | 1 | Right now the game is set to end after a player goes through a certain number of checkpoints and there is only one round. But you can decide how many rounds the game will run. |

#### Game Start Subcategory

| Option | Value | Explanation |
| --- | --- | --- |
| **Autostart** | 30 seconds | This determines whether the game will automatically start after a set amount of time. This only applies to published Islands. |
| **Game Start Countdown** | 5 seconds | When the game starts, players have to wait this amount of time before they can do something. |

#### Spawning Subcategory

| Option | Value | Explanation |
| --- | --- | --- |
| **Join In Progress** | Spectate | You don’t want players joining in the middle of a race, so this makes them a spectator until the next race starts. |

#### Eliminations Subcategory

| Option | Value | Explanation |
| --- | --- | --- |
| **Down But Not Out** | Off | Because this is primarily a racing game and not a typical combat game, Down But Not Out isn’t needed. |
| **Eliminated Player's Items** | Drop | This setting determines what happens to a player’s items when that player is eliminated. Setting it to Drop means eliminated players drop all their items on the ground. |
| **Health Granted on Elimination** | 25 | This sets the amount of health a player receives when eliminating another player. If the amount of health gained goes over the maximum health amount, the excess is applied to the player’s shields. |

#### Scoring Subcategory

| Option | Value | Explanation |
| --- | --- | --- |
| **Vehicle Trick Score Multiplier** | 0.0 | There aren’t any tricks in this game, so this is set to 0. |

#### Victory Condition

| Option | Value | Explanation |
| --- | --- | --- |
| **Game Win Condition** | Most Rounds Wins | The devices end the round when a certain number of checkpoints are passed by a player. Since we have Rounds set to 1, the player that goes through the right number of checkpoints first wins the round, and wins the game. |

### Round Category > Victory Subcategory

| Option | Value | Explanation |
| --- | --- | --- |
| **Round Win Condition** | Score | This setting determines what players need to do to win the game. Setting this to Score means the player with the highest score at the end of the round wins that round and wins the game. This is shown in the first column of the Scoreboard. |
| **Tie Breaker 1** | Time | If two players have the same score at the end of the round, they are tied. This setting determines what will break the tie. Setting it to Time means that when two players are tied, whichever player has the lowest time will win the round and the game. |

### Player Category

#### Locomotion Subcategory

| Option | Value | Explanation |
| --- | --- | --- |
| **Glider Redeploy** | Off | This prevents players from deploying their glider when they are in the air, unless they use an item. |

#### Health Subcategory

| Option | Value | Explanation |
| --- | --- | --- |
| **Starting Health** | 100% | This sets how much health a player has when they spawn on the Island. |
| **Max Health** | 100 | This sets the maximum amount of health the character can gain in the game. |

#### Shields Subcategory

| Option | Value | Explanation |
| --- | --- | --- |
| **Starting Shields** | 100% | This sets the player’s Shield value when they spawn on the Island. |
| **Max Shields** | 50 | This sets the maximum amount of Shield the player can gain in the game. |

#### Pickups Subcategory

| Option | Value | Explanation |
| --- | --- | --- |
| **Allow Item Pick Up** | Yes | This setting allows players to pick up the powerups in the game, as well as picking up any items dropped by eliminated players. |
| **Auto Pickup Pickups** | Yes | Auto Pickup is when players automatically collect items. Players will automatically collect Pickups. |
| **Auto Pickup Ammo** | Yes | Auto Pickup is when players automatically collect items. Players will automatically collect ammo. |
| **Auto Pickup Items** | Yes | Auto Pickup is when players automatically collect items. Players will automatically collect items. |
| **Auto Pickup Gadgets** | Yes | Auto Pickup is when players automatically collect items. Players will automatically collect Gadgets. |
| **Auto Pickup Traps** | No | Building is turned off in this game, so players won’t be able to pickup or place traps. |
| **Auto Pickup Weapons** | Yes | Auto Pickup is when players automatically collect items. Players will automatically collect weapons. |

#### Build Mode Subcategory

| Option | Value | Explanation |
| --- | --- | --- |
| **Allow Building** | None | This racing game doesn’t need players to build, so building is turned off for this game. Choosing None also means players can’t place traps in the game. |

#### Inventory Subcategory

| Option | Value | Explanation |
| --- | --- | --- |
| **Maximum Building Resources** | 0 | Building is not part of the game design for this Island, so players will not be able to collect building resources. |
| **Allow Item Drop** | No | Once a player picks up an item, they can’t drop it from their inventory during the game. |

#### Equipment Subcategory

| Option | Value | Explanation |
| --- | --- | --- |
| **Environment Damage** | Off | Setting this to Off means the players won't be able to damage the environment of the Island. |
| **Structure Damage** | None | Setting this to None means the players aren't able to damage any structures you build on the Island. |
| **Weapon Destruction** | Percentage | This setting modifies how much damage is done to buildings and the environment during games. |
| **Weapon Destruction Percentage** | None | This setting ensures that players' weapons won't destroy the environment or structures on the island. |
| **Pickaxe Destruction** | None | This setting ensures that players can't use their pickaxe to destroy the environment or structures on the island. |
| **Pickaxe Damage** | No Damage | This racing game doesn't include combat, so you can turn off the ability to use a pickaxe to damage another player. |

### World Category > Ambiance Subcategory

| Option | Value | Explanation |
| --- | --- | --- |
| **Time of Day** | Pick a time of day | The example Island is set to 10:00 PM, but you can set this to any time. Setting the time here gives you more control over the lighting in the game. |

### User Interface Category

#### HUD Subcategory

| Option | Value | Explanation |
| --- | --- | --- |
| **HUD Info Type** | Score | This setting determines what information is tracked in the players' HUD. Selecting Score means the HUD will track a player's score. |

#### Scoreboard Subcategory

| Option | Value | Explanation |
| --- | --- | --- |
| **Display Scoreboard** | Yes | When the player presses the **M** key this determines if they will see the Scoreboard. |

## Build the Pre-Game Lobby

All games should have a pre-game lobby, where the players wait until the start of the game. Follow these steps to create a pre-game lobby for your race game.

## Designer Tips

Here are some tips for changing or adding things to your island in order to change how the island plays out, or how to create new games based on this island by changing various devices or settings.

### Create a Surfboard Race

The same steps used to create this Hoverboard island can be used to create a surfboard racing island. The things you need to change are listed below.

Here's a video example of a Surfboard Race.

### Variations for the Hoverboard Race

- Using the lessons learned in this tutorial, you can create other game modes. For example, giving everyone weapons changes the game play, because players will want to go slowly and shoot each other instead of just racing.
- Using additional or different types of traps can change the driving experience for players. Putting traps in strategic locations, such as a speed boost in a tight area, can make the driving experience more challenging.
- You can create Barriers to keep players on a track instead of just on a map. The Barriers can be made invisible or be visible depending on the look the developer is going for.
- You can change the powerups or items granted to players:

  - You can change the Visual Effect powerup to have a longer or shorter delay before it respawns.
  - You can create a combat game mode, and use the Item Granter to grant weapons and ammunition.
  - You can change the Item Granter to grant a set amount of items, grant items in sequence instead of randomly, and even force players to equip an item granted by the Item Granter.
  - You can use the Item Granter to replace the player’s items instead of adding to the player's items.
  - You can set the Item Granter grant items to a team, a class, or to all players. These choices give you the ability to create different types of powerups, which can benefit the players or challenge them.

### Create a Copy of Your Race Island

When you have an Island you like, but want to experiment by adding or changing things, you can make a duplicate of your Island. That way you can experiment and make changes without messing up your current Island.

When you open the console and click **Create New**, the **Game Creation** screen displays. To duplicate your Island, select it in the list and click the **Duplicate** button below the list. A copy of your original Island will appear in the list, and you can set the portal to take you there.

[![image alt text](https://dev.epicgames.com/community/api/documentation/image/0c3dd01f-5ccb-48b7-ac06-1dec394de39b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0c3dd01f-5ccb-48b7-ac06-1dec394de39b?resizing_type=fit)

Once you have experimented and changed things, if you like the new island you can change the name of the island by going to **My Island** and clicking the **Description** tab.
