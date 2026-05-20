## https://dev.epicgames.com/documentation/en-us/fortnite/explosive-device-design-example-in-fortnite-creative

# Explosive Device Design Example

Use this simple mechanic to add flash to any island.

![Explosive Device Design Example](https://dev.epicgames.com/community/api/documentation/image/7629fe0d-0563-46f0-9827-7896151cb92e?resizing_type=fill&width=1920&height=335)

The **Explosive** device is a fun way to add action to any island.

In this design example, you'll explore a simple mechanic that you can use to add a bubbling visual effect to an explosive barrel that warns players splayers it's about to explode!

You can add this [game mechanic](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#game-mechanics) to any game or experience to give it a little flash!

## Devices Used

- 1 x [**Explosive**](using-explosive-devices-in-fortnite-creative) device
- 1 x [**VFX Creator**](using-vfx-creator-devices-in-fortnite-creative) device
- 1 x [Timer](https://dev.epicgames.com/documentation/fortnite/using-timer-devices-in-fortnite-creative) device
- 1 x [Trigger](https://dev.epicgames.com/documentation/fortnite/using-trigger-devices-in-fortnite-creative) (or other activating) device

## Build Your Own

You will set up an **explosive barrel** and create a **visual effect** to go with it. Next, you'll set up a **timer** to control the timing of the blast, then add a **trigger** to set the whole mechanic in motion!

### Place the Explosive Device

### Place a VFX Creator Device

When you place the VFX Creator device, be sure to place it on top of the barrel.

To place the device on top of the barrel, you may need to turn off the **Drops** option on the [Create mode hotkeys](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#create-mode-hotkeys) menu.

[![](https://dev.epicgames.com/community/api/documentation/image/b706f63d-5ae4-4dab-bd11-613d09196031?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b706f63d-5ae4-4dab-bd11-613d09196031?resizing_type=fit)

Select an option, then use the Drops hotkey to toggle this **On** or **Off**.

This is a context-sensitive menu, which means options change based on your current actions.

### Add a Timer Device

Time to set the timer! This will control the timing of the bubble blast.

The timer will not be visible during the game, so it doesn't matter where you place it.

### Add a Trigger Device

The final device to place is the trigger. The player will interact with the trigger, so it needs to be within the player's sight.

### Bind Devices

**Direct event binding** is how you set triggers between devices. When you set an **event** on one device, the binding automatically updates on the **function** for the bound device.

## Bonus Points!

Want to add some cool sound effects to go with the visual effects? Use the **Audio Player** device!

Add the device, pick a cool sound, then add a function that lets the Trigger device trigger the audio player!

[![](https://dev.epicgames.com/community/api/documentation/image/8a4924aa-3ae8-44ac-8a76-fe1bfc6eb6f0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8a4924aa-3ae8-44ac-8a76-fe1bfc6eb6f0?resizing_type=fit)
