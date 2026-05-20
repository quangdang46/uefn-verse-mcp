## https://dev.epicgames.com/documentation/en-us/fortnite/health-powerup-design-examples-in-fortnite

# Health Powerup Device Design Examples

Reward players with increased health for themselves and their shields.

![Health Powerup Device Design Examples](https://dev.epicgames.com/community/api/documentation/image/f3b0df88-0937-4a97-a5ee-ec40b699c34b?resizing_type=fill&width=1920&height=335)

Health Powerup is a device you can use in many different ways to regenerate a player's health, the health of their shield, or both. Find out a few cool ways to work this device into your island gameplay!

## Health Boost Pickup

You can set up a health boost that increases a player’s health over time. In this example, you’ll configure the device to give the player a three-second health boost when they pick up the device.

### Devices Used

- 3 x Health Powerup devices
- 1 x [Player Spawner](https://dev.epicgames.com/documentation/fortnite/using-player-spawn-pad-devices-in-fortnite-creative) device
- 1 x [Item Granter](https://dev.epicgames.com/documentation/fortnite/using-item-granter-devices-in-fortnite-creative) device
- 1 x [Creature Spawner](https://dev.epicgames.com/documentation/fortnite/using-creature-spawner-devices-in-fortnite-creative) device

### Set Up the Devices

1. Start with the **T**ilted To**wers POI Island** starter island.
2. Place a **Player Spawner** device.
3. Place an **Item Granter** device and register a Tactical Assault Rifle to the device.
4. Customize the Item Granter as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/01ce1ce7-173f-42e0-b975-5b8f4f4ca5e3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/01ce1ce7-173f-42e0-b975-5b8f4f4ca5e3?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Receiving Players | All |
   | Grant on Game Start | On |
5. Place a **Creature Spawner** device.
6. Place a **Health Powerup** device.
7. Customize the Health Powerup as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/a96cfd55-67c0-4473-a5f3-3d33f69b817a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a96cfd55-67c0-4473-a5f3-3d33f69b817a?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Effect Magnitude | 15 |
   | Effect Duration | 3 Seconds |
8. Duplicate the Health Powerup two more times in different locations.

You now have the basic functionality for a powerup that gives a timed health boost!

### Design Tip

This core functionality of the Health Powerup is a great way to give players an incentive to move around your map in a multiplayer mode! Try playing with the spawn behavior on the powerups to get more variation in which powerups are reactivated, and when!

## Survival Safe Room

The Health Powerup pairs very well with other devices to create the appearance that the player is being healed by an unseen force!

In this example, you’ll use a Volume device with the Health Powerup device to create a safe room that heals the player!

### Devices Used

- 1 x Health Powerup device
- 1 x Player Spawner device
- 1 x [Wildlife Spawner](https://dev.epicgames.com/documentation/fortnite/using-wildlife-spawner-devices-in-fortnite-creative) device
- 2 x [Post Process Device](https://dev.epicgames.com/documentation/fortnite/using-post-processing-devices-in-fortnite-creative) devices
- 1 x [Volume](https://dev.epicgames.com/documentation/fortnite/using-volume-devices-in-fortnite-creative) device

### Set Up the Island

1. Start with the **Arctic Island** starter island.
2. Place a fire from the **Colossal Coliseum Prop Gallery** inside the building on the hill.
3. Place a **Player Spawner**.
4. Customize the Player Spawner so **Visible in Game** is set to **Off**:

   [![](https://dev.epicgames.com/community/api/documentation/image/4f724178-959b-411e-a147-3f0b4fd55a5f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4f724178-959b-411e-a147-3f0b4fd55a5f?resizing_type=fit)
5. Place a **Wildlife Spawner** between the Player Spawner and the building.
6. Customize the Wildlife Spawner as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/88113855-3180-4c18-80bd-afd44deeae1b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/88113855-3180-4c18-80bd-afd44deeae1b?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Biome Variant | Snow |
   | Allow Infinite Spawn | No |
   | Spawn Timer | 0.1 Seconds |
   | Spawn Through Walls | Off |
   | Spawn Radius | 30.0M |
   | Taming | Disabled |
7. Place a **Post Process** device.
8. Customize the Post Process device as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/7c149fc5-be08-4763-af62-aa08b3694dd8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7c149fc5-be08-4763-af62-aa08b3694dd8?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Post Process Effect | Frost |
   | Blend in Duration | 1.0 |
   | Blend out Duration | 1.0 |

### Configure the Safe Zone

### Modify Island Settings

Make the following modifications to the island settings.

You now have the functionality for a safe zone in an arctic survival game!

### Design Tip

Invisible Health Powerups can give the impression that anything is healing the player, as long as it can send events to start and stop the healing! For example, try healing the player whenever they are in a vehicle! Or maybe heal the player only when they are standing in fire!

## Build a Combat Game with Custom Health Pickup!

In this example, you’ll use events and functions on the Health Powerup to create your own custom health pickup, complete with audio and visual effects!

### Devices Used

- 1 x Health Powerup device
- 1 x Player Spawner device
- 1 x Item Granter device
- 1 x [Tracker](https://dev.epicgames.com/documentation/fortnite/using-tracker-devices-in-fortnite-creative) device
- 3 x [Creature Spawner](https://dev.epicgames.com/documentation/fortnite/using-creature-spawner-devices-in-fortnite-creative) devices
- 1 x [Prop Manipulator](https://dev.epicgames.com/documentation/fortnite/using-prop-manipulator-devices-in-fortnite-creative) device
- 1 x [Customizable Light](https://dev.epicgames.com/documentation/fortnite/using-customizable-light-devices-in-fortnite-creative) device
- 1 x [Audio Player](https://dev.epicgames.com/documentation/fortnite/using-audio-player-devices-in-fortnite-creative) device
- 1 x [VFX Spawner](https://dev.epicgames.com/documentation/fortnite/using-vfx-spawner-devices-in-fortnite-creative) device

### Set Up the Basic Gameplay

1. Place a **Player Spawner**.
2. Customize the Player Spawner so **Visible in Game** is set to **Off.**
3. Place an **Item Granter** and register a Tactical Assault Rifle to the device.
4. Customize the Item Granter as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/f6d43a80-68fd-43ce-9400-d37642049f86?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f6d43a80-68fd-43ce-9400-d37642049f86?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Receiving Players | All |
   | Grant on Game Start | On |
5. Place three **Creature Spawners** around the area.
6. Place a Tracker.
7. Customize the **Tracker** as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/bdc897a0-2802-4609-b6b7-ba4b4533bb0e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bdc897a0-2802-4609-b6b7-ba4b4533bb0e?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Stat to Track | Events |
   | Target Value | 5 |
   | Tracker Title | Eliminate Creatures |
   | Description Text | Eliminate 5 Creatures to Spawn the Healing Idol! |
   | Quest Icon | Enemy |
8. Configure the following **functions** on the Tracker to increment the progress each time a creature is eliminated.

   [![](https://dev.epicgames.com/community/api/documentation/image/d82cf20c-f8fb-4ef9-9788-1641411a0d01?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d82cf20c-f8fb-4ef9-9788-1641411a0d01?resizing_type=fit)

   | Function | Select Device | Select Event |
   | --- | --- | --- |
   | Increment Progress When Receiving From | Creature Spawner 1-3 | On a Creature Is Eliminated |

### Configure the Custom Health Powerup

1. Place a statue from the **Colossal Coliseum Prop Gallery**. Size the statue to be roughly the same size as the player.
2. Place a **Health Powerup** in the center of the statue.
3. Customize the Health Powerup as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/2aba62f4-b82d-4c01-aa51-eb0d7758a079?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2aba62f4-b82d-4c01-aa51-eb0d7758a079?resizing_type=fit)

   [![](https://dev.epicgames.com/community/api/documentation/image/acff128b-567a-4d58-8d22-6c74f47086a2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/acff128b-567a-4d58-8d22-6c74f47086a2?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Stat to Modify | Both |
   | Effect | Set To |
   | Effect Magnitude | 200 |
   | Pickup Radius | 1 |
   | Respawn | No |
   | Spawn on Minigame Start | No |
   | Ambient Audio | Off |
   | Pick Up Audio | Off |
   | Who Can See This Powerup | None |
4. Place a **Prop Manipulator** connected to the statue.
5. Customize the Prop Manipulator so **Start Hidden** is set to **On**:
6. Place a **Customizable Light** over the statue.
7. Customize the Customizable Light as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/0381cd9b-9122-4149-9025-1c2334038379?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0381cd9b-9122-4149-9025-1c2334038379?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Initial State | Off |
   | Light Color | #FFB000 |
8. Place an **Audio Player** by the statue.
9. Customize the Audio Player as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/7b5073bd-9566-4008-bc14-ff3c9e42207f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7b5073bd-9566-4008-bc14-ff3c9e42207f?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Audio | Unlock |
   | Play on Hit | Off |
10. Place a **VFX Spawner** on the statue.
11. Customize the VFX Spawner as follows:

    [![](https://dev.epicgames.com/community/api/documentation/image/219dc2ad-f46b-48bd-ab08-68407501dbd9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/219dc2ad-f46b-48bd-ab08-68407501dbd9?resizing_type=fit)

    | Option | Value |
    | --- | --- |
    | Effect Type | Burst |
    | Burst Visual Effect | Explosion Electrical |
12. Configure the following events on the Tracker to spawn the custom pickup when the player completes the creature elimination objective.

    [![](https://dev.epicgames.com/community/api/documentation/image/2c1196ae-55cb-4100-9214-d3b5701b04cd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2c1196ae-55cb-4100-9214-d3b5701b04cd?resizing_type=fit)

    | Event | Select Device | Select Function |
    | --- | --- | --- |
    | When Complete Send Event To | Customizable Light | Turn On |
    | When Complete Send Event To | Health Powerup | Spawn |
    | When Complete Send Event To | Prop Manipulator | Show Props |
    | When Complete Send Event To | Audio Player | Play |
13. Configure the following events on the Health Powerup to play the custom effects and destroy the Creature Spawners when the player picks it up.

    [![](https://dev.epicgames.com/community/api/documentation/image/00110316-4464-4c5c-bf07-bb2ec20f5563?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/00110316-4464-4c5c-bf07-bb2ec20f5563?resizing_type=fit)

    [![](https://dev.epicgames.com/community/api/documentation/image/b3476f7c-a77d-4648-9b79-df6a860cc0c6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b3476f7c-a77d-4648-9b79-df6a860cc0c6?resizing_type=fit)

    | Event | Select Device | Select Function |
    | --- | --- | --- |
    | On Item Picked Up Send Event To | Creature Spawner 1-3 | Destroy Spawner |
    | On Item Picked Up Send Event To | Creature Spawner 1-3 | Eliminate Creatures |
    | On Item Picked Up Send Event To | Customizable Light | Turn Off |
    | On Item Picked Up Send Event To | Prop Manipulator | Hide Props |
    | On Item Picked Up Send Event To | VFX Spawner | Restart |

You now have the core functionality for a custom health pickup!

### Design Tip

With the event that is called when the player picks up the Health Powerup, you can control any other device! Maybe if a player picks up a Health Powerup, the colors of the world should get brighter with a Post Process device! Or, you could this event to give the player a speed boost as well as a health boost!
