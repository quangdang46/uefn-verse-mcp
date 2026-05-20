## https://dev.epicgames.com/documentation/en-us/fortnite/design-a-car-racing-game-in-fortnite-creative

# Car Racing Game

Build your own car-racing game, then invite friends and followers to gun it on your island for the win!

![Car Racing Game](https://dev.epicgames.com/community/api/documentation/image/08c3e8f1-d54f-45ef-9130-d88a3e05fa1f?resizing_type=fill&width=1920&height=335)

This [tutorial](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) shows you how to set up a car race that uses checkpoints and a scoring system to determine the winner. It also features some [designer tips](https://dev.epicgames.com/documentation/fortnite/design-a-car-racing-game-in-fortnite-creative) that can improve the overall [gameplay](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary).

The sample island code for this tutorial is **0740-7456-4290**. Head to the **Fortnite lobby** to take a look!

Note the different features of the island, then come back and explore this tutorial to see how you can recreate it on your own island.

## Devices Used

These devices were used for this island tutorial:

- 4 x [Player Spawners](https://dev.epicgames.com/documentation/fortnite/using-player-spawn-pad-devices-in-fortnite-creative)
- 4 x [Pickup Truck Spawners](https://dev.epicgames.com/documentation/fortnite/using-pickup-truck-spawner-devices-in-fortnite-creative)
- 15 x [Race Checkpoints](https://dev.epicgames.com/documentation/fortnite/using-race-checkpoint-devices-in-fortnite-creative)
- 1 x [Score Manager](https://dev.epicgames.com/documentation/fortnite/using-score-manager-devices-in-fortnite-creative)
- ~ x [Barriers](https://dev.epicgames.com/documentation/fortnite/using-barrier-devices-in-fortnite-creative)
- 1 x [Timed Objective](https://dev.epicgames.com/documentation/fortnite/using-timed-objective-devices-in-fortnite-creative)
- 4 x [Triggers](https://dev.epicgames.com/documentation/fortnite/using-trigger-devices-in-fortnite-creative)
- 1 x [Race Manager](https://dev.epicgames.com/documentation/fortnite/using-race-manager-devices-in-fortnite-creative)
- 1 x [End Game Device](https://dev.epicgames.com/documentation/fortnite/using-end-game-devices-in-fortnite-creative)

## Overview of Tutorial Steps

Here's a quick overview of the steps you'll need to recreate this island, in ideal sequence:

1. Create a new island using a [starter island](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary).
2. Add Player Spawners.
3. Add vehicles.
4. Add and set up the Race [Checkpoints](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary).
5. Add and set up the scoring system using the Score Manager.
6. Add barriers at the starting line.
7. Add and set up the Timed Objective devices and triggers to monitor player progress and movement.
8. Add the Race Manager device.
9. Add more barriers to set up boundaries.
10. Adjust the My Island Settings to configure the [pre-game](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) [lobby](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary).

## Create Your Island

Choose Arid Island as your starter island.

If you're placing multiple identical devices, best practice is to place the first device, customize it as needed, then copy and place the additional devices. Even if each device needs further customization, such as setting up a different team number for each, this can still save you time.

## Add Player Spawners

You should now have four spawners. Each pad should have a unique team number, and **When Player Spawned Transmit On** should be set to a unique channel number.

If you're using multiple copies of a device on an island, it can be helpful to [rename](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) them — in this case, based on the team.

## Add Vehicles

While in [Create mode](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary), open the [Quick Menu](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) (on a PC, do this by pressing the **B** key). Locate the **Building as Prop** option, and set it to **Off**. This will cause devices to snap to the grid when you're placing them, and it helps to quickly and accurately position devices.

### Force a Player into the Driver's Seat

Now that the spawners for players and vehicles are set up, it's time to make sure your channel settings are correct. The easiest way to do this is to have the spawn pad transmit a channel number when a player spawns on it at the same time a vehicle has **Assigns Driver When Receiving From**, and on the same channel that was entered on the spawn pad.

You can see the spawn pad and corresponding vehicle spawner, along with their options. Each vehicle and spawn pad should have a matching channel assigned to **When Player Spawned Transmit On** and **Assigns Driver When Receiving From**.

[![matching channels for spawn pad and vehicle](https://dev.epicgames.com/community/api/documentation/image/98c4d445-311a-43e9-98a0-b457af86c694?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/98c4d445-311a-43e9-98a0-b457af86c694?resizing_type=fit)

Check each player and vehicle spawn pad to ensure there's a vehicle for each team and their channel numbers match.

If you ever need to check which channels have been set up and for which devices, press the **Tab** key, then select **My Island** from the top navigation bar.

[![Channel browser button](https://dev.epicgames.com/community/api/documentation/image/ec9c7c29-a865-4f02-8bc9-9bb3d183718b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ec9c7c29-a865-4f02-8bc9-9bb3d183718b?resizing_type=fit)

The **Channel Usage** screen will show which channels are transmitting or receiving, along with the associated devices. You can also use this screen to debug channel behavior.

[![Channel usage screen](https://dev.epicgames.com/community/api/documentation/image/eec7ddd2-f493-4c82-adcc-9e5aecb64f3d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/eec7ddd2-f493-4c82-adcc-9e5aecb64f3d?resizing_type=fit)

### Exit the Vehicle

Next, you'll need a [Trigger](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) device. You'll set this trigger to reassign the player as the driver of their vehicle 5 seconds after they exit the vehicle. You can change the amount of time the player can exit the vehicle, or even force them to never leave the vehicle.

With devices like triggers, or any other devices where players cannot interact with the device directly, it doesn't matter where you place them. Experienced Fortnite developers like to group them together in an out-of-the-way corner for convenience, ease of access, and easy tracking of the devices they've added.

## Set Up Checkpoints

From the Devices tab, add a **Race Checkpoint** device and place it where you want the race to start.

When you place this checkpoint, it is automatically labeled as checkpoint **Number 1**. When you add more checkpoints, you will need to increment the checkpoint numbers by 1 for each additional checkpoint.

It's important to customize **When Checkpoint Completed Transmit On**. This will send a [signal](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) on the channel you select (for this tutorial, Channel 8) whenever a vehicle passes through the checkpoint. The checkpoint will then automatically turn off for that vehicle, and the next checkpoint in the sequence will turn on, as determined by the **Checkpoint Number**. All checkpoints must be on the same channel.

Use these values for the first checkpoint:

[![checkpoint options](https://dev.epicgames.com/community/api/documentation/image/68983d86-5281-4b5e-8c74-844ec8468738?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/68983d86-5281-4b5e-8c74-844ec8468738?resizing_type=fit)

| Option | Value | Explanation |
| --- | --- | --- |
| **Checkpoint Number** | Checkpoint 1 | This number will automatically show for first checkpoint. For each checkpoint you add, increase the number by 1. |
| **Allow Players to Pass without Vehicle** | No | This prevents a player from abandoning a vehicle and finishing the race on foot. |
| **Visible Prior To Race Start** | No | Not making the checkpoints visible prior to race start is used by lots of designers, but you can set this to a different value if you want. |
| **Enabled During Phase** | Gameplay Only | Players must wait until the race starts to pass a checkpoint. |
| **When Checkpoint Completed Transmit On** | Channel 8 | This signal goes to the Score Manager, so only one channel is needed. |

## Add a Scoring System

After you set up each checkpoint to send a signal when a vehicle passes through, set up a **Score Manager** device to count the points. Place the device and set the following options:

[![scoring options](https://dev.epicgames.com/community/api/documentation/image/037270db-8385-4767-99db-c1a5fef32e19?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/037270db-8385-4767-99db-c1a5fef32e19?resizing_type=fit)

| Option | Value | Explanation |
| --- | --- | --- |
| **Score Value** | 1 | Each checkpoint awards 1 score. |
| **Increment Score on Awarding** | Off | You don't need the Score Manager to update the amount of score incrementally. |
| **Activate When Receiving From** | Channel 8 | This must be the same channel the checkpoints transmit on. |

When the Score Manager receives a signal on Channel 8, it will add a **Score Value** for the player passing through the checkpoint.

Since there are 15 checkpoints on the island and each checkpoint awards 1 point, a score of 15 will win the race.

## Add a Win Condition

Now you can set the win condition with a score of 15 winning the round.

You will need to scroll down the Game tab to find all of the options.

## Cover Vehicles with Barriers

Placing **Barrier** devices over the vehicles prevents players from starting the race before the devices are deactivated.

## Set Up the Timed Objective

To start the race, you will set up a **Timed Objective** device. This will give a countdown to the start, then display a HUD message announcing the start of the race.

In-game, once the Barrier devices are disabled, the player can take off down the track and the race is on!

## Add the Race Manager Device

You'll use the Race Manager to set how many laps it takes to finish a race, and set the channel for the Timed Objective device. By default, this device will also add waypoints and show arrows that point to the next checkpoint unless disabled.

[![Race manager options](https://dev.epicgames.com/community/api/documentation/image/b777faa7-0ae9-40ff-bfee-5937154feb79?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b777faa7-0ae9-40ff-bfee-5937154feb79?resizing_type=fit)

| Option | Value | Explanation |
| --- | --- | --- |
| **Number of Laps** | 1 | One lap is the default. If you change this to more than one, you will need to modify the score on **My Island > Game > Score To End** to match the score now possible. For example, if you want the race to go for 2 rounds, this would require 30 score to win. |
| **Start Race on Game Start** | No | The race will start when a signal is received. |
| **Start Race When Receiving From Channel** | Channel 7 | This signal will come from the Timed Objective device. |

## Define Boundries with Barriers

You can add barriers to prevent players from driving off the island. It's a good idea to place barriers in any spot where a player might do this, as shown in the example below, and you can also place them in strategic spots to keep the vehicles from leaving the racetrack.

[![barrier placement example](https://dev.epicgames.com/community/api/documentation/image/aaa15386-3d3c-4aff-a146-694e6ccb69ab?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/aaa15386-3d3c-4aff-a146-694e6ccb69ab?resizing_type=fit)

## Add a Pre-Game Lobby

Adding a **pre-game lobby** gives players a place to wait until the race starts.

This is where the players will enter your island, so you will need four spawn pads to accommodate up to four players.

You can add some fun things for players to do while waiting in the lobby, such as providing [Driftboards](https://dev.epicgames.com/documentation/fortnite/using-driftboard-spawner-devices-in-fortnite-creative) or [Baller vehicles](https://dev.epicgames.com/documentation/fortnite/using-baller-spawner-devices-in-fortnite-creative)that are available only during pre-game. You can set this by customizing the **Enabled During Phase** option to **PreGame Only** for that vehicle spawner device.

[![enabled during phase option changes](https://dev.epicgames.com/community/api/documentation/image/6c9498fb-7062-4a8e-84cb-cf9a04e82657?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6c9498fb-7062-4a8e-84cb-cf9a04e82657?resizing_type=fit)

[![pre-game lobby example](https://dev.epicgames.com/community/api/documentation/image/aa8e0d33-f515-43a4-b73e-30aadec8df9c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/aa8e0d33-f515-43a4-b73e-30aadec8df9c?resizing_type=fit)

*What the pre-game lobby for this island looks like.*

Depending on how you set up your island, you might also want to add barriers around the lobby area to prevent vehicles from getting into the pre-game lobby. In the Barrier device options, set **Enabled During Phase** to **Gameplay Only**.

[![lobby barrier custom options](https://dev.epicgames.com/community/api/documentation/image/cc6a7551-fab5-469c-89da-29f0dea9040b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cc6a7551-fab5-469c-89da-29f0dea9040b?resizing_type=fit)

### Modify More My Island Settings

The final step for setting up your pre-game lobby is to return to **Island Settings > Game** and do some final changes.

You will need to scroll down this tab to find all of the options.

| Option | Value | Explanation |
| --- | --- | --- |
| **Spawn Location** | Spawn Pads | This sends the players directly to their spawn pads in the pre-game lobby instead of having them fall from the sky. |
| **Post-Game Spawn Location** | Island Start | This sends the players back to the lobby at end of game. |
| **Autostart** | 60 Seconds | After 60 seconds, the race will automatically start again. Note that this only works for published islands. |
| **Game Start Countdown** | 10 Seconds | This controls how long the pre-game lobby stays open before the game begins. |
| **Vehicle Trick Score Multiplier** | 0.0 | Set this to 0.0 as this feature isn't used in this tutorial. |

## Designer Tips

Here are some tips that can improve how your island plays.

### Modifying Vehicles

There are lots of customization options available for the vehicles, and here are some that can influence gameplay.

| Option | Explanation |
| --- | --- |
| **Boost Regen** | One of the easiest ways to modify a vehicle is to adjust the Boost Regen, which controls how quickly a [boost](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) meter fills, or [regenerates](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary). Options Include No boost, Slow, Default, Fast, and Unlimited. Changing this parameter has the biggest effect on vehicle performance. |
| **Tire Selection** | There are road tires and off-road tires. The tires you select will influence how the vehicle handles. |

### Adding Traps (Boosters)

Another good way to spice up your island is to use [trap](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) devices such as the Speed Boost or [Bouncer](https://dev.epicgames.com/documentation/fortnite/using-bouncer-gallery-devices-in-fortnite-creative). Putting these traps in key locations can make your races even more challenging.

Check out this video to see some samples of how a vehicle could be affected by a trap device.

### Invisible Barriers

There may be cases where you want to block off certain parts of the island with invisible barriers like out-of-bounds areas, or to make small walls impregnable. The barrier device is perfect for these scenarios.

## Video Tutorial
