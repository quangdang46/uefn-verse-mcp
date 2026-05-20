## https://dev.epicgames.com/documentation/en-us/fortnite/lock-device-design-examples

# Lock Device Design Examples

Explore the versatility of a simple Lock device!

![Lock Device Design Examples](https://dev.epicgames.com/community/api/documentation/image/8496d36e-732c-4d3b-820d-f072df269c34?resizing_type=fill&width=1920&height=335)

You can use the **Lock** device to customize the state and accessibility of a door. Locking and unlocking can be triggered by player actions or by other devices.

This device only works with assets that have a door or gate attached.

## Locking a Door

The most basic use for the Lock device is — you guessed it — locking a door!

Connect the lock to a **Button** device for easy toggling between locked and unlocked states.ndefined

### Devices Used

- 1 x [Lock](https://dev.epicgames.com/documentation/fortnite/using-lock-devices-in-fortnite-creative) device
- 1 x [Player Spawner](https://dev.epicgames.com/documentation/fortnite/using-player-spawn-pad-devices-in-fortnite-creative) device
- 1 x [Button](https://dev.epicgames.com/documentation/fortnite/using-button-devices-in-fortnite-creative) device

### Set Up the Devices

You now have the basic functionality for a locking door!

### Design Tip

The Lock device can very easily be connected to a Conditional Button device to give the added requirement that aplayer possess the correct key. The key can be anything: an actual key, a specific weapon, a fish, or anything else you can imagine.

## Escape Room Exit

Locks are a core part of any escape room or puzzle game where players must solve a puzzle to get out of an area. In this example, you’ll set up a basic puzzle that unlocks the player’s exit when solved.

### Devices Used

- 1 x **Lock** device
- 1 x **Player Spawner** device
- 1 x [HUD Message](https://dev.epicgames.com/documentation/fortnite/using-hud-message-devices-in-fortnite-creative) device
- 1 x [Audio Player](https://dev.epicgames.com/documentation/fortnite/using-audio-player-devices-in-fortnite-creative) device
- 4 x [Switch](https://dev.epicgames.com/documentation/fortnite/using-switch-devices-in-fortnite-creative) devices

### Set Up the Play Area

1. Place the **Castle Cellar** prefab.
2. Place a **Player Spawner** device inside the building.
3. Customize the player spawner to **not be visible in-game**:

   [![](https://dev.epicgames.com/community/api/documentation/image/1d9b23b1-182b-46b2-bc18-31d090c2a646?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1d9b23b1-182b-46b2-bc18-31d090c2a646?resizing_type=fit)
4. Place a lock on each of the two doors leading outside.
5. Place a **HUD Message** device.
6. Customize the HUD message:

   [![](https://dev.epicgames.com/community/api/documentation/image/511e8f74-09bb-4015-af4d-0b4b27a0541c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/511e8f74-09bb-4015-af4d-0b4b27a0541c?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Message | Flip all three levers to escape! |
   | Show on Round Start | On |
   | Time from Round Start | Instant |
   | Text Color | White |
7. Place an **Audio Player** device. (In later steps, you will configure this to play a sound effect when the puzzle is completed.)
8. Customize the audio player:

   [![](https://dev.epicgames.com/community/api/documentation/image/bc6e2373-a3cf-4fa7-8562-470142440981?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/bc6e2373-a3cf-4fa7-8562-470142440981?resizing_type=fit)

   | Option | Value | Description |
   | --- | --- | --- |
   | Enable Spatialization | Off | Makes sure the audio pan is equal regardless of where the player is. |
   | Enable Volume Attenuation | Off | Makes sure the audio volume is equal regardless of where the player is. |

### Configure the Switch System

Next, you’ll set up a basic logic system that will be able to tell whether all of the puzzle switches are on or not.

You now have the basic functionality for an escape room using locks!

### Design Tip

To add some more tension to a puzzle like this, try giving the player some type of time limit. That could be as simple as a Timer that locks them inside permanently if they don’t complete the puzzle in a certain amount of time. Or, think of more creative ways to limit the player, like slowly doing damage to them while inside or filling the room up with water!

### Build a Door Parkour Game!

When combined with other devices like the Timer, the Lock device can produce very interesting results. In this example, you’ll create a parkour map using opening and closing doors as a primary mechanic!

### Devices Used

1. 8 x **Lock** devices
2. 1 x **Player Spawner** device
3. 1 x [Prop Mover](https://dev.epicgames.com/documentation/fortnite/using-prop-mover-devices-in-fortnite-creative) device
4. 1 x [Bouncer Gallery](https://dev.epicgames.com/documentation/fortnite/using-bouncer-gallery-devices-in-fortnite-creative) device
5. 1 x [Damage Volume](https://dev.epicgames.com/documentation/fortnite/using-damage-volume-devices-in-fortnite-creative) device
6. 1 x [Timer](https://dev.epicgames.com/documentation/fortnite/using-timer-devices-in-fortnite-creative) device
7. 1 x [Trigger](https://dev.epicgames.com/documentation/fortnite/using-trigger-devices-in-fortnite-creative) device
8. 1 x [End Game](https://dev.epicgames.com/documentation/fortnite/using-end-game-devices-in-fortnite-creative) device

### Set Up Your Parkour Island

Begin by setting up your parkour island using floors from the **Colossal Coliseum Floor & Stair Gallery** and doors from the **Colossal Coliseum Wall Gallery**. While setting up the island, test out the jumps yourself to dial in the distances between objects! If you’re confused about how things should look, see the video above.

1. Place a floor floating high up in the air.
2. On the starting floor, place a Player Spawner.
3. Customize the Player Spawner so **Visible in Game** is set to **Off**

   [![](https://dev.epicgames.com/community/api/documentation/image/d66738a4-3042-4c4f-b267-58f607ef699d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d66738a4-3042-4c4f-b267-58f607ef699d?resizing_type=fit)
4. In front of the starting platform, place a few floors with doors on either side.
5. In front of this platform, place another floor up and slightly to the left.
6. Place a Prop Mover on this platform. Make sure that the device appears green while placing, which indicates that it is connected to the platform. Rotate the Prop Mover to point to the right.
7. Customize the Prop Mover:

   [![](https://dev.epicgames.com/community/api/documentation/image/5fa9339e-5c79-4a5a-ad0d-3f726e630fa3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/5fa9339e-5c79-4a5a-ad0d-3f726e630fa3?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Speed | 4.0 Meters/Second |
   | On Player Collision Behavior | Continue |
   | Player Damage on Collision | 0.0 |
   | Path Complete Action | Ping Pong |
8. In front and below this platform, place a bouncer from the Bouncer Gallery device.
9. Customize the Bouncer:
10. Way above the Bouncer, place another platform with a door in front.
11. Create a path of four horizontal doors with gaps between them, each one raised slightly from the last. Rotate them differently to create some variation.
12. After the last door, place another platform blocked by a door. This will be the ending point for the parkour course!
13. Place a Damage Volume on the ground below the parkour course.
14. Customize the Damage Volume:

    [![](https://dev.epicgames.com/community/api/documentation/image/cbe30e70-8633-4350-91ff-fe5357c0288d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cbe30e70-8633-4350-91ff-fe5357c0288d?resizing_type=fit)

    | Option | Value |
    | --- | --- |
    | Zone Depth | 100 |
    | Zone Height | Minimal |
    | Damage Type | Elimination |

### Configure the Locks

### Set Up the Game End

### Modify Island Settings

Make the following modifications to the island settings.

You now have a working parkour game using locks!

### Design Tip

This example uses only one timer to control all of the locks, but consider having more timers to control each lock individually. This would give more control over each door, allowing you to set some to be quicker than others!
