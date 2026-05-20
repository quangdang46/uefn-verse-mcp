## https://dev.epicgames.com/documentation/en-us/fortnite/prop-manipulator-device-design-examples-in-fortnite

# Prop Manipulator Device Design Examples

Explore some novel ways to use customized props in your gameplay!

![Prop Manipulator Device Design Examples](https://dev.epicgames.com/community/api/documentation/image/0bd2baed-c95e-4aad-89b3-ee92062e0c35?resizing_type=fill&width=1920&height=335)

Props can't do anything, right? Wrong!

With the **Prop Manipulator** device, you can customize your props in many of the same ways you would a device. Read on for some innovative ideas on how you can apply this device to the props on your island!

## Basic Hidden Prop

The Prop Manipulator can easily hide and show props, making them very useful for connecting to other devices!

### Devices Used

- 1 x [Prop Manipulator](https://dev.epicgames.com/documentation/fortnite/using-prop-manipulator-devices-in-fortnite-creative) device
- 1 x [Player Spawner](https://dev.epicgames.com/documentation/fortnite/using-player-spawn-pad-devices-in-fortnite-creative) device
- 1 x [Conditional Button](https://dev.epicgames.com/documentation/fortnite/using-conditional-button-devices-in-fortnite-creative) device

### Set Up the Gameplay

1. Start with an island that has trees, such as the **Temperate Island** starter island.
2. Place a **Player Spawner** device near some trees.
3. Place a barrel from the **Spire Prop Gallery**.
4. Place a **Prop Manipulator** device connected to the barrel.
5. Customize the Prop Manipulator as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/37d8ede9-13c6-46b2-bd3c-fb3d75a86876?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/37d8ede9-13c6-46b2-bd3c-fb3d75a86876?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Start Hidden | On |
   | Modify Prop Health | Yes |
   | Is Prop Invulnerable | Yes |
6. Place a **Conditional Button** device in front of the barrel and register **Wood** to the device.
7. Customize the Conditional Button as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/480e497b-ac7a-43da-acfc-6d9e16cec34c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/480e497b-ac7a-43da-acfc-6d9e16cec34c?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Interact Time | 1.0 Seconds |
   | Interact Text | Build a Barrel |
   | Disable After Use | On |
   | Key Items Required | 100 |
   | Visible During Game | Hologram Only |
8. Configure the following event on the Conditional Button device so that when the player spends 100 Wood, the Prop Manipulator shows the barrel.

   [![](https://dev.epicgames.com/community/api/documentation/image/0f536441-ba2a-4669-9efb-97514affe147?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0f536441-ba2a-4669-9efb-97514affe147?resizing_type=fit)

   | Event | Select Device | Select Function |
   | --- | --- | --- |
   | On Activated Send Event To | Prop Manipulator | Show Prop |

You now have the basic functionality for a basic hidden prop that can be shown with a Conditional Button purchase!

### Design Tip

You can use this core functionality in many different gameplay situations. For example, showing and hiding props is useful for allowing players to unlock unique props at specific gameplay moments, or for creating custom powerups that should be hidden when the player picks them up!

## Resource-Dispensing Props

Use the Prop Manipulator to customize how a prop gives resources when hit.

In this example, you’ll create rocks that drop gold!

### Devices Used

- 2 x Prop Manipulator devices
- 1 x Player Spawner device
- 1 x Conditional Button device
- 1 x [Item Granter](https://dev.epicgames.com/documentation/fortnite/using-item-granter-devices-in-fortnite-creative) device

### Set Up the Rocks

1. Place a **Player Spawner** device.
2. Customize the Player Spawner as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/df580ddf-b136-4e0d-bd1d-f243c84f6600?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/df580ddf-b136-4e0d-bd1d-f243c84f6600?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Visible in Game | Off |
3. Place **five** **rocks** from the **Resource Prop Gallery**.
4. Place a **Prop Manipulator** device in the center of the area of rocks.
5. Customize the Prop Manipulator as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/13bf9b58-8d07-4661-a9d6-5668ed3565ea?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/13bf9b58-8d07-4661-a9d6-5668ed3565ea?resizing_type=fit)

   [![](https://dev.epicgames.com/community/api/documentation/image/224ca66e-c33c-4a1c-af94-f5a77591fc91?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/224ca66e-c33c-4a1c-af94-f5a77591fc91?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Override Resources | On |
   | Resource Node Available | 10 |
   | Resource Node Given | 2 |
   | Resources Node Type | Gold |
   | Resource Node Depletion Mode | Restock Over Time |
   | Affect All Objects in a Zone | On |
   | Zone Width (Tiles) | 5.0 |
   | Zone Depth (Tiles) | 5.0 |
   | Modify Prop Health | Yes |
   | Is Prop Invulnerable | Yes |
6. Place another much larger rock in the same area.
7. Place a **Prop Manipulator** device connected to the rock.
8. Customize the Prop Manipulator as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/af177189-c8a2-4005-849c-a7e51f08598f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/af177189-c8a2-4005-849c-a7e51f08598f?resizing_type=fit)

   [![](https://dev.epicgames.com/community/api/documentation/image/2cd6a681-f9c1-4b43-9749-0ae730fb9b18?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2cd6a681-f9c1-4b43-9749-0ae730fb9b18?resizing_type=fit)

   | Option | Value | Description |
   | --- | --- | --- |
   | Start Hidden | On |  |
   | Override Resources | On |  |
   | Resource Node Available | 100 |  |
   | Resource Node Given | 5 |  |
   | Resource Node Type | Gold |  |
   | Priority | 1 | This ensures that the prop is affected by this Prop Manipulator instead of the previous one. |
   | Modify Prop Health | Yes |  |
   | Is Prop Invulnerable | Yes |  |

### Configure the Purchases

1. Place a **Conditional Button** and register **Gold** to the device.
2. Customize the Conditional Button as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/0617d687-2fb7-4571-af3f-76296e39b076?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/0617d687-2fb7-4571-af3f-76296e39b076?resizing_type=fit)
3. Configure the following event on the Conditional Button so that when the player spends 50 Gold, they unlock the ability to harvest the larger rock.

   | Option | Value |
   | --- | --- |
   | Interact Text | Unlock the Big Stone! |
   | Key Items Required | 50 |
4. Place an **Item Granter** and register a **Jewel** to the device.
5. Place another Conditional Button.
6. Customize the Conditional Button as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/d82960c6-3bd3-49dc-8c9b-05466f41cf85?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d82960c6-3bd3-49dc-8c9b-05466f41cf85?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Interact Text | Buy the Jewel! |
   | Key Items Required | 150 |
7. Configure the following event on the Conditional Button so that when the player spends 150 Gold, they receive the Jewel!

   [![](https://dev.epicgames.com/community/api/documentation/image/680fbced-12cf-4cfe-9b97-a3660655ca66?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/680fbced-12cf-4cfe-9b97-a3660655ca66?resizing_type=fit)

   | Event | Select Device | Select Function |
   | --- | --- | --- |
   | On Activated Send Event To | Item Granter | Grant Item |

### Modify Island Settings

Make the following modifications to the island settings.

You now have the functionality for a system that overrides prop resource settings!

### Design Tip

In this example, you used the priority setting to decide which Prop Manipulator a prop would be affected by when it was touched by multiple Prop Manipulators. This functionality can be very helpful when designing complicated systems with multiple Prop Manipulators doing different things to different props!

## Build an Aim-Training Game!

The Prop Manipulator can send events when props are damaged or destroyed. Use this for unique damage triggers!

### Devices Used

- 5 x Prop Manipulator devices
- 1 x Player Spawner device
- 1 x Item Granter device
- 1 x [Random Number Generator](https://dev.epicgames.com/documentation/fortnite/using-random-number-generator-devices-in-fortnite-creative) device
- 5 x [Trigger](https://dev.epicgames.com/documentation/fortnite/using-trigger-devices-in-fortnite-creative) devices
- 2 x [Score Manager](https://dev.epicgames.com/documentation/fortnite/using-score-manager-devices-in-fortnite-creative) devices
- 1 x [Timer](https://dev.epicgames.com/documentation/fortnite/using-timer-devices-in-fortnite-creative) device
- 1 x [Button](https://dev.epicgames.com/documentation/fortnite/using-button-devices-in-fortnite-creative) device

### Set Up the Basic Gameplay

### Configure the Targets

1. Place a **Random Number Generator** device. This device will randomly select the next target.
2. Customize the Random Number Generator as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/f56b2f70-0e70-4bd0-9a7b-b270e7ab6173?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f56b2f70-0e70-4bd0-9a7b-b270e7ab6173?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Value Limit 2 | 5 |
   | Roll Time | Instant |
   | Pick Each Number Once | Yes (Reset on Game Start) |
   | Zone Direction | Forward |
   | Length | 2.5 |
   | Visible During Game | No |
3. Place a **Trigger** device in the first sequencer area of the Random Number Generator.
4. Customize the Trigger as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/f908d17a-a6f0-4248-8788-08fb54afdfeb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f908d17a-a6f0-4248-8788-08fb54afdfeb?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Visible In Game | Off |
   | Triggered by Player | Off |
   | Triggered by Vehicles | Off |
   | Triggered by Water | Off |
   | Trigger VFX | Off |
   | Trigger SFX | Off |
5. Place a sphere from the Primitive Shapes Gallery in the sky in front of the Player Spawner device.
6. Place a Prop Manipulator device connected to the sphere.
7. Customize the Prop Manipulator as follows:
8. Configure the following event on the Trigger device so that when it’s triggered by the Random Number Generator, it shows the sphere.

   [![](https://dev.epicgames.com/community/api/documentation/image/6692cfa3-692b-44fa-af84-6cb0a99c7823?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6692cfa3-692b-44fa-af84-6cb0a99c7823?resizing_type=fit)

   | Event | Select Device | Select Function |
   | --- | --- | --- |
   | On Triggered Send Event To | Target Prop Manipulator 1 | Show Props |
9. Configure the following events on the Prop Manipulator so that when it's shot, it hides itself and shows a new random target.

   [![](https://dev.epicgames.com/community/api/documentation/image/612d96d4-febd-462f-833a-7f3fd1ca8ceb?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/612d96d4-febd-462f-833a-7f3fd1ca8ceb?resizing_type=fit)

   | Event | Select Device | Select Function |
   | --- | --- | --- |
   | On Damaged Send Event To | Target Prop Manipulator 1 | Hide Props |
   | On Damaged Send Event To | Random Number Generator | Activate |
10. Duplicate and place the sphere, Trigger, and Prop Manipulator together four more times.
11. Place the Triggers in each of the sequencer spaces of the Random Number Generator.
12. Place each of the sphere and Prop Manipulator pairs spread in the sky in front of the Player Spawner.

### Configure the Score and Game Flow

1. Place a **Score Manager** device.
2. Configure the following functions on the Score Manager so that when a target is hit, the player is awarded a point.

   [![](https://dev.epicgames.com/community/api/documentation/image/7dabf4b1-54d1-4398-9936-23147b7dd254?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7dabf4b1-54d1-4398-9936-23147b7dd254?resizing_type=fit)

   | Function | Select Device | Select Event |
   | --- | --- | --- |
   | Activate When Receiving From | Target Prop Manipulator 1-5 | On Damaged |
3. Place another Score Manager. This Score Manager will reset the player’s score when starting a new training session.
4. Customize the Score Manager as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/3efce931-29eb-4e40-a838-140d4ec0fad2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3efce931-29eb-4e40-a838-140d4ec0fad2?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Score Value | 0 |
   | Score Award Type | Set |
5. Place a **Timer** device.
6. Customize the Timer as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/64004633-9124-4dbb-ad5d-5d09636843fc?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/64004633-9124-4dbb-ad5d-5d09636843fc?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Duration | 15.0 Seconds |
   | Can Interact | No |
   | Completion Behavior | Reset |
   | Visible During Game | Hidden |
   | Timer Color | White |
   | Display Time In | Seconds Only |
7. Configure the following event on the Timer so that when the training session ends, all of the targets are hidden.

   [![](https://dev.epicgames.com/community/api/documentation/image/fb3c7034-2182-4e55-a65a-6cfa7b20a941?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fb3c7034-2182-4e55-a65a-6cfa7b20a941?resizing_type=fit)

   | Event | Select Device | Select Function |
   | --- | --- | --- |
   | On Success Send Event To | Target Prop Manipulator 1-5 | Hide Props |
8. Place a Button device in front of the Player Spawner.
9. Customize the Button as follows:

   [![](https://dev.epicgames.com/community/api/documentation/image/cf1538df-4a16-4b92-ae12-1558bf960941?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cf1538df-4a16-4b92-ae12-1558bf960941?resizing_type=fit)

   | Option | Value |
   | --- | --- |
   | Interact Time | 1.0 Second |
   | Reset Delay | 15.0 Seconds |
   | Interaction Text | Start Aim Training |
   | Visible During Game | No |
   | Interaction Radius | 2.0 Meters |
10. Configure the following event on the Button so that when the player presses it, it resets their score, starts the Timer, and shows the first target with the Random Number Generator.

    [![](https://dev.epicgames.com/community/api/documentation/image/96e93886-1321-4766-a0d9-3f9f23348019?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/96e93886-1321-4766-a0d9-3f9f23348019?resizing_type=fit)

    | Event | Select Device | Select Function |
    | --- | --- | --- |
    | On Interact Send Event To | Random Number Generator | Activate |
    | On Interact Send Event To | Reset Score Manager | Activate |
    | On Interact Send Event To | Timer Device | Sta |

You now have the core functionality for an aim-training game!

### Design Tip

This example could easily be extended in a number of ways.

From a gameplay perspective, try adding different types of targets that award different points, and put the higher point targets further away, or increase the game’s polish by adding additional VFX and SFX when hitting a target with the VFX Spawner and Audio Player, respectively.
