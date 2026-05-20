## https://dev.epicgames.com/documentation/en-us/fortnite/synchronized-disappearing-platforms-using-verse-in-unreal-editor-for-fortnite

# Synchronized Disappearing Platforms

Use Verse to create a series of platforms that appear and disappear in sequence using one device.

![Synchronized Disappearing Platforms](https://dev.epicgames.com/community/api/documentation/image/ac4a6bfe-bd43-4eb0-b52a-f4b62bc820eb?resizing_type=fill&width=1920&height=335)

A series of disappearing platforms is a staple of platforming game modes like obstacle courses. These require players to time their jumps across a series of platforms, or they'll fall and have to start over.

By following this tutorial, you'll learn how to create a series of platforms that sequentially appear and disappear using one device created with Verse in **Unreal Editor for Fortnite** (**UEFN**).

|  |  |
| --- | --- |
|  |  |

## Verse Language Features Used

- array: With the [array](https://dev.epicgames.com/documentation/fortnite/verse-glossary) [type](https://dev.epicgames.com/documentation/fortnite/verse-glossary#type), you can store platform references together for quick access and to avoid code duplication.
- loop: The platform cycle of platforms appearing and disappearing should start when the game begins and run continuously. This example shows how to create this behavior with the Verse `loop` [expression](https://dev.epicgames.com/documentation/fortnite/verse-glossary#expression).
- block: With the `block` expression, you can group multiple expressions together so they are [executed](https://dev.epicgames.com/documentation/fortnite/verse-glossary#execute) sequentially.
- for: With the `for` expression, you can iterate over each platform in your array.
- sync: With the `sync` expression and [structured concurrency](https://dev.epicgames.com/documentation/fortnite/verse-glossary#structured-concurrency), you can run multiple async expressions concurrently.

## Verse APIs Used

- `Sleep()`: With the `Sleep()` API, you can choose how long the platforms will be in their invisible and visible states.
- [Editable Properties](https://dev.epicgames.com/documentation/fortnite/editable-properties-in-verse): several[Verse-authored device](https://dev.epicgames.com/documentation/fortnite/verse-glossary#verse-authored-device) properties are exposed to UEFN so you can customize them in the Editor – three delays for the platforms' behavior and four device references to the platforms.

## Instructions

Follow these steps to learn how to set up a series of platforms that disappear and appear periodically. The [complete script](https://dev.epicgames.com/documentation/fortnite/synchronized-disappearing-platforms-using-verse-in-unreal-editor-for-fortnite) is included at the end of this guide for reference.

### Setting Up the Level

This tutorial uses the [Verse Starter Template](verse-starter-template-in-unreal-editor-for-fortnite) as its starting point. To get started, initialize a new project from the **Verse Device** feature example.

[![Initialize Starter Template](https://dev.epicgames.com/community/api/documentation/image/910c64b1-e88b-46c4-bc0b-614e0cbc34e3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/910c64b1-e88b-46c4-bc0b-614e0cbc34e3?resizing_type=fit)

This example uses the following props and devices.

- 1 x [Player Spawn Pad Device](https://www.fortnite.com/creative/docs/using-player-spawner-devices-in-fortnite-creative): This device defines where the player spawns at the start of the game.
- 6 x **Creative Prop**: Creative props have several behaviors you can call with Verse, such as `Hide()` and `Show()` to toggle the platform's visibility and collision. This tutorial uses the **Airborne Hoverplatform A** as the player-interactable platform, but feel free to change this to suit the needs of your experience.

Follow these steps to set up your level:

### Creating the Device

This example uses a [Verse-authored device](https://dev.epicgames.com/documentation/fortnite/verse-glossary#verse-authored-device) to define the behavior for toggling the visibility of the platforms. Follow these steps to create this device using Verse.

### Editing the Device Properties in UEFN

This section shows how to expose device properties to UEFN so you can customize them in the editor:

- Three `float` constants to store how long the platforms should be invisible/visible named `HeadStart`, `AppearDelay`, and `DisappearDelay`.
- Devices references to the creative objects you placed in the level.

Follow these steps to expose these properties from the **platform_series** device you created in the previous section.

1. Open [Verse Explorer](https://dev.epicgames.com/documentation/fortnite/verse-explorer-user-interface-reference-in-unreal-editor-for-fortnite) and double-click **platform_series.verse** to open the script in [Visual Studio Code](https://dev.epicgames.com/documentation/fortnite/verse-glossary#visual-studio-code).
2. To the `platform_series` class definition, add the following fields:

   - An editable `float` named `HeadStart`. This represents how long to wait, in seconds, after platforms start appearing and before platforms start disappearing. Initialize this value to `2.5` or two and a half seconds.

     Verse

     ```
       # How long to wait in seconds after platforms start appearing
       # before they start disappearing.
       @editable
       HeadStart:float = 2.5
     ```

      # How long to wait in seconds after platforms start appearing
     # before they start disappearing.
     @editable
     HeadStart:float = 2.5
   - An editable `float` named `AppearDelay`. This represents how long to wait, in seconds, before the next platform appears. Initialize this value to `1.0`, or one second.

     Verse

     ```
       # How long to wait in seconds before the next platform appears.
       @editable
       AppearDelay:float = 1.0
     ```

      # How long to wait in seconds before the next platform appears.
     @editable
     AppearDelay:float = 1.0
   - An editable `float` named `DisappearDelay`. This represents how long to wait, in seconds, before the next platform disappears. Initialize this value to `1.25`, or one and a quarter seconds.

     Verse

     ```
       # How long to wait in seconds before the next platform disappears.
       @editable
       DisappearDelay:float = 1.25
     ```

      # How long to wait in seconds before the next platform disappears.
     @editable
     DisappearDelay:float = 1.25
   - An editable `creative_prop` named `DisappearingPlatform`. This is the in-level platform that will disappear and appear. Because your code doesn't yet have a reference to this object in the level, you'll instantiate this with an empty [archetype](https://dev.epicgames.com/documentation/fortnite/verse-glossary#archetype) `creative_prop{}`. You'll assign this reference to your floating platform later.

     Verse

     ```
       # The in-level platform that disappears and reappears.
       @editable
       DisappearingPlatform:creative_prop = creative_prop{}
     ```

      # The in-level platform that disappears and reappears.
     @editable
     DisappearingPlatform:creative_prop = creative_prop{}
3. Your `platform_series` class fields should look like this:

   Verse

   ```
        # A Verse-authored creative device that can be placed in a level
        platform_series := class(creative_device):
   		
        # How long to wait in seconds after platforms start appearing
        # before they start disappearing.
        @editable
        HeadStart:float = 2.5
   		
        # How long to wait in seconds before the next platform appears.
        @editable
   ```

   It's helpful to use the `@editable` attribute to expose values like `AppearDelay` to the editor from your scripts. This lets you customize their values in UEFN without having to rebuild Verse code each time, so you can iterate quickly and find values that fit your gameplay experience.
4. Save the script in Visual Studio Code.
5. In the UEFN toolbar, click **Verse**, and then **Build Verse Code** to update the **platform_series** device that's in the level.

   [![Click Build Verse Scripts to compile your code](https://dev.epicgames.com/community/api/documentation/image/cfc74781-6d57-48b2-9db7-f36dc01944f7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cfc74781-6d57-48b2-9db7-f36dc01944f7?resizing_type=fit)
6. In the **Outliner** panel in UEFN, select the **platform_series** device to open its **Details** panel.
7. In the **Details** panel under **Platform Series**, set **DisappearingPlatform** to **SynchronizedPlatform1** (the creative prop you added to the level) by clicking on the **object picker** and selecting the platform in the viewport.

### Hiding and Showing a Platform

Now that you've set up the level and the first platform, let's add the functionality to show and hide the platform. Follow these steps to add this behavior to the **platform_series** device:

### Hiding and Showing Multiple Platforms

While you could repeat the code in the previous step for every platform in the level that you want to disappear, creating an array to store all the device references is more efficient. This will let you iterate through each platform in the array, executing code on each without having to duplicate the Verse device multiple times. Follow these steps to hide and show multiple platforms:

1. In your `platform_series` class definition, change the `DisappearingPlatform` field to an array of `creative_prop` named `DisappearingPlatforms`. You'll use this array to iterate over the platforms in order. Initialize the variable with the default value `array{}`, an empty array.

   Verse

   ```
        # The in-level platforms that disappear and reappear in sequence.
        @editable
        DisappearingPlatforms:[]creative_prop = array{}
   ```

    # The in-level platforms that disappear and reappear in sequence.
   @editable
   DisappearingPlatforms:[]creative_prop = array{}
2. You can use the `for` expression to iterate over each element in the array. The `for` expression uses the `X -> Y` pattern, to give you an index-value pairing. The index is bound to the left part (`X`) and the value is bound to the right part (`Y`). In this case, `X` is the platform's number / index and `Y` is each platform reference retrieved from the array. First, create a `for` expression to iterate over each element, and get the index of each number in a variable `PlatformNumber`.

   ~~~(verse)
   # Runs when the device is started in a running game
   OnBegin<override>()<suspends>:void=
   for:
   PlatformNumber -> DisappearingPlatform:DisappearingPlatforms
   do:
   ~~~
3. Print out the number of the platform, and call `Hide()` to hide the platform. Then `Sleep()` for a `DisappearDelay` amount of seconds.

   Verse

   ```
        # For each platform in DisappearingPlatforms, make it invisible and sleep.
        for:
            PlatformNumber -&gt; DisappearingPlatform:DisappearingPlatforms
        do:
            # Hide the platform
            DisappearingPlatform.Hide()
            Print("Platform {PlatformNumber} is now hidden")
            Sleep(DisappearDelay)
   ```

    # For each platform in DisappearingPlatforms, make it invisible and sleep.
   for:
   PlatformNumber -&amp;gt; DisappearingPlatform:DisappearingPlatforms
   do:
   # Hide the platform
   DisappearingPlatform.Hide()
   Print(&quot;Platform {PlatformNumber} is now hidden&quot;)
   Sleep(DisappearDelay)
4. To show the platforms against, you'll use a second `for` expression after the first. Iterate over each platform in `DisappearingPlatforms` in the same way, except this time call `Show()` to show the platform, and `Sleep()` for an `AppearDelay` amount of seconds.

   ~~~(verse)
   # For each platform in DisappearingPlatforms, make it visible and sleep.
   for:
   PlatformNumber -> DisappearingPlatform:DisappearingPlatforms
   do:
   # Show the platform.
   DisappearingPlatform.Show()
   Print("Platform {PlatformNumber} is now visible")
   Sleep(AppearDelay)
   ~~~
5. When writing code, it's a good idea to put code you might want to reuse into separate functions. This lets you call the code from different contexts, and avoid having to rewrite the same code over and over. Depending on your experience you may want to hide and show the platforms during different situations, so you'll make functions to handle each of these. Add two new functions named `HideAllPlatforms()` and `ShowAllPlatforms()` to your `platform_series` class definition. Move the `for` expression that handles hiding the platforms into `HideAllPlatforms()`, and the expression that handles showing the platforms into `ShowAllPlatforms()`. Since you're using the `Sleep()` function, these functions need to be asynchronous, so add the `<suspends>` modifier to each. Then in `OnBegin()`, call `HideAllPlatforms()`, then `ShowAllPlatforms()`.

   Verse

   ```
        # Runs when the device is started in a running game
        OnBegin<override>()<suspends>:void=
            HideAllPlatforms()
            ShowAllPlatforms()

        HideAllPlatforms()<suspends>:void=
            # For each platform in DisappearingPlatforms, make it invisible and sleep.
            for:
                PlatformNumber -> DisappearingPlatform:DisappearingPlatforms
            do:
   ```
6. As it stands, this code will only run once. To make the platforms disappear and reappear for as long as the game is running, you can use the loop expression to repeat this behavior. To handle this, add a `loop` expression to `OnBegin()` that includes the calls to `HideAllPlatforms()` and `ShowAllPlatforms()`In this example, you want to toggle the visibility of the platforms for as long as the game is running, so there's no need to add a `break` expression to exit the `loop`.

   Verse

   ```
        # Runs when the device is started in a running game
        OnBegin<override>()<suspends>:void=
            loop:
                # Hide all platforms.
                HideAllPlatforms()

                # Show all platforms.
                ShowAllPlatforms()
   ```

    # Runs when the device is started in a running game
   OnBegin&lt;override&gt;()&lt;suspends&gt;:void=
   loop:
   # Hide all platforms.
   HideAllPlatforms()
   # Show all platforms.
   ShowAllPlatforms()

   If you run this code, the platforms will all disappear in sequence first and then all reappear in the same order, repeating until the game ends.
7. Save your code and compile it. In the **Outliner** panel in UEFN, select the **platform_series** device to open its **Details** panel.
8. In the **Details** panel under **DisappearingPlatforms**, add an array element for each platform in the level. Add new elements to the array with the "Add Element" button, then click on the **object picker** and select the creative prop in the viewport. Make sure that the order of this array matches the order you want to iterate over:

   [![Assign the seven platforms in the level to properties on the platform_series device](https://dev.epicgames.com/community/api/documentation/image/2757d33c-0914-4c7a-82e9-87a9d4413a1b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2757d33c-0914-4c7a-82e9-87a9d4413a1b?resizing_type=fit)

Now if you run this code, the platforms will all disappear in sequence first then reappear in the same order, repeating until the game ends.

### Synchronize the Platforms Disappearing and Reappearing

To add more urgency as the player jumps across the tiles, you can make the platforms start disappearing while platforms later in the sequence are still appearing. That way, the player will have to rush across the series or they'll fall. To create this behavior, both routines (`ShowAllPlatforms()` and `HideAllPlatforms()`) must run at the same time, with the second lagging behind the first, so that the player has a head start to jump to the next platform before it disappears.

Follow these steps to make the platforms all hide and show at the same time.

When you playtest the level now, the platforms start disappearing in sequence while the platforms later in the sequence reappear, and this pattern repeats for as long as the game is running.

## Complete Script

The following code is the complete script for making a series of platforms that appear and disappear in sequence.

Verse

```
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

# See https://dev.epicgames.com/documentation/en-us/uefn/create-your-own-device-in-verse for how to create a verse device.

# A Verse-authored creative device that can be placed in a level
platform_series := class(creative_device):

    # How long to wait in seconds after platforms start appearing
```

## On Your Own

By completing this tutorial, you've learned how to create a device using Verse that toggles the visibility of a series of platforms for as long as the game runs.

Using what you've learned, try the following:

- Change the order the platforms appear and disappear.
- Apply the same concepts to periodically call functions on other device types, such as the [Prop Mover Device](https://www.fortnite.com/creative/docs/using-prop-mover-devices-in-fortnite-creative).
