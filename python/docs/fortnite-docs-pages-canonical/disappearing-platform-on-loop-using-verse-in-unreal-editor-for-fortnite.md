## https://dev.epicgames.com/documentation/en-us/fortnite/disappearing-platform-on-loop-using-verse-in-unreal-editor-for-fortnite

# Disappearing Platform on Loop

Use Verse to create a platform that appears and disappears periodically.

![Disappearing Platform on Loop](https://dev.epicgames.com/community/api/documentation/image/cd2b7ca9-a992-4c8a-898e-f4f95a299660?resizing_type=fill&width=1920&height=335)

Platforms that appear and disappear periodically are a staple of platforming game modes like obstacle courses. They require players to time their jumps to navigate to the next platform, and if they miss, they'll fall and have to start over.

By following this tutorial, you'll learn how to use **Verse** in **Unreal Editor for Fortnite** (**UEFN**) to create a platform that appears and disappears on a loop. The [complete script](https://dev.epicgames.com/documentation/fortnite/disappearing-platform-on-loop-using-verse-in-unreal-editor-for-fortnite) is included at the end of this tutorial for reference.

## Verse Language Features Used

- loop: The platform alternates between being visible and invisible until the game ends. This example uses the Verse `loop` expression to continuously run this behavior.

## Verse APIs Used

- [`Sleep()`](https://dev.epicgames.com/documentation/en-us/uefn/verse-api/versedotorg/simulation/sleep): With the `Sleep()` function, you can choose how long the platform will be in its invisible and visible states.
- [Editable Properties](https://dev.epicgames.com/documentation/fortnite/editable-properties-in-verse): Two device properties are exposed to UEFN so you can customize them in the editor — a `creative_prop` reference for the platform and a `ToggleDelay` for the `Sleep()` function call.

### Setting Up the Level

This tutorial uses the [Verse Starter Template](verse-starter-template-in-unreal-editor-for-fortnite) as its starting point. To get started, initialize a new project from the **Verse Device** feature example.

[![Initialize Starter Template](https://dev.epicgames.com/community/api/documentation/image/c97f9f48-218d-404a-92cb-7d729c266ee0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c97f9f48-218d-404a-92cb-7d729c266ee0?resizing_type=fit)

This example uses the following props and devices:

- 1 x [**Player Spawn Pad device**](https://www.fortnite.com/creative/docs/using-player-spawner-devices-in-fortnite-creative): This device defines where the player spawns at the start of the game.
- 3 x **Creative Prop**: Creative props have several behaviors you can call with Verse, such as `Hide()` and `Show()` to toggle the platform's visibility and collision. This tutorial uses the **Airborne Hoverplatform A** as the player-interactable platform, but feel free to change this to suit the needs of your experience.

Follow these steps to set up your level:

### Creating the Verse Device

This example uses a [Verse-authored device](https://dev.epicgames.com/documentation/fortnite/verse-glossary#verse-authored-device) to define the behavior that toggles platform visibility. Follow these steps to create your Verse device and place it in the level.

### Editing the Device Properties in UEFN

This section shows how to expose two device properties to UEFN so you can customize them in the editor:

- A `creative_prop` reference to the Creative Prop that you placed in the level.
- A [float](https://dev.epicgames.com/documentation/fortnite/verse-glossary) [constant](https://dev.epicgames.com/documentation/fortnite/verse-glossary#constant) to store how long the platform should be invisible/visible, named `ToggleDelay`.

Follow these steps to expose these properties to the editor from the **looping_disappearing_platform** device you created in the previous section.

1. Open [Verse Explorer](https://dev.epicgames.com/documentation/fortnite/verse-explorer-user-interface-reference-in-unreal-editor-for-fortnite) and double-click **looping_disappearing_platform.verse** to open the script in [Visual Studio Code](https://dev.epicgames.com/documentation/fortnite/verse-glossary#visual-studio-code).
2. To the `looping_disappearing_platform` class definition, add the following fields:

   - An editable `float` named `ToggleDelay`. This represents the time between toggling between visible and invisible. [Initialize](https://dev.epicgames.com/documentation/fortnite/verse-glossary#initialize) this [value](https://dev.epicgames.com/documentation/fortnite/verse-glossary#value) to `2.0`, or two seconds.

     Verse

     ```
       # The amount of time to wait before toggling visiblity of the platform.
       @editable
       ToggleDelay:float = 2.0
     ```

      # The amount of time to wait before toggling visiblity of the platform.
     @editable
     ToggleDelay:float = 2.0
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
3. Your `looping_disappearing_platform` class fields should now look like this:

   Verse

   ```
        using { /Fortnite.com/Devices }
        using { /Verse.org/Simulation }
        using { /UnrealEngine.com/Temporary/Diagnostics }
   		
        # See https://dev.epicgames.com/documentation/en-us/uefn/create-your-own-device-in-verse for how to create a verse device.
   		
        # A Verse-authored creative device that can be placed in a level
        looping_disappearing_platform := class(creative_device):
   		
            # The amount of time to wait before toggling visiblity of the platform.
   ```

   It's helpful to use the `@editable` attribute to expose values like `ToggleDelay` to the editor from your scripts. This lets you customize their values in UEFN without having to rebuild Verse code each time, so you can iterate quickly and find values that fit your gameplay experience.
4. Save the script in Visual Studio Code and compile your code to update the **looping_disappearing_platform** device in the level.

   [![Click Build Verse Code to compile your code](https://dev.epicgames.com/community/api/documentation/image/a1dcaf07-4702-48c7-a6b2-fbb47e1e9da1?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/a1dcaf07-4702-48c7-a6b2-fbb47e1e9da1?resizing_type=fit)
5. In the **Outliner** panel in UEFN, select the **looping_disappearing_platform** device to open its **Details** panel.

   [![Select looping_disappearing_platform in the Outliner to open its Details panel](https://dev.epicgames.com/community/api/documentation/image/07955732-3483-4cb6-aefa-1e613cc5cf7a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/07955732-3483-4cb6-aefa-1e613cc5cf7a?resizing_type=fit)
6. In the **Details** panel under **Looping Disappearing Platform**:

   - Set **DisappearingPlatform** to **LoopingDisappearingPlatform** (the Creative Prop you added to the level) by clicking on the **object picker** and selecting the Creative Prop in the viewport, or searching for the **LoopingDisappearingPlatform** in the search bar.
   - Set **ToggleDelay** to the number of seconds you want the platform to be visible/invisible. This value defaults to **2.0** since this is the value you defined earlier.

### Hiding and Showing the Platform

Now that you've set up the level and devices, you can add logic to show and hide the platform. Follow these steps to add this behavior to the **looping_disappearing_platform** device:

When you playtest your level, your platform should appear and disappear every two seconds for as long as the game is running.

## Complete Script

The following code is the complete script for making a platform disappear and appear on a loop.

Verse

```
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# See https://dev.epicgames.com/documentation/en-us/uefn/create-your-own-device-in-verse for how to create a verse device.

# A Verse-authored creative device that can be placed in a level
looping_disappearing_platform := class(creative_device):

    # The amount of time to wait before toggling visiblity of the platform.
```

## On Your Own

By completing this tutorial, you've learned how to create a device using Verse that toggles the visibility of a platform for as long as the game runs.

Using what you've learned, try the following:

- Duplicate the setup with the **looping_disappearing_platform** device and Prop, and try different `ToggleDelay` timings to create a longer series of platforms.
- Apply the same concepts to periodically call functions on other objects, such as the [Prop Mover device](https://www.fortnite.com/en-US/creative/docs/using-prop-mover-devices-in-fortnite-creative).
