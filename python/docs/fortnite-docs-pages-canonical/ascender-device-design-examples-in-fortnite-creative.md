## https://dev.epicgames.com/documentation/en-us/fortnite/ascender-device-design-examples-in-fortnite-creative

# Ascender Device Design Examples

See several ways to use the ascender to speed your players to greater heights!

![Ascender Device Design Examples](https://dev.epicgames.com/community/api/documentation/image/d1ba31c0-fb9b-44bb-8bdf-4eabc52d0a99?resizing_type=fill&width=1920&height=335)

The **Ascender** device is a fast-moving cable mechanism that players can use to travel up or down.

Following are three examples of fun ways to use this device.

## Example 1: High Ground Ascender

The ascender is great for giving players a way to gain the high ground in a competitive environment.

### Devices Used

- 1 x [**Ascender**](using-ascender-devices-in-fortnite-creative) device
- 1 x [Player Spawner](https://dev.epicgames.com/documentation/fortnite/using-player-spawn-pad-devices-in-fortnite-creative) device
- 1 x [**Item Granter**](using-item-granter-devices-in-fortnite-creative) device
- 1 x [**Guard Spawner**](using-guard-spawner-devices-in-fortnite-creative) device

### Set Up the Devices

1. Place the **Pueblo Bell Tower** from the **Prefabs** category under the **Content** browser to establish the high ground.
2. Place a **Player Spawner** device on the ground.
3. Place an **Item Granter** device and register a **Legendary Tactical Assault Rifle** to the device.
   Customize the Item Granter as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/b4f85776-8fe9-4deb-b581-7832282eba35?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b4f85776-8fe9-4deb-b581-7832282eba35?resizing_type=fit)

   | Option | Value | Description |
   | --- | --- | --- |
   | **Receiving Players** | All | Any player can receive the rifle. |
   | **Grant on Game Start** | On | The player receives the rifle at the start of the game. |
4. Place an **Ascender** device leading up to the top of the tower.
5. Customize the ascender as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/c87650ce-7b9c-4b6f-a4ee-55ffaf0ba156?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c87650ce-7b9c-4b6f-a4ee-55ffaf0ba156?resizing_type=fit)

   | Option | Value | Description |
   | --- | --- | --- |
   | **Ascender Style** | Wall | The ascender looks like a wall. |
6. Place a **Guard Spawner** on the ground.
7. Customize the device as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/2dbb1e80-a394-4a53-b248-6e5ae2a077b2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2dbb1e80-a394-4a53-b248-6e5ae2a077b2?resizing_type=fit)

   | Option | Value | Description |
   | --- | --- | --- |
   | **Guard Team Option** | Team Wildlife & Creatures | Sets the team the guards are assigned to. |

You now have the basic functionality for a high ground advantage using the Ascender device!

### Design Tip

Gaining the high ground is a huge advantage in many competitive modes and can be tied into many interesting gameplay choices.

Consider giving the player a choice to either take a slow but protected interior stairwell or a fast but exposed Ascender when trying to climb a building.

## Example 2: Build an Alarm Ascender

The Ascender device can be configured to send events when players begin or end ascending or descending. In this example, you’ll use this functionality to create an ascender connected to an alarm system that triggers when players ascend.

### Devices Used

- 1 x [**Ascender**](using-ascender-devices-in-fortnite-creative) device
- 1 x [Player Spawner](https://dev.epicgames.com/documentation/fortnite/using-player-spawn-pad-devices-in-fortnite-creative) device
- 5 x [**Customizable Light**](using-customizable-light-devices-in-fortnite-creative) devices
- 5 x **[Audio Player](https://dev.epicgames.com/documentation/en-us/fortnite-creative/using-audio-player-devices-in-fortnite-creative)** devices

### Set Up the Play Area

### Configure the Alarm System

1. Place a **Customizable Light** device near the top of the ascender.
2. Customize the light as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/6e418efa-de2e-4ead-b58a-621a86be51e8?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6e418efa-de2e-4ead-b58a-621a86be51e8?resizing_type=fit)

   | Option | Value | Description |
   | --- | --- | --- |
   | **Initial State** | Off | Starts the game with the light off. It will remain off until triggered. |
   | **Light Color** | #FF0100 | A red light builds the tension. |
   | **Light Intensity** | 25% | Softens the light. |
   | **Light Size** | Huge (100) | Sets how much area the light will shine on. |
   | **Rhythm Preset** | Wave | Makes the light change in a rhythmic pattern. |
   | **Rhythm Time** | X8 | How fast the pattern changes. |
3. Configure the following [functions](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#function) on the light to turn it on when the player reaches the top of the ascender.

   [![](https://dev.epicgames.com/community/api/documentation/image/7ecc00ee-d20b-46b1-86ac-06f627759136?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7ecc00ee-d20b-46b1-86ac-06f627759136?resizing_type=fit)

   | Function | Select Device | Select Event |
   | --- | --- | --- |
   | **Turn On** | Ascender | Ascend End |
4. Place an Audio Player device.
5. Customize the audio player as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/da5618cf-9dbe-4fb9-bc01-f82a9d3fcb3d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/da5618cf-9dbe-4fb9-bc01-f82a9d3fcb3d?resizing_type=fit)

   | Option | Value | Description |
   | --- | --- | --- |
   | **Audio** | Threat | This option makes an alarming sound. |
   | **Visible in Game** | On | Players can see the device in-game. |
   | **Play on Hit** | Off | Doesn't make a sound if the player collides with it. |
   | **Mesh** | Loudspeaker | The device will appear as a loudspeaker in-game. |
6. Configure the following functions on the audio player to play the sound when the player finishes ascending.

   [![](https://dev.epicgames.com/community/api/documentation/image/dbb673b2-0567-44fa-9965-9ee532640966?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dbb673b2-0567-44fa-9965-9ee532640966?resizing_type=fit)

   | Function | Select Device | Select Event |
   | --- | --- | --- |
   | **Play** | Ascender | Ascend End |
7. Duplicate the Customizable Light and Audio Player devices four times each, placing them around the castle.

You now have the basic functionality for a system that triggers an alarm when a player uses the ascender.

### Design Tip

This functionality could be very engaging in an asymmetrical game mode where one team defends a base while another team attempts to infiltrate it.

Consider using this system to increase the tension in a single-player heist game mode!

## Example 3: Build a Boss Battle Entrance with the Ascender!

The **Ascender** device can be enabled and disabled with events from other devices, making it perfect for a traversal method that can be unlocked.

In this example, you’ll set up a basic adventure game with a locked ascender that ultimately carries the player up to the boss battle!

### Devices Used

- 1 x [**Ascender**](using-ascender-devices-in-fortnite-creative) device
- 1 x [Player Spawner](https://dev.epicgames.com/documentation/fortnite/using-player-spawn-pad-devices-in-fortnite-creative) device
- 1 x [**Item Granter**](using-item-granter-devices-in-fortnite-creative) device
- 6 x [**Creature Placer**](using-creature-placer-devices-in-fortnite-creative) devices
- 1 x [**Elimination Manager**](using-elimination-manager-devices-in-fortnite-creative) device
- 1 x [**Conditional Button**](using-conditional-button-devices-in-fortnite-creative) device
- 1 x [Audio**Player**](https://dev.epicgames.com/documentation/en-us/fortnite-creative/using-audio-player-devices-in-fortnite-creative) device
- 1 x [**Post Process**](using-post-process-devices-in-fortnite-creative) device
- 1 x [**End Game**](using-end-game-devices-in-fortnite-creative) device

### Set Up the Starting Area

1. Begin with the **Temperate Island** starter island.
   Place a **Player Spawner** device in the northwest valley of the Island.
   Customize the spawner **Visible in Game** option to **Off**.

   [![](https://dev.epicgames.com/community/api/documentation/image/8b29db53-76a9-4896-adb2-22e8a9838513?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8b29db53-76a9-4896-adb2-22e8a9838513?resizing_type=fit)
2. Place five **Creature Placer** devices along the path leading up the hill.

   [![](https://dev.epicgames.com/community/api/documentation/image/d5d560e8-e555-4da6-8f58-c4b89c9ec2ad?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d5d560e8-e555-4da6-8f58-c4b89c9ec2ad?resizing_type=fit)
3. Customize the creature placers as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/273e4da8-9d47-473f-987d-ecae00a08f75?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/273e4da8-9d47-473f-987d-ecae00a08f75?resizing_type=fit)

   | Option | Value | Description |
   | --- | --- | --- |
   | **Creature Type** | Red Fiend | Vary this setting between the Creature Placers to create interesting gameplay. |
   | **Activation Range** | 5.0 Tiles | Vary this setting between the Creature Placers to create interesting gameplay. |
4. Place an **Elimination Manager** device, then register a stack of **gold** to the device.
5. Customize the elimination manager as follows:

   | Option | Value | Description |
   | --- | --- | --- |
   | **Target Type** | All creatures | This applies to any creatures you add. |
   | **Run Over Pickup** | On | Lets the player pick up an item by running over it. |
6. Place a **Post Process** device.
7. Customize the device by setting the **Post Process Effect** option to **Horror Movie** to make things look creepy.

   [![](https://dev.epicgames.com/community/api/documentation/image/8d88182d-1f84-46a2-8d3a-1be32f0b8e0f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8d88182d-1f84-46a2-8d3a-1be32f0b8e0f?resizing_type=fit)

Consider adding more trees, rocks, or other props along the path to give it a more natural feel!

### Set Up the Ascender

### Configure the Boss Battle

### Bind Functions / Events

**Direct event binding** is how you set devices to communicate directly with other devices. This involves setting **functions** and **events** for the devices involved.

### Modify Island Settings

Make the following modifications to the island settings.

You now have the basic functionality for a system that uses an ascender to create a dramatic boss battle entrance!

### Design Tip

Turning an ascender on and off based on other conditions can be a powerful way to give players an unlockable advantage in a competitive game mode.

Try connecting the ascender to a Tracker device and requiring players to complete specific objectives to unlock use of the device.

Also, think of other effects that could be triggered when players ride the ascender to create more dramatic and exciting gameplay moments!
