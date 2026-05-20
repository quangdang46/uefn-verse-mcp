## https://dev.epicgames.com/documentation/en-us/fortnite/creature-spawner-device-design-examples-in-fortnite

# Creature Spawner Device Design Examples

See some ways to use this device to create interesting gameplay.

![Creature Spawner Device Design Examples](https://dev.epicgames.com/community/api/documentation/image/7932a250-5754-49ae-a059-6728ef2195b7?resizing_type=fill&width=1920&height=335)

You can control lots of different aspects of the creatures spawned in your game, from their appearance to when and how often they spawn.

Have a look at some interesting ways to manage creature spawning in these examples.

## Unique Creature Rush

You can combine the **Creature Spawner** device with the **Creature Manager** device to create unique enemy behavior.

### Devices Used

- 1 x [Creature Spawner](https://dev.epicgames.com/documentation/fortnite/using-creature-spawner-devices-in-fortnite-creative) device
- 1 x [Player Spawner](https://dev.epicgames.com/documentation/fortnite/using-player-spawn-pad-devices-in-fortnite-creative) device
- 1 x [Creature Manager](https://dev.epicgames.com/documentation/fortnite/using-creature-manager-devices-in-fortnite-creative) device

### Set Up the Gameplay

You now have the basic functionality for a unique fiend enemy!

### Design Tip

This basic combination of devices can be used to create precisely balanced creature gameplay. If you’re using random enemy spawns on the Creature Spawner, consider using multiple Creature Managers for different creature types to get unique behavior for every different creature!

## Puzzle Creature Spawner

The Creature Spawner device has functions that can eliminate creatures and even destroy the entire spawner when an event is called. In this example, you’ll use this functionality to create a Creature Spawner that can only be destroyed by completing a simple puzzle.

### Devices Used

- 1 x Creature Spawner device
- 1 x Player Spawner device
- 1 x [Item Granter](https://dev.epicgames.com/documentation/fortnite/using-item-granter-devices-in-fortnite-creative) device
- 3 x [Prop Manipulator](https://dev.epicgames.com/documentation/fortnite/using-prop-manipulator-devices-in-fortnite-creative) devices
- 1 x [Tracker](https://dev.epicgames.com/documentation/fortnite/using-tracker-devices-in-fortnite-creative) device

### Set Up the Basic Gameplay

### Create the Puzzle

1. Place a **Tracker** device.
2. Customize the Tracker as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/32fc812a-1644-4ac6-b494-18393872a238?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/32fc812a-1644-4ac6-b494-18393872a238?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Stat to Track | Events |
   | Target Value | 3 |
   | Tracker Title | Idols |
   | Description Text | Destroy the Idols! |
3. Configure the following event on the Tracker so that when the player completes their objective, the creatures will be eliminated and the spawner will be destroyed.

   [![](https://dev.epicgames.com/community/api/documentation/image/f7d8af95-9b8f-4ee9-a59f-d17764b16929?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f7d8af95-9b8f-4ee9-a59f-d17764b16929?resizing_type=fit)

   | Event | Select Device | Select Function |
   | --- | --- | --- |
   | When Complete Send Event To | Creature Spawner | Destroy Spawner |
   | When Complete Send Event To | Creature Spawner | Eliminate Creatures |
4. Place a statue from the **Jungle Temple Prop Gallery**.
5. Place a **Prop Manipulator** device connected to the statue.
6. Customize the Prop Manipulator as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/cafd7448-721d-4830-a358-5eabb9593b97?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cafd7448-721d-4830-a358-5eabb9593b97?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Mopdify Prop Health | Yes |
   | Prop Health | 200 |
7. Configure the following event on the Prop Manipulator so that when the player destroys it, it increments the objective progress on the Tracker.

   [![](https://dev.epicgames.com/community/api/documentation/image/0f8bb1b2-f466-4a82-b925-304f4d16865a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0f8bb1b2-f466-4a82-b925-304f4d16865a?resizing_type=fit)

   | Event | Select Device | Select Function |
   | --- | --- | --- |
   | On Destroyed Send Event To | Tracker | Increment Progress |
8. Duplicate the statue and Prop Manipulator twice and place them in various visible locations around the area.

You now have the functionality for a Creature Spawner that can only be destroyed by completing a separate objective!

### Design Tip

Enemies like creatures can be a great way to create tension while the player completes other gameplay objectives. After all, a puzzle is always harder when you're being chased by a horde of monsters!

## Build a Creature Survival Game!

The Creature Spawner has built-in settings that can make it very easy to theme the enemies with a consistent aesthetic. In this example, you’ll use this functionality to create a creature survival game set in an arctic tundra!

### Devices Used

- 3 x Creature Spawner devices
- 1 x Player Spawner device
- 2 x Item Granter devices
- 1 x [Elimination Manager](https://dev.epicgames.com/documentation/fortnite/using-elimination-manager-devices-in-fortnite-creative) device
- 1 x [Health Powerup](https://dev.epicgames.com/documentation/fortnite/using-health-powerup-devices-in-fortnite-creative) device
- 3 x [Conditional Button](https://dev.epicgames.com/documentation/fortnite/using-conditional-button-devices-in-fortnite-creative) devices
- 1 x [Quadcrusher Spawner](https://dev.epicgames.com/documentation/fortnite/using-quadcrasher-spawner-devices-in-fortnite-creative) device

### Set Up the Basic Gameplay

1. Start with the **Arctic Island** starter island.
2. Place the **Ice House Hut A** prefab.
3. Use a **Billboard** device to label the building as the shop.
4. Place a **Player Spawner** device in front of the shop.
5. Customize the Player Spawner as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/6c33b194-fda2-48ba-833e-8b5acd56b1c6?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6c33b194-fda2-48ba-833e-8b5acd56b1c6?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Visible in Game | Off |
6. Place an **Item Granter** device and register a **Tactical Assault Rifle** to the device.
7. Customize the Item Granter as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/9ae0f300-eff4-45e6-8b7b-7e742a490b6e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9ae0f300-eff4-45e6-8b7b-7e742a490b6e?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Receiving Players | All |
   | Spare Weapon Ammo | 999 |
   | Grant on Game Start |  |
8. Place an **Elimination Manager** device and register **Gold** to the device.
9. Customize the Elimination Manager as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/a9af3bf2-74f5-46f6-9adc-e37a7911da5b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a9af3bf2-74f5-46f6-9adc-e37a7911da5b?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Target Type | All Creatures |
   | Run Over Pickup | On |
10. Place a **Creature Spawner** device in front of the shop.
11. Customize the Creature Spawner as follows:

    [![](https://dev.epicgames.com/community/api/documentation/image/a9bc77a2-168a-4c9e-9fc5-0960e0e16fca?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a9bc77a2-168a-4c9e-9fc5-0960e0e16fca?resizing_type=fit)

    | Option | Value |
    | --- | --- |
    | Spawner Type | Ice Spawner |
    | Creature Type | Ice Random |
    | Number of Creatures | 2 |
    | Activation Range | 5.0 Tiles |
    | Max Spawn Distance | 1.0 Tiles |
    | Restore Player Shield on Elimination | Off |
12. Duplicate this Creature Spawner two more times and place them both away from the shop, raising the **Number of Creatures** on each to **4** and **6** respectively.

### Configure the Shop

1. Place a **Health Powerup** device.
2. Customize the Health Powerup as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/79e1446f-2ca2-4ef5-a950-652dc37d3d6d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/79e1446f-2ca2-4ef5-a950-652dc37d3d6d?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Effect | Set To |
   | Effect Magnitude | 100 |
   | Time To Respawn | Instant |
   | Ambient Audio | Off |
   | Pick Up Audio | Off |
   | Who Can See This Powerup | None |
3. Place a **Conditional Button** device for the health upgrade and register **Gold** to the device.
4. Label it with a **Billboard**.
5. Customize the **Conditional Button** as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/bfbc87eb-30c5-47e7-94e8-1658e6a31227?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bfbc87eb-30c5-47e7-94e8-1658e6a31227?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Interact Text | Buy Health |
   | Key Items Required | 2 |
6. Configure the following event on the Conditional Button so that when the player pays, their health is restored.

   [![](https://dev.epicgames.com/community/api/documentation/image/d3962b4f-8af6-4e67-a706-233203f81116?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d3962b4f-8af6-4e67-a706-233203f81116?resizing_type=fit)

   | Event | Select Device | Select Function |
   | --- | --- | --- |
   | On Activated Send Event To | Health Powerup | Pickup |
7. Place an **Item Granter** and register a **Legendary Tactical Assault Rifle** to the device.
8. Customize the Item Granter as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/4d48bc28-1626-4c8a-ad85-7691ac444400?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4d48bc28-1626-4c8a-ad85-7691ac444400?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Spare Weapon Ammo | 999 |
9. Place a Conditional Button for the weapon upgrade and register Gold to the device. Label it with a Billboard.
10. Customize the Conditional Button as follows:

    [![](https://dev.epicgames.com/community/api/documentation/image/ad1ff156-1bd2-4ad7-8e17-7bfe893c896e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ad1ff156-1bd2-4ad7-8e17-7bfe893c896e?resizing_type=fit)

    | Option | Value |
    | --- | --- |
    | Interact Text | Buy Weapon Upgrade |
    | Key Items Required | 5 |
11. Configure the following event on the Conditional Button so that when the player pays, they receive an upgraded weapon.

    [![](https://dev.epicgames.com/community/api/documentation/image/1b67d681-8934-4635-a99a-269656dc957a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1b67d681-8934-4635-a99a-269656dc957a?resizing_type=fit)

    | Event | Select Device | Select Function |
    | --- | --- | --- |
    | On Activated Send Event To | Weapon Upgrade Item Granter | Grant Item |
12. Place a Quadcrusher Spawner device outside the shop.
13. Customize the Quadcrusher Spawner as follows:

    [![](https://dev.epicgames.com/community/api/documentation/image/b1e50e1c-187c-47a7-9d9d-b40a9736cd5f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b1e50e1c-187c-47a7-9d9d-b40a9736cd5f?resizing_type=fit)

    | Options | Value |  |
    | --- | --- | --- |
    | Enabled During Phase | None |  |
    | Visible During Game |  |  |
14. Place a **Conditional Button** for the Quadcrusher and register **Gold** to the device. Label it with a **Billboard**.
15. Customize the Conditional Button as follows:

    [![](https://dev.epicgames.com/community/api/documentation/image/7660904c-b91b-488a-a1a1-9a9cd4ba5670?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7660904c-b91b-488a-a1a1-9a9cd4ba5670?resizing_type=fit)

    | Option | Value |
    | --- | --- |
    | Interact Text | Buy Quadcrusher |
    | Key Items Required | 8 |
16. Configure the following event on the Conditional Button so that when the player pays, the Quadcrusher spawns.

    [![](https://dev.epicgames.com/community/api/documentation/image/bb5cb281-0529-4a2c-b671-9db83f6a7fbb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bb5cb281-0529-4a2c-b671-9db83f6a7fbb?resizing_type=fit)

    | Event | Select Device | Select Function |
    | --- | --- | --- |
    | On Activated Send Event To | Quadcrusher Spawner | Enable |

### Modify Island Settings

Make the following modifications to the island settings.

You now have the core functionality for an icy creature survival game!

### Design Tip

Consider how you could use the built-in events on the Creature Spawner to create an even more immersive experience. For example, you could connect a Creature Spawner to an Audio Player and have an ominous sound effect play anytime a creature is spawned. With these events, the possibilities are endless!
