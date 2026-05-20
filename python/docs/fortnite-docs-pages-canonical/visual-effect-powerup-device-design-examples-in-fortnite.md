## https://dev.epicgames.com/documentation/en-us/fortnite/visual-effect-powerup-device-design-examples-in-fortnite

# Visual Effect Powerup Device Design Examples

Let players know when they've accomplished something cool with a visual effect!

![Visual Effect Powerup Device Design Examples](https://dev.epicgames.com/community/api/documentation/image/647d8285-a996-47c0-8412-d43bf907d501?resizing_type=fill&width=1920&height=335)

###### Prerequisite topics

In order to understand and use the content on this page, make sure you are familiar with the following topics:

- [Visual Effect Powerup Devices](https://dev.epicgames.com/documentation/fortnite/using-visual-effect-powerup-devices-in-fortnite-creative)

You can set a **Visual Effect Powerup** device to validate player behavior with a visual effect, such as when the player picks up an item or reaches a destination. Use this device to reinforce in-game information, communicate the importance of an event, or make characters sparkle just for fun!

## Basic Setup

Think of the [Visual Effect Powerup](https://dev.epicgames.com/documentation/fortnite/using-visual-effect-powerup-devices-in-fortnite-creative) device as the location where you set up the details of the effect that you want to play on characters in-game. Like other devices that players never need to see or interact with, it should be placed somewhere convenient for the island creator to access and change, but it does not need to be in the playable area of your island.

[![](https://dev.epicgames.com/community/api/documentation/image/95964ccc-0bce-4366-9e20-bfc442d48ca5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/95964ccc-0bce-4366-9e20-bfc442d48ca5?resizing_type=fit)

### Devices Used

- 1 x [Visual Effect Powerup](https://dev.epicgames.com/documentation/fortnite/using-visual-effect-powerup-devices-in-fortnite-creative) device
- 1 x [Health Powerup](https://dev.epicgames.com/documentation/fortnite/using-health-powerup-devices-in-fortnite-creative) device

### Overview

### Place and Customize Devices

### Set the Functions for the Devices

### Design Tip

Choose the colors and visual effects you like for the powerups!

## Combine Powerups for Visual Effects

Using techniques from the [basic setup](https://dev.epicgames.com/documentation/fortnite/visual-effect-powerup-device-design-examples-in-fortnite#basic-setup) above, you can add visual effects to other powerup devices.

This example is a good follow to the previous example.

[![](https://dev.epicgames.com/community/api/documentation/image/cc6be776-3b32-4239-984d-9ae3cb66e30d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cc6be776-3b32-4239-984d-9ae3cb66e30d?resizing_type=fit)

Devices Used

- 1 x [Damage Amplifier Powerup](https://dev.epicgames.com/documentation/fortnite/using-damage-amplifier-powerup-devices-in-fortnite-creative) device
- 1 x [Stat Powerup](https://dev.epicgames.com/documentation/fortnite/using-stat-powerup-devices-in-fortnite-creative) device
- 1 x [Grind Powerup](https://dev.epicgames.com/documentation/fortnite/grind-powerup-devices) device
- 3 x Visual Effects Powerup devices

### Overview

[![](https://dev.epicgames.com/community/api/documentation/image/a1c91c72-d0de-4e84-94e9-622e6d53aba3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a1c91c72-d0de-4e84-94e9-622e6d53aba3?resizing_type=fit)

### Place the Devices

1. Place a **Damage Amplifier Powerup** device, a **Stat Powerup** device, and a **Grind Powerup** device in a convenient location.
2. Place a **Visual Effect Powerup** device near each one.

   Place these devices near the powerups in step 1 for convenience.
3. Configure settings for the Visual Effect Powerup device that you will connect to the **Damage Amplifier** ****P**owerup**:

   [![](https://dev.epicgames.com/community/api/documentation/image/4ed9d519-9a9c-405c-9692-54c79c2c64c5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4ed9d519-9a9c-405c-9692-54c79c2c64c5?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Visual Effect | GLOW |
   | Color Type | DIRECT COLOR |
   | Custom Color | #FF00E2 |
4. Configure the functions:

   [![](https://dev.epicgames.com/community/api/documentation/image/d4174db1-3ac1-44f8-b13f-fde4267984e5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d4174db1-3ac1-44f8-b13f-fde4267984e5?resizing_type=fit)

   | Function | Select Device | Select Event |
   | --- | --- | --- |
   | Pickup When Receiving From | Damage Amplifier Pickup | On Item Picked Up |
5. Configure the **Visual Effect Powerup** device that you will connect to the **Stat Powerup**:

   [![](https://dev.epicgames.com/community/api/documentation/image/8f734a3c-421a-40bb-b8e7-09a9e23aa52f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8f734a3c-421a-40bb-b8e7-09a9e23aa52f?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Effect Duration | 15 SECONDS |
   | Visual Effect | OUTLINE |
   | Color Type | DIRECT COLOR |
   | Custom Color | #FFF000 |
6. Configure the functions:

   [![](https://dev.epicgames.com/community/api/documentation/image/66951003-4686-42b9-9ff9-1c7052e594a9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/66951003-4686-42b9-9ff9-1c7052e594a9?resizing_type=fit)

   | Function | Select Event |  |
   | --- | --- | --- |
   | Pickup When Receiving From | Stat Powerup | On Item Picked Up |
7. Configure the **Grind Powerup** device:

   [![](https://dev.epicgames.com/community/api/documentation/image/41515619-445c-4318-93ff-d1f5d00ae7f4?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/41515619-445c-4318-93ff-d1f5d00ae7f4?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Respawn | YES |
   | Effect Duration | 20 SECONDS |
8. Configure the **Visual Effect Powerup** device:

   [![](https://dev.epicgames.com/community/api/documentation/image/0a123bf7-ba6c-499a-9ace-84369e0fcfc0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0a123bf7-ba6c-499a-9ace-84369e0fcfc0?resizing_type=fit)

   | Option |  |
   | --- | --- |
   | Effect Duration | 15 SECONDS |
   | Visual Effect | SPARK AURA |
   | Color Type | DIRECT COLOR |
   | Custom Color | #3500FF |
9. Configure the **Visual Effect Powerup** device functions:

   [![](https://dev.epicgames.com/community/api/documentation/image/c3405c26-9241-4a82-9799-7cd8609576fc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c3405c26-9241-4a82-9799-7cd8609576fc?resizing_type=fit)

   | Function | Select Device | Select Event |
   | --- | --- | --- |
   | Pickup When Receiving From | Grind Powerup | On Item Picked Up |

### Design Tip

Now you have set up distinctive visual effects for every powerup on your island!

Try experimenting with the duration of the powerups and the visual effects.

## Create a More Complex Setup

[![](https://dev.epicgames.com/community/api/documentation/image/a3ec199f-f85a-465a-a023-6be26418b084?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a3ec199f-f85a-465a-a023-6be26418b084?resizing_type=fit)

Let’s create a wild free-for-all battle game mode for up to 8 players!

### Devices Used

- 10 x Item Spawner devices
- 8 x Player Spawner devices
- 2 x [Cannon Spawner](https://dev.epicgames.com/documentation/fortnite/using-cannon-spawner-devices-in-fortnite-creative) devices
- 2 x [Siege Cannon Spawner](https://dev.epicgames.com/documentation/fortnite/using-siege-cannon-devices-in-fortnite-creative) devices
- 1 x [Boat Spawner](https://dev.epicgames.com/documentation/fortnite/using-boat-spawner-devices-in-fortnite-creative) device
- 1 x [Helicopter Spawner](https://dev.epicgames.com/documentation/fortnite/using-helicopter-spawner-devices-in-fortnite-creative) device
- 2 x [Surfboard Spawner](https://dev.epicgames.com/documentation/fortnite/using-surfboard-spawner-devices-in-fortnite-creative) devices
- 12 x Visual Effect Powerup  devices
- 1 x [Barrier](https://dev.epicgames.com/documentation/fortnite/using-barrier-devices-in-fortnite-creative) device

### Overview

1. Make a ship-themed battle arena.
2. Customize the Visual Effect Powerup devices and powerups.
3. Place the Player Spawners.
4. Place the Vehicle Spawners.
5. Place the Item Spawners.
6. Place the powerups.
7. Configure the game mode.

### Make a Ship-Themed Battle Arena

[![](https://dev.epicgames.com/community/api/documentation/image/22be880f-b470-4006-98d7-6cafdd6c839e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/22be880f-b470-4006-98d7-6cafdd6c839e?resizing_type=fit)

Oasis Island features a tiny island with a handy beached boat. That island makes a good mid-point for our ship-to-ship island battle!

### Customize the Visual Effect Powerup Devices for All Four Powerups

This step is the same as [Basic Setup](https://dev.epicgames.com/documentation/fortnite/visual-effect-powerup-device-design-examples-in-fortnite#basic-setup) and [Combine Powerups for Visual Effects](https://dev.epicgames.com/documentation/fortnite/visual-effect-powerup-device-design-examples-in-fortnite#combine-powerups-for-visual-effects), so repeat those steps here. 

[![](https://dev.epicgames.com/community/api/documentation/image/90e351a9-dc13-4f07-827e-6ab7529609f2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/90e351a9-dc13-4f07-827e-6ab7529609f2?resizing_type=fit)

### Place the Player Spawners

Place five player spawners on the Megalodon ship and three more spawners on the pirate ship.

[![](https://dev.epicgames.com/community/api/documentation/image/7149b261-0a91-4b89-9c92-64166d0dea7b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7149b261-0a91-4b89-9c92-64166d0dea7b?resizing_type=fit)

Pick whatever starting locations seem fun to you!

[![](https://dev.epicgames.com/community/api/documentation/image/4bf042a6-ccd9-4203-a295-ead14aef159b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4bf042a6-ccd9-4203-a295-ead14aef159b?resizing_type=fit)

[![](https://dev.epicgames.com/community/api/documentation/image/e1d5684a-c9ab-489d-b4f6-f13736e6bff5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e1d5684a-c9ab-489d-b4f6-f13736e6bff5?resizing_type=fit)

### Place the Vehicle Spawners

This play space is so big that it’s perfect for using vehicles to add to the fun!

### Load and Place the Item Spawners

### Place the Powerups in the Play Area

Copy and place the various powerup spawners where you think players would have the most fun finding and using:

[![](https://dev.epicgames.com/community/api/documentation/image/3995b014-91e1-41b9-ada5-09881b3e9d3f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3995b014-91e1-41b9-ada5-09881b3e9d3f?resizing_type=fit)

[![](https://dev.epicgames.com/community/api/documentation/image/a21dfc8b-6fef-4994-968b-a06cd3439e80?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a21dfc8b-6fef-4994-968b-a06cd3439e80?resizing_type=fit)

[![](https://dev.epicgames.com/community/api/documentation/image/dada1fc9-a2ba-448a-8e77-748afa2a61e3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dada1fc9-a2ba-448a-8e77-748afa2a61e3?resizing_type=fit)

[![](https://dev.epicgames.com/community/api/documentation/image/f78ea43f-2f61-47a5-8c58-a0d6e9eb8e1a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f78ea43f-2f61-47a5-8c58-a0d6e9eb8e1a?resizing_type=fit)

[![](https://dev.epicgames.com/community/api/documentation/image/6b39db7e-b662-4008-a3e6-79e671bdafdf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6b39db7e-b662-4008-a3e6-79e671bdafdf?resizing_type=fit)

[![](https://dev.epicgames.com/community/api/documentation/image/82329d30-1c79-4ae6-a3c4-275ae4ab4772?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/82329d30-1c79-4ae6-a3c4-275ae4ab4772?resizing_type=fit)

[![](https://dev.epicgames.com/community/api/documentation/image/220e4a73-2e1b-45b7-9e2f-1a162bc8943a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/220e4a73-2e1b-45b7-9e2f-1a162bc8943a?resizing_type=fit)

### Configure the Game Mode Using the Island Settings

### Add a Barrier Device to Constrain the Action

To help ensure that players don’t wander too far away from the fun, add a barrier device just under Oasis Island in the center of the map:

[![](https://dev.epicgames.com/community/api/documentation/image/1ad51eb7-5cc6-49ab-a292-906e653e39b6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1ad51eb7-5cc6-49ab-a292-906e653e39b6?resizing_type=fit)

Use the following settings on the device:

[![](https://dev.epicgames.com/community/api/documentation/image/c5d8b2ec-0174-4930-9f12-3ae485a5bcdd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c5d8b2ec-0174-4930-9f12-3ae485a5bcdd?resizing_type=fit)

| Option | Value |
| --- | --- |
| Barrier Material | Translucent (only visible when near) |
| Zone Shape | Hollow Box |
| Barrier Depth | 60.0 Tiles |
| Barrier Width | 60.0 Tiles |
| Barrier Height | 30 Tiles |
| Collide With Camera | Off |

### Design Tip

And there you have it — a unique, playable, free-for-all fight for up to eight players!

Try adjusting the placement of the powerups, vehicles, even the weapons — inside of the Item Spawners to create unique experiences.
