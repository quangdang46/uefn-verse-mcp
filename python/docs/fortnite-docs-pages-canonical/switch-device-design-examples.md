## https://dev.epicgames.com/documentation/en-us/fortnite/switch-device-design-examples

# Switch Device Design Examples

Explore ways to switch up your games with switches!

![Switch Device Design Examples](https://dev.epicgames.com/community/api/documentation/image/0f0979f9-b11a-4b02-b669-11f79c9abc9c?resizing_type=fill&width=1920&height=335)

###### Prerequisite topics

In order to understand and use the content on this page, make sure you are familiar with the following topics:

- [Switch Devices](https://dev.epicgames.com/documentation/fortnite/using-switch-devices-in-fortnite-creative)

Switch devices can be operated by users to turn devices on or off, or as a game mechanic to start or stop other devices.

[![](https://dev.epicgames.com/community/api/documentation/image/a7c90ffd-b162-4a5c-a4e7-c22a47992951?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a7c90ffd-b162-4a5c-a4e7-c22a47992951?resizing_type=fit)

## Simple Light Switch Mechanic

One basic use of the Switch device is as a light switch as it can be easily configured to turn other devices on and off.

### Devices Used

- 1 x [Player Spawner](https://dev.epicgames.com/documentation/fortnite/using-player-spawn-pad-devices-in-fortnite-creative) device
- 2 x [Customizable Light (Torch)](https://dev.epicgames.com/documentation/fortnite/using-customizable-light-devices-in-fortnite-creative) devices
- 1 x [Switch](https://dev.epicgames.com/documentation/fortnite/using-switch-devices-in-fortnite-creative) device

### Set Up the Devices

### Bind Functions and Events

[Direct event binding](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#directeventbinding) is how you set devices to communicate directly with other devices. This involves setting [functions](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#function) and [events](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#event) for the devices involved.

You now have the basic functionality for players interacting with lights using the Switch device!

### Design Tip

You can connect a switch to any device. These are  useful in turning different devices on and off! A switch can be easily used to open and close a door remotely, trigger the movement of a prop, or enable or disable a vehicle.

## Build a Persistent Tutorial Manager

The Switch device can be configured to save its state between playthroughs, allowing for very basic and straightforward data saving.

In this example, you will use a switch to create a system that automatically skips a tutorial if the player has completed it before.

### Devices Used

- 1 x Switch device
- 1 x Player Spawner device
- 1 x [Item Granter](https://dev.epicgames.com/documentation/fortnite/using-item-granter-devices-in-fortnite-creative) device
- 1 x [Creature Spawner](https://dev.epicgames.com/documentation/fortnite/using-creature-spawner-devices-in-fortnite-creative) device
- 2 x [Player Checkpoint](https://dev.epicgames.com/documentation/fortnite/using-player-checkpoint-devices-in-fortnite-creative) devices
- 2 x [Teleporter](https://dev.epicgames.com/documentation/fortnite/using-teleporter-devices-in-fortnite-creative) devices
- 1 x [Trigger](https://dev.epicgames.com/documentation/fortnite/using-trigger-devices-in-fortnite-creative) device

### Set Up the Basic Gameplay

You’ll begin by setting up the basic play area and gameplay functionality.

### Configure the Different Start Points

You’ll now use the **Teleporter** and **Player Checkpoint** devices to configure starting locations for the tutorial and gameplay segments.

### Set Up the Persistent Switch

Now, set up a switch to keep track of whether the player has completed the tutorial, and to save the data.

### Bind Functions and Events

The next step is to bind the functions and events.

You now have the basic functionality for a system that uses a switch to track whether a player has completed a tutorial!

### Design Tip

This example showcases a Persistent Tutorial Manager in a single-player context, but the persistence functionality on the switch can easily be used for multiplayer games as well.

For each player to have their own unique switch, make sure the **Store State Per Player** setting is on **Yes**. This would be great in Islands where different players can enter the game at different times, making sure that each is able to interact with the tutorial on their own.

## Build a King-of-the-Hill Game!

The Switch device can be used as an interactable objective in a two-player King-of-the-Hill game!

In this example, you will use a Switch device to represent which player is in control of the hill. If **On**, the Blue Team is in control. If **Off**, the Red Team is in control.

### Devices Used

- 1 x Switch device
- 2 x Player Spawner devices
- 2 x Team Settings & Inventory devices
- 2 x [End Game](https://dev.epicgames.com/documentation/fortnite/using-end-game-devices-in-fortnite-creative) devices
- 3 x [Timer](https://dev.epicgames.com/documentation/fortnite/using-timer-devices-in-fortnite-creative) devices
- 16 x [Customizable Light](https://dev.epicgames.com/documentation/fortnite/using-customizable-light-devices-in-fortnite-creative) (Spotlight) devices
- 6 x [VFX Spawner](https://dev.epicgames.com/documentation/fortnite/using-vfx-spawner-devices-in-fortnite-creative) devices
- 2 x [Skydome](https://dev.epicgames.com/documentation/fortnite/using-skydome-devices-in-fortnite-creative) devices
- 2 x [Channel](https://dev.epicgames.com/documentation/fortnite/using-channel-devices-in-fortnite-creative) devices

### Set Up the Play Area and Basic Devices

### Configure the Two Teams

### Set Up the VFX

### Bind Functions and Events

You now have a fully functioning King-of-the-Hill game!

### Design Tip

This example is configured for just two players, but you could add more player spawners to accomodate a larger battle.

When adding more players, make sure the play space is large enough to accommodate many interactions at once, and tune the amount of time it takes players to respawn to keep the gameplay engaging!
