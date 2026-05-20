## https://dev.epicgames.com/documentation/en-us/fortnite/random-sentry-fight-in-fortnite-creative

# Random Sentry Fight

Put a new twist on the classic shooting gallery experience with randomly spawning sentries that shoot back at you!

![Random Sentry Fight](https://dev.epicgames.com/community/api/documentation/image/a9841ed0-a425-4522-9ba1-ab7ebdd40bb0?resizing_type=fill&width=1920&height=335)

[![Random Sentry Fight gameplay example](https://dev.epicgames.com/community/api/documentation/image/da565d0f-e5fc-4738-8c02-e2bffd09cd14?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/da565d0f-e5fc-4738-8c02-e2bffd09cd14?resizing_type=fit)

*Click to enlarge image.*

Players spawn with a pistol and no shield, a sentry spawns with a rocket launcher and takes aim at the player. Survival is the name of the game.

The developer's goal is to randomly spawn a sentry for the player to fight, this gameplay example helps the player work on their fight engagement skills and weapon accuracy. After creating this example, the developer will know how to use the following devices:

- [Random Number Generator device](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#random-number-generator)
- [Trigger device](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#trigger)
- [Class Selector device](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#class-selector)
- [Class Designer device](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#class-designer)
- [Timed Objective device](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#timer)
- [Score Manager device](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#score-manager)
- [Sentry device](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary)
- [Player Spawn Pad device](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary).

## Devices Used

To learn more about placing [devices](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#device), props, and using the [grid](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#grid), see the [Video Tutorials](https://www.epicgames.com/fortnite/en-US/creative/docs/fortnite-creative-video-tutorials).

- **5 x** [Sentry Device](using-sentry-devices-in-fortnite-creative)
- **5 x** [Trigger](https://dev.epicgames.com/documentation/fortnite/using-trigger-devices-in-fortnite-creative)
- **2 x** [Class Designer](using-class-designer-devices-in-fortnite-creative)
- **2 x** [Class Selector](using-class-selector-devices-in-fortnite-creative)
- **1 x** [Timed Objective device](https://dev.epicgames.com/documentation/fortnite/using-timed-objective-devices-in-fortnite-creative)
- **1 x** [Score Manager](https://dev.epicgames.com/documentation/fortnite/using-score-manager-devices-in-fortnite-creative)
- **1 x** [Random Number Generator](https://dev.epicgames.com/documentation/fortnite/using-random-number-generator-devices-in-fortnite-creative)

## Prefabs Used

You can use any prefab for this gameplay example you want. Alternatively, you don’t have to contain the player and sentry devices in an arena if you want to have an open concept level.

The following prefab was used:

- E.G.O. Science Station - 30 X Wall

[![Creating a rectangular arena box](https://dev.epicgames.com/community/api/documentation/image/0d7f70d8-17c1-405b-a7b4-f85d83e91104?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0d7f70d8-17c1-405b-a7b4-f85d83e91104?resizing_type=fit)

## Instructions

Each of the devices you need for this gameplay example is described below.

### Placing Prefab Walls

### Placing the Random Number Generator Device

Only modify the options described below, leave the rest of the default settings as is.

1. Press **Tab** to go into the **Creative Inventory**.
2. Click **Devices > Random Number Generator (RNG) > Equip** to add the Random Number Generator device to your **Quick Bar**. Continue to add the following devices from the menu:

   1. Player Spawn Pad device
   2. Sentry device
   3. Class Selector device
   4. Class Designer device
   5. Score Manager device
   6. Timed Objective device
   7. Trigger device
3. Place the RNG outside the arena. Make sure that the volume boxes of the device don’t go into the arena area.

   If the RNG volume boxes stray into the arena, copy the device and turn it around by pressing **E** to rotate the device out of the arena. Paste the RNG outside the arena, then delete the RNG you copied.

   [![Placing the Random Number Generator device outside the arena](https://dev.epicgames.com/community/api/documentation/image/6c0d1078-ec25-4773-9767-b4b32fdabe83?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6c0d1078-ec25-4773-9767-b4b32fdabe83?resizing_type=fit)
4. Edit the RNG device options.

   [![Editing the Random Number Generator device options](https://dev.epicgames.com/community/api/documentation/image/d997aa48-5260-473a-b8dd-d20f9a763944?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d997aa48-5260-473a-b8dd-d20f9a763944?resizing_type=fit)

   *Click image to enlarge.*

   | Option | Value | Explanation |
   | --- | --- | --- |
   | **Winning Value** | **3** | Determines the winning value that awards the shield and legendary assault rifle to the player. |
   | **Zone** | **Forward** | Set to move forward through the zone associated with the Trigger devices in the RNG volume boxes. |
   | **Activate When Receiving From** | **Channel 10** | Receives a signal from the Trigger device and randomly selects from volumes 1-6. |
   | **On Win Transmit On** | **Channel 9** | Sends a signal to the second Class Selector device to grant the player the Legendary Assault rifle and shield. |
   | **On Lose Transmit** | **Channel 8** | Sends a signal to the first Class Selector to grant the player a Rare Sidearm pistol. |
   | **When Rolled Max Transmit On** | **Channel 6** | When the number specified by Value Limit 2 is rolled, a signal is sent to the Score Manager to award Points to the player. |

   The default values for **Value Limit 1** (1) and **Value Limit 2** (6) are the values you want to work with, these volumes determine how many volume boxes to add to the RNG.
   The RNG counts as a sequencer, the Trigger devices in the volume boxes activate all devices set to accept sequencers when triggered by the RNG.

### Placing the Player Spawn Pad Device

### Placing the Trigger Device

### Placing the Sentry Devices

1. Select the **Sentry** device from the Quick Bar.
2. Place a Sentry in the arena against the back wall.

   [![Sentries placed against the back wall of the arena](https://dev.epicgames.com/community/api/documentation/image/e4c88680-5bd2-4d0f-a582-fef6eecf3eb9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e4c88680-5bd2-4d0f-a582-fef6eecf3eb9?resizing_type=fit)
3. Edit the first Sentry device options. This sentry is the easy sentry that the player fights after a losing roll of the RNG.

   [![Edit the first sentry options](https://dev.epicgames.com/community/api/documentation/image/35bd1ea8-1c7e-40f5-bb24-83e517714432?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/35bd1ea8-1c7e-40f5-bb24-83e517714432?resizing_type=fit)

   *Click image to enlarge.*

   | Option | Value | Explanation |
   | --- | --- | --- |
   | **Weapon Type** | **Burst Assault Rifle** | Equips the sentry with a Burst Assault rifle when it spawns. |
   | **Health** | **200** | Sentry has 200 health. |
   | **Range** | **50M** | Expand the range of the sentry to include a larger area so the sentry will start attacking when the player spawns into the arena. |
   | **Accuracy** | **Moderate** | The sentry has moderately good aim. |
   | **Spawn on Game Start** | **No** | The Random Number Generator will signal to spawn the sentry. |
   | **Score on Elimination** | **5** | When the sentry is eliminated it will award 5 points to the player. |
   | **Spawn When Receiving From** | **Channel 1** | Spawns a sentry when receiving a signal from the Trigger device. |
   | **Destroy Sentry When Receiving From** | **Channel 11** | This will destroy the sentry if they eliminate a player and a new one will spawn when the player respawns. |
   | **When Eliminated Transmit On** | **Channel 7** | Sends a signal to the Timer device after the sentry has been eliminated. |
   | **When Eliminating Player Transmit On** | **Channel 11** | If the sentry is successful in eliminating the player the sentry will send a signal. |
4. Copy the easy sentry and paste two more next to the first sentry.
5. Add higher Health and Accuracy levels and better Weapon Types to the third sentry.
6. Assign larger points to **Score on Elimination**.
7. Use the same values from the **Spawn When Receiving From** and **When Eliminated Transmit On** options above. This sentry is harder to eliminate, and is the sentry the player fights on a winning roll of the RNG.
8. Copy and paste this sentry two more times.

### Placing the Class Selector Device

[![Placing the Class Selector devices outside the arena](https://dev.epicgames.com/community/api/documentation/image/23cc93b0-f534-415e-a6ae-1eb190a188b9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/23cc93b0-f534-415e-a6ae-1eb190a188b9?resizing_type=fit)

### Placing the Class Designer Device

1. Select the **Class Designer** device from the Quick Bar.
2. Place the Class Designer outside the arena.

   [![Placing the Class Designer device outside the arena](https://dev.epicgames.com/community/api/documentation/image/b22bc88e-d1e3-4e8a-a9f3-632725a0a3fd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b22bc88e-d1e3-4e8a-a9f3-632725a0a3fd?resizing_type=fit)
3. Press **Tab** to go back to the **Creative Inventory**.
4. Select **Weapons > Rare Sidearm Pistol > Equip**. The Rare Sidearm Pistol icon appears in the Quick Bar.
5. Click, hold, and drag the Rare Sidearm Pistol icon out of the Quick Bar until you see the [backpack icon](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#backpack-icon), then release to drop the pistol into the Class Designer.

   [![Adding the Sidearm Pistol to the first Class Designer device](https://dev.epicgames.com/community/api/documentation/image/08ef1935-3cea-48c8-ba13-a6cb29c3e35a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/08ef1935-3cea-48c8-ba13-a6cb29c3e35a?resizing_type=fit)

   *Click image to enlarge.*
6. Edit the Class Designer device options.

   [![Editing the Class Designer device options](https://dev.epicgames.com/community/api/documentation/image/a54e5368-adcc-49f1-ac53-408d09bf250d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a54e5368-adcc-49f1-ac53-408d09bf250d?resizing_type=fit)

   *Editing the Class Designer device options.*

   | Option | Value | Explanation |
   | --- | --- | --- |
   | **Class Identifier** | **1** | Identifies the first class as the losing class that receives the rare sidearm pistol and no shields. |
   | **Grant Items on Respawn** | **Yes** | Equips the player with a weapon on respawn. |
   | **Equip Granted Item** | **First Item** | Automatically equips the weapon granted to the player. |
7. Select the Class Designer device from the Quick Bar again.
8. Place the second Class Designer device away from the first device so the weapon you select for the second Class Designer doesn’t get added to the first device by accident.
9. Follow the instructions above to add a **Legendary Assault Rifle** to the second Class Designer.
10. Edit the **Class Identifier** value to 2 and **Starting Shields** to 100%. This creates the winning class that is awarded a better weapon and shields.

### Placing the Score manager Device

### Placing the Timed Objective Device

## My Island Settings

Use My Island options to enhance your game’s experience. My Island options work with your device settings to determine the game’s structure and how your devices work together, and what the game UI does during your game.

Try the following:

### Game Options

[![Changing the Game options in My Island](https://dev.epicgames.com/community/api/documentation/image/9c92c808-8681-40b8-98c7-baac3c3c5109?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9c92c808-8681-40b8-98c7-baac3c3c5109?resizing_type=fit)

*Click image to enlarge.*

| Option | Value | explanation |
| --- | --- | --- |
| **Max Players** | **1** | You only want one player at a time in this game. |
| **Default Class** | **1** | This setting affects the player’s assigned class at the start of each game. |

### Settings Options

[![Chaning the Settings options in My Island](https://dev.epicgames.com/community/api/documentation/image/e9225a30-0be1-4609-9d84-ee4bd302d688?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/e9225a30-0be1-4609-9d84-ee4bd302d688?resizing_type=fit)

*Click image to enlarge.*

| Option | Value | Explanation |
| --- | --- | --- |
| **Infinite Ammo** | **On** | Make sure that the player doesn’t run out of ammo when they’re up against the sentries. |
| **Environment Damage** | **Off** | You don’t want the arena to get destroyed while the player takes on the sentries. |
| **Show StoneResource Count** | **No** | The player doesn’t need to see this information. |
| **Show Wood Resource Count** | **No** | The player doesn’t need to see this information. |
| **Show Metal Resource Count** | **No** | The player doesn’t need to see this information. |
| **Show Gold Resource Count** | **No** | The player doesn’t need to see this information. |

## Playing Your Game

From playing with this example, you’ll understand how to use the Score Manager to award points when triggered, how the RNG works with the Triggers and the Timed Objective device to randomly spawn Sentries, and how to create different player classes and parameters for each class.

Create your own version of the Random Sentry Fight by substituting sentries for creatures or animals. Try editing the radius for each of your sentries so they spawn at different distances between the player and the spawn point and change the points awarded based on the sentry’s level of difficulty.
