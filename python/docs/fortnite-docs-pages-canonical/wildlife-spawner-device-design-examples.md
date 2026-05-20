## https://dev.epicgames.com/documentation/en-us/fortnite/wildlife-spawner-device-design-examples

# Wildlife Spawner Device Design Examples

Find new ways to integrate various types of wildlife into your game play, from chasing chickens to riding raptors!

![Wildlife Spawner Device Design Examples](https://dev.epicgames.com/community/api/documentation/image/1f9b9e94-0a70-4dda-9d94-a981caa72611?resizing_type=fill&width=1920&height=335)

Wildlife spawners can spawn an array of creatures, some of which you can hunt, tame, or ride! You're about to learn some fun ways to integrate a few of these creatures into your own gameplay design.

## Basic Animal Hazard

In this example, you'll see how to use a **Wildlife Spawner** device to configure animals that are hazardous for players!

### Devices Used

- 1 x [Wildlife Spawner](https://dev.epicgames.com/documentation/fortnite/using-wildlife-spawner-devices-in-fortnite-creative) device
- 1 x [Player Spawner](https://dev.epicgames.com/documentation/fortnite/using-player-spawn-pad-devices-in-fortnite-creative) device
- 1 x [Item Granter](https://dev.epicgames.com/documentation/fortnite/using-item-granter-devices-in-fortnite-creative) device

### Set Up the Devices

You now have the basic functionality for an animal hazard!

### Design Tip

Consider which animals make the most sense to be spawning in your Island — it might not make sense to spawn a wolf on a desert island, for instance.

To make the wildlife blend in more with your environment, explore the biome variants on chickens, boars, and wolves!

## Timed Chicken Capture

The Wildlife Spawner can spawn chickens. Fortnite chickens can be picked up, jumped with, and thrown by the player! This makes them a fun option for a timed capture challenge.

### Devices Used

- 1 x Wildlife Spawner device
- 1 x Player Spawner device
- 1 x [Volume](https://dev.epicgames.com/documentation/fortnite/using-volume-devices-in-fortnite-creative) device
- 1 x [Timer](https://dev.epicgames.com/documentation/fortnite/using-timer-devices-in-fortnite-creative) device

### Set Up the Devices

1. Create a small pen for the captured chickens to go in using fence assets from the **Farm Building** gallery.
2. Place a **Player Spawner** device.
3. Place a **Wildlife Spawner** device.
4. Customize the Wildlife Spawner to use a chicken as the [spawn](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#spawn) type:

   [![](https://dev.epicgames.com/community/api/documentation/image/160c01aa-5b7e-4a8c-a3c1-71d1b65e15db?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/160c01aa-5b7e-4a8c-a3c1-71d1b65e15db?resizing_type=fit)
5. Place a **Volume** device in the center of the pen.
6. Customize the **Volume** to disable player events:

   [![](https://dev.epicgames.com/community/api/documentation/image/a2e2fdfc-bd0c-4dba-a1f1-b49b8c2b27d6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a2e2fdfc-bd0c-4dba-a1f1-b49b8c2b27d6?resizing_type=fit)
7. Place a **Timer** device and customize it:

   [![](https://dev.epicgames.com/community/api/documentation/image/494669d7-0260-4c81-ad7e-3660a62c6534?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/494669d7-0260-4c81-ad7e-3660a62c6534?resizing_type=fit)

   [![](https://dev.epicgames.com/community/api/documentation/image/9facc71f-b4fc-4244-8339-ad2f9fb09787?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9facc71f-b4fc-4244-8339-ad2f9fb09787?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Duration | 15.0 Seconds |
   | Start at Game Start | On |
   | Can Interact | No |
   | Success on Timer End | False |
   | Visible During Game | Hidden |
   | Timer Color | White |
   | Timer Running Text | Capture a chicken before time runs out! |

### Bind Functions and Events

[Direct event binding](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#directeventbinding) is how you set devices to communicate directly with other devices. This involves setting [functions](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#function) and [events](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#event) for the devices involved.

You now have the basic functionality for a timed chicken capture challenge!

### Design Tip

Think about other interesting ways to interact with these fowl creatures. You could use a chicken to give a player a boost in jump height or provide a slow glide, or maybe use a chicken toss to  trigger a new phase of gameplay in a puzzle game!

## Build a Raptor Companion Adventure

Some spawned wildlife can be tamed by players and become a player's companion.

In this example, you'll see how to give the player a Raptor that the player can tame, and ride, and that can help in combat!

### Devices Used

- 1 x Wildlife Spawner device
- 1 x Player Spawner device
- 1 x Item Granter device
- 2 x [Creature Spawner](https://dev.epicgames.com/documentation/fortnite/using-creature-spawner-devices-in-fortnite-creative) devices
- 2 x [Tracker](https://dev.epicgames.com/documentation/fortnite/using-tracker-devices-in-fortnite-creative) devices
- 1 x [Beacon](https://dev.epicgames.com/documentation/fortnite/using-beacon-devices-in-fortnite-creative) device
- 1 x [Trigger](https://dev.epicgames.com/documentation/fortnite/using-trigger-devices-in-fortnite-creative) device
- 1 x [End Game](https://dev.epicgames.com/documentation/fortnite/using-end-game-devices-in-fortnite-creative) device

### Set Up the Basic Gameplay

1. Begin with the **Mountain Ridge Island** starter island.
2. Place a **Player Spawner** device near the large mountain on the island.
3. Customize the Player Spawner to set **Visible in Game** to **Off**.

   [![](https://dev.epicgames.com/community/api/documentation/image/7e3f87e9-3a22-47e8-ace4-7d88b7612a6b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7e3f87e9-3a22-47e8-ace4-7d88b7612a6b?resizing_type=fit)
4. Place an **Item Granter** device and register a **Makeshift Bow** to the device.
5. Customize the Item Granter:

   [![](https://dev.epicgames.com/community/api/documentation/image/2be7d0f9-08d5-4784-a313-d1672fd565a7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2be7d0f9-08d5-4784-a313-d1672fd565a7?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Receiving Players | All |
   | Spare Weapon Ammo | 30 |
   | Grant on Game Start | On |
6. Place a **Wildlife Spawner** device in front of the Player Spawner.
7. Customize the Wildlife Spawner:

   [![](https://dev.epicgames.com/community/api/documentation/image/b43cb9cb-6732-4bfa-9aec-b95ab742393a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b43cb9cb-6732-4bfa-9aec-b95ab742393a?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Type | Raptor |
   | Spawn Count | 1 |
   | Spawn Radius | 1.0M |
   | Invincible | Yes |
   | Riding | Enabled |
8. Place a **Creature Spawner** part of the way up the mountain.
9. Customize the Creature Spawner:

   [![](https://dev.epicgames.com/community/api/documentation/image/4ab629a7-1fc2-419f-90c6-2a5eb8cc23f6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4ab629a7-1fc2-419f-90c6-2a5eb8cc23f6?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Creature Type | Fiend |
   | Limit Spawned Creatures | Yes |
   | Total Spawn Limit | 4 |
   | Spawner Visibility | Off |
   | Spawn Effects Visibility | Off |
   | Max Spawn Distance | 1.0 Tiles |
10. Duplicate this Creature Spawner and place the copy further up the mountain.

### Configure the Quests

### Set Up the Game End

### Bind Functions and Events

You now have a working adventure game with a Raptor companion!

### Design Tip

Consider how raptors and other rideable animals can spruce up your gameplay.  The unique jump height boost on the raptor can give players new traversal possibilities, and the energy settings on the Wildlife Spawner device provide fine control over movement strength for spawned animals.

Also think about how you can use tamable animals as a combat advantage for players to discover!
