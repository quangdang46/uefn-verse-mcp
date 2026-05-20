## https://dev.epicgames.com/documentation/en-us/fortnite/disappearing-platform-on-touch-using-verse-in-unreal-editor-for-fortnite

# Disappearing Platform on Touch

Create a platform using Verse that disappears when the player touches it and reappears a random number of seconds later.

![Disappearing Platform on Touch](https://dev.epicgames.com/community/api/documentation/image/332285ab-0dd9-43be-9996-59d90f6091f7?resizing_type=fill&width=1920&height=335)

Platforms that disappear when you land on them are a staple of platforming game modes like obstacle courses. They require the player to act quickly and plan where they're going so they don't fall.

By following this tutorial, you'll learn how to build a platform that disappears when the player touches it and reappears a random number of seconds later using **Verse** in **Unreal Editor for Fortnite** (**UEFN**). This example shows how to create an area where the player must jump from platform to platform to avoid falling. The [complete script](https://dev.epicgames.com/documentation/fortnite/disappearing-platform-on-touch-using-verse-in-unreal-editor-for-fortnite) is included at the end of this guide for reference.

## Verse Language Feature Used

- spawn: The `spawn` [expression](https://dev.epicgames.com/documentation/fortnite/verse-glossary#expression) is used to [call](https://dev.epicgames.com/documentation/fortnite/verse-glossary#call) the [asynchronous](https://dev.epicgames.com/documentation/fortnite/verse-glossary#async) [function](https://dev.epicgames.com/documentation/fortnite/verse-glossary) that makes the platform reappear after a random number of seconds.

## Verse APIs Used

- `Sleep()`: The `Sleep()` API is used to insert the delays between the platform disappearing and reappearing again after a random amount of time.
- `GetRandomFloat()`: The `GetRandomFloat()` API is used to compute a random amount of time before the platform reappears.
- [Editable Properties](https://dev.epicgames.com/documentation/fortnite/editable-properties-in-verse): Four properties are exposed to UEFN – three floats to control the disappearance and reappear delays of the platform and the platform reference itself.
- [Device Events](https://dev.epicgames.com/documentation/fortnite/coding-device-interactions-in-verse): You'll use the Trigger device's `TriggeredEvent` to know when a player lands on the platform.

### Setting Up the Level

This tutorial uses the [Verse Starter Template](verse-starter-template-in-unreal-editor-for-fortnite) as its starting point. To get started, initialize a new project from the **Verse Device** feature example.

[![Initialize Starter Template](https://dev.epicgames.com/community/api/documentation/image/a8b94147-e7d5-4011-aafe-d9a346e5fdaf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a8b94147-e7d5-4011-aafe-d9a346e5fdaf?resizing_type=fit)

This example uses the following props and devices.

- 1 x [Player Spawn Pad device](https://www.epicgames.com/fortnite/creative/docs/using-player-spawn-pad-devices-in-fortnite-creative): This device defines where the player spawns at the start of the game.
- 4 x **Creative Prop**: Creative props have several behaviors you can call with Verse, such as `Hide()` and `Show()` to toggle the platform's visibility and collision. This tutorial uses the **Airborne Hoverplatform A** as the player-interactable platform, but feel free to change this to suit the needs of your experience.
- 4 x [Trigger device](https://dev.epicgames.com/documentation/en-us/fortnite-creative/using-trigger-devices-in-fortnite-creative): You'll use these triggers to know when a player lands on each platform.

Follow these steps to set up your level:

### Creating the Device

This example uses a [Verse-authored device](https://dev.epicgames.com/documentation/fortnite/verse-glossary#verse-authored-device) to define the behavior for making the platform disappear when the player lands on it and re-appear a random number of seconds later. Follow these steps to create this device using Verse.

### Editing the Device Properties in UEFN

This section shows how to expose four device properties to UEFN so you can customize them in the editor:

- A device reference to the creative object you placed in the level.
- A [float](https://dev.epicgames.com/documentation/fortnite/verse-glossary) [constant](https://dev.epicgames.com/documentation/fortnite/verse-glossary#constant), named `DisappearDelay`, to store how long to wait after the player touches the platform before hiding it.
- Two `float` constants named `DelayMin` and `DelayMax` that store the minimum and maximum amounts of time to wait before making the platform reappear. These two values define the allowed range when getting a random number.

Follow these steps to expose these properties from the **disappear_on_touch_platform** device you created in the previous section.

1. Open [Verse Explorer](https://dev.epicgames.com/documentation/fortnite/verse-explorer-user-interface-reference-in-unreal-editor-for-fortnite) and double-click **disappear_on_touch_platform.verse** to open the script in [Visual Studio Code](https://dev.epicgames.com/documentation/fortnite/verse-glossary#visual-studio-code).
2. To the `disappear_on_touch_platform` class definition, add the following fields:

   - An editable `float` named `DisappearDelay`. This is how long to wait after the player touches the platform before hiding it. [Initialize](https://dev.epicgames.com/documentation/fortnite/verse-glossary#initialize) this [value](https://dev.epicgames.com/documentation/fortnite/verse-glossary#value) to `1.0`, or one second.

     Verse

     ```
       # How long to wait after the player touches the platform before hiding it.
       @editable
       DisappearDelay:float = 1.0
     ```

      # How long to wait after the player touches the platform before hiding it.
     @editable
     DisappearDelay:float = 1.0
   - An editable `float` named `DelayMin`. This is the minimum amount of time to wait before making the platform reappear. Initialize this to `3.0`, or three seconds.

     Verse

     ```
       # The minimum amount of time to wait before making the platform reappear.
       @editable
       DelayMin:float = 3.0
     ```

      # The minimum amount of time to wait before making the platform reappear.
     @editable
     DelayMin:float = 3.0
   - An editable `float` named `DelayMax`. This is the maximum amount of time to wait before making the platform reappear. Initialize this to `4.0`, or four seconds.

     Verse

     ```
       # The maximum amount of time to wait before making the platform reappear.
       @editable
       DelayMax:float = 4.0
     ```

      # The maximum amount of time to wait before making the platform reappear.
     @editable
     DelayMax:float = 4.0
   - An editable `creative_prop` named `DisappearingPlatform`. This is the in-level platform that will disappear and appear periodically. Because your code doesn't yet have a reference to this object in the level, you'll instantiate this with an empty [archetype](https://dev.epicgames.com/documentation/fortnite/verse-glossary#archetype) `creative_prop{}`. You'll assign this reference to your floating platform later.

     Verse

     ```
       # Reference to the platform in the level.
       @editable
       DisappearingPlatform:creative_prop = creative_prop{}
     ```

      # Reference to the platform in the level.
     @editable
     DisappearingPlatform:creative_prop = creative_prop{}
   - An editable `trigger_device` named `PlatformTrigger`. You'll need the `TriggeredEvent` event from this device to know when a player lands on the platform.

     Verse

     ```
       # The zone a player enters when landing on the platform.
       @editable
       PlatformTrigger:trigger_device = trigger_device{}
     ```

      # The zone a player enters when landing on the platform.
     @editable
     PlatformTrigger:trigger_device = trigger_device{}
3. Your `disappear_on_touch_platform` class fields should look like this:

   Verse

   ```
        # A Verse-authored creative device that can be placed in a level
        disappear_on_touch_platform := class(creative_device):
   		
            # How long to wait after the player touches the platform before hiding it.
            @editable
            DisappearDelay:float = 1.0
   		
            # The minimum amount of time to wait before making the platform reappear.
            @editable
            DelayMin:float = 3.0
   ```

   It's helpful to use the `@editable` attribute to expose values like `ToggleDelay` to the editor from your scripts. This lets you customize their values in UEFN without having to rebuild Verse code each time, so you can iterate quickly and find values that fit your gameplay experience.
4. Save the script in Visual Studio Code.
5. In the UEFN toolbar, click **Verse**, and then **Build Verse Code** to update the **disappear_on_touch_platform** device in the level.
6. In the **Outliner** panel in UEFN, select the **disappear_on_touch_platform** device to open its **Details** panel.
7. In the **Details** panel under **Disappear on Touch Platform**, set **Platform** to **RecyclePlatform** (the creative prop you added to the level) by clicking on the **object picker** and selecting the platform device in the viewport.
8. Now that you have a prop referenced by your Verse device, select both devices and duplicate them multiple times in the level to create a series of platforms for the player to jump between. Each new Verse device you create should be referencing its own platform.

   [![Duplicate the Verse device and platform setup to add more to the level](https://dev.epicgames.com/community/api/documentation/image/a06b68d6-936d-4735-a8f9-b2e9d0f18c2b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a06b68d6-936d-4735-a8f9-b2e9d0f18c2b?resizing_type=fit)

### Hiding and Showing the Platform

Now that you've set up the level and devices, you can add the functionality to show and hide the platform when a player lands on it. Follow these steps to add this behavior to the `disappear_on_touch_platform` class:

### Detecting the Player Landing on the Platform

To be able to detect when the player lands on the platform, you can [subscribe](https://dev.epicgames.com/documentation/fortnite/verse-glossary#subscribe) to the `TriggeredEvent` [event](https://dev.epicgames.com/documentation/fortnite/verse-glossary) that the `trigger_device` class exposes. The trigger only sends the `TriggeredEvent` when a player walks over it. Because you set **Times Can Trigger** to one, you'll need to call `Reset()` on the trigger to reset its state and allow it to send the `TriggeredEvent` again.

Follow these steps to detect when the player touches the platform, and use the code you wrote in the previous section to make the platform hide and reappear in response.

Although you need to hide the platform when a player lands on it, you can't add the code for hiding and showing the platform directly to the `OnPlayerTouch()` method. The `Sleep()` function can only be called in an asynchronous context, and you can't add the `suspends` specifier to `OnPlayerTouch()` because `TriggeredEvent` doesn't allow asynchronous functions as its event handler. Instead, you can use spawn to call an asynchronous function from `OnPlayerTouch()`. Follow these steps to add your asynchronous function.

## Complete Script

The following code is the complete script for making a platform disappear when the player lands on the platform and reappear after a random number of seconds.

Verse

```
using { /Fortnite.com/Devices }
using { /Verse.org/Random }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# See https://dev.epicgames.com/documentation/en-us/uefn/create-your-own-device-in-verse for how to create a verse device.
# A Verse-authored creative device that can be placed in a level
disappear_on_touch_platform := class(creative_device):

    # How long to wait after the player touches the platform before hiding it.
```

## On Your Own

By completing this tutorial, you've learned how to create a device using Verse that makes a platform disappear when the player lands on it and reappears a random number of seconds later.

Using what you've learned, try the following:

- Play around with the sizes and positions of the platforms to create an interesting challenge.
- In this example the player doesn't score any points and nothing happens when they fall. Can you think of how you'd implement a scoring system and a loss condition?
