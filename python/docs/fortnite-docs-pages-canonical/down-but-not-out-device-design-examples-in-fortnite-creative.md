## https://dev.epicgames.com/documentation/en-us/fortnite/down-but-not-out-device-design-examples-in-fortnite-creative

# Down But Not Out Device Design Example

Learn how to build a cooperative mountain-climbing game where players rely on each other to overcome dangers and reach the summit!

![Down But Not Out Device Design Example](https://dev.epicgames.com/community/api/documentation/image/bc48fd2e-b443-4233-b6d0-28ad0fd22257?resizing_type=fill&width=1920&height=335)

The **Down But Not Out** device can save players from elimination. Even if a player loses all their health, another player can swoop in and revive them before it’s too late!

In this example, the objective is to occupy the capture area at the mountain's summit for a specified time to win the game, with players working cooperatively to achieve the objective.

This device is an excellent choice for team vs. team games, allowing players to rescue teammates in danger. You will learn how to build a cooperative mountain-climbing game where players have to rely on each other to overcome the dangers of the mountain and reach the summit!

## Devices Used

- 2 x [Player Spawner](https://dev.epicgames.com/documentation/fortnite/using-player-spawn-pad-devices-in-fortnite-creative) devices (for two players)
- 1 x [Physics Boulder](https://dev.epicgames.com/documentation/fortnite/using-physics-boulder-devices-in-fortnite-creative) device
- 1 x [VFX Creator](using-vfx-creator-devices-in-fortnite-creative) device
- 1 x [Audio Player](using-speaker-devices-in-fortnite-creative) device
- 1 x [Volume](https://dev.epicgames.com/documentation/fortnite/using-volume-devices-in-fortnite-creative) device
- 1 x [Damage Volume](using-damage-volume-devices-in-fortnite-creative) device
- 1 x [Capture Area](using-capture-area-devices-in-fortnite-creative) device
- 1 x [Down But Not Out](using-down-but-not-out-devices-in-fortnite-creative) device

For devices that you'll place more than once, you can save time if you place and customize the first one, then copy and place as needed!

## Build Your Own

For this example, you will configure the island settings, build your mountain, and add and modify devices.

Place at least one **Player Spawner** device on your island first to avoid having to fall into the island each time you access it!

## Configure the Island Settings

Since this game is about climbing, you'll want to make sure that the players move in ways that support that gameplay.

You will be making more changes to island settings at the end of this example, but you'll circle back later!

## Build the Mountain

There are a number of [galleries](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#gallery) with big pieces of rock that make a great starting point for your mountain-climbing game. This design example uses terrain pieces from the **Modular Mountain Gallery Temperate Buildable** and Mod**ular Rock Gallery Temperate A** galleries, but feel free to select from other galleries as well.

For more on galleries, see [Using Prefabs and Galleries](https://dev.epicgames.com/documentation/fortnite/using-prefabs-and-galleries-in-fortnite-creative).

[![island settings](https://dev.epicgames.com/community/api/documentation/image/ce1500e4-0838-4a77-b8b3-203ff996e4ce?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ce1500e4-0838-4a77-b8b3-203ff996e4ce?resizing_type=fit)

### Build the Mountain Base

### Add Ledges for Climbing

The bottom rocks provide the base for your mini-game, but you should continue to pile on more to ensure that players can scale from the bottom to the peak.

Using rocks as ledges also lets the player take advantage of movements like mantling.

[![build ledges](https://dev.epicgames.com/community/api/documentation/image/706c8e96-7090-482a-b2c4-7d8236d69a22?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/706c8e96-7090-482a-b2c4-7d8236d69a22?resizing_type=fit)

Explore the galleries and you’ll find all sorts of interesting shapes for players to climb over.

If you need to scale or rotate the rocks, make sure the **Quick Menu** (**Tab > Quick Menu**) **Collision** setting is on **Terrain**.

[![Quick Menu](https://dev.epicgames.com/community/api/documentation/image/787a3580-4e80-47d5-8f81-566ed4b01383?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/787a3580-4e80-47d5-8f81-566ed4b01383?resizing_type=fit)

This lets you push the ledge rocks into the base mountain to create an upward path.

Be sure to test the path that you build — if *you* can’t climb from ground to peak, it's likely no one else can either!

## Add Some Danger!

On the mountain, players have to watch out for dangerous boulders rolling down from above. You'll use devices to help players identify dangerous areas with showers of falling rocks and a rumbling sound when they enter into an area where a boulder can fall.

### Place a Physics Boulder Device

To find this device, use the search box, or look at the **Environment** subcategory under **Devices**.

[![Find Physics Boulder device](https://dev.epicgames.com/community/api/documentation/image/70f72f92-3ea4-4e9f-b76c-f8bcdcab7609?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/70f72f92-3ea4-4e9f-b76c-f8bcdcab7609?resizing_type=fit)

The search box is an easy way to find any device if you know the device name! Just make sure you don't have any subcategories checked that could filter out that device.

### Place a VFX Creator Device

You will use this device to create a visual effect for falling rocks.

### Place an Audio Player Device

Not every spot on the mountain is safe, and rolling boulders are a constant danger. You'll use an audio player to play a dramatic sound effect that will help warn players that a huge rock is about to tumble down on their heads!

### Place a Volume Device

The boulders are only released when players enter certain areas. You’ll use a **Volume** device to bind the other devices and create the hazards climbers will encounter when climbing your mountain.

This leaves only the Player Events Enabled, which means that when a player enters or leaves this volume, bound devices will be triggered.

## Bind the Devices

**Direct event binding** is how devices communicate with each other. There are several bindings you'll need to set up for the game mechanics to work correctly.

You will bind the Physics Boulder, VFX Creator and the Audio Player to the Volume device to activate all of them when a player enters volume, and to send the boulder rolling down the side of the mountain when they exit the volume!

All of this binding can be done from the Volume device.

These settings result in a warning of eminent rock fall to a player when they enter the volume, followed by an actual falling boulder when the player moves out of the volume.

## Position the Obstacles on Your Mountain

Now that you've configured the first four devices, it's time to get them ready to do their dangerous magic.

## Set the Win Condition Devices

Some mountain peaks rise so high that breathing becomes difficult when a climber scales them. Mountain climbers call this region the **death zone**. The remaining devices will set up the game mechanics for your mountain's death zone.

### Place a Damage Volume Device

The last three settings leave only players losing health from this damage volume.

### Place a Capture Area Device

You will add a **Capture Area** device to your mountain that covers the summit area. This defines the peak of the mountain as the objective for your players to climb to.

### Place a Down But Not Out Device

The final device here is **Down But Not Out**. With this, players can rescue each other from the dangers of the climb so they can all reach the summit together!

## Complete Island Settings Configurations

The final step is to configure the Mode and Round settings in your Island Settings.

And there you have it — a cooperative mountain climbing adventure!

## Design Tip

Explore adding other devices to create even more obstacles on your mountain!
