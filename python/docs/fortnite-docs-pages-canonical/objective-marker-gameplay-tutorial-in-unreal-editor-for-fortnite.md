## https://dev.epicgames.com/documentation/en-us/fortnite/objective-marker-gameplay-tutorial-in-unreal-editor-for-fortnite

# Moving Objective Marker

Use Verse to create a moving objective marker.

![Moving Objective Marker](https://dev.epicgames.com/community/api/documentation/image/73b3dd37-677b-4a54-8633-cc445250a113?resizing_type=fill&width=1920&height=335)

Objective markers are used in many games to guide a player to the next goal or point of interest. In this tutorial, you will learn how to make a reusable objective marker with the [Map Indicator device](https://www.fortnite.com/en-US/creative/docs/using-map-indicator-devices-in-fortnite-creative) and Verse.

## Verse Language Features Used

- struct: You can group [variables](https://dev.epicgames.com/documentation/fortnite/verse-glossary#variable) of different [types](https://dev.epicgames.com/documentation/fortnite/verse-glossary#type) in a [struct](https://dev.epicgames.com/documentation/fortnite/verse-glossary).
- **Extension method**: A special type of [function](https://dev.epicgames.com/documentation/fortnite/verse-glossary) that acts like a [member](https://dev.epicgames.com/documentation/fortnite/verse-glossary#member) of an existing [class](https://dev.epicgames.com/documentation/fortnite/verse-glossary) or type, but does not require the creation of a new type or [subclass](https://dev.epicgames.com/documentation/fortnite/verse-glossary). In this guide, you will be creating an extension [method](https://dev.epicgames.com/documentation/fortnite/verse-glossary#method) for struct.
- named argument: An [argument](https://dev.epicgames.com/documentation/fortnite/verse-glossary#argument) that is passed to a [function call](https://dev.epicgames.com/documentation/fortnite/verse-glossary#function-call) with its [parameter](https://dev.epicgames.com/documentation/fortnite/verse-glossary#parameter) name specified.

## Verse APIs Used

- [creative_prop API](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_prop): The `creative_prop` API provides methods for prop movement.
- [Editable Properties](https://dev.epicgames.com/documentation/fortnite/editable-properties-in-verse): Several properties are used to both reference devices and update variable [values](https://dev.epicgames.com/documentation/fortnite/verse-glossary#value) for quick testing.

## Instructions

Follow these steps to learn how to set up a single objective marker device that can move to multiple objectives or points of interest. The complete scripts are included at the end of this guide for reference.

### Setting Up the Level

This example uses the following props and devices.

- 1 x Building Prop: A [prop](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#prop) that will be used to move the Map Indicator device.
- 1 x [Map Indicator device](https://www.fortnite.com/en-US/creative/docs/using-map-indicator-devices-in-fortnite-creative): A device that will display custom markers on the minimap and overview map.
- 1 x [Player Spawn Pad device](https://www.fortnite.com/en-US/creative/docs/using-player-spawn-pad-devices-in-fortnite-creative): Add this close to the prop so the player will spawn near it.

### Using the Prop API

The first step to getting a device moving with Verse is moving a prop with the Prop API. Follow these steps to move a prop around your level.

1. [Create a new Verse device](https://dev.epicgames.com/documentation/fortnite/create-your-own-device-using-verse-in-unreal-editor-for-fortnite) named **objective_coordinator_device**.
2. Under the default `using` expressions at the top of the Verse file, add a `using` expression for the [SpatialMath module](https://dev.epicgames.com/documentation/fortnite/verse-api/unrealenginedotcom/temporary/spatialmath). This module contains code you will reference to move props.

   Verse

   ```
        using { /UnrealEngine.com/Temporary/SpatialMath }
   ```

    using { /UnrealEngine.com/Temporary/SpatialMath }
3. Add two editable properties:

   - A `creative_prop` constant named `RootProp` to store a reference to the moving prop.
   - A `transform` constant named `Destination` to store the location the prop will be moving to.

     Verse

     ```
       objective_coordinator_device<public> := class<concrete>(creative_device):

           @editable
           RootProp<public> : creative_prop = creative_prop{}

           @editable
           Destination<public> : transform = transform{}
     ```

      objective_coordinator_device&lt;public&gt; := class&lt;concrete&gt;(creative_device):
     @editable
     RootProp&lt;public&gt; : creative_prop = creative_prop{}
     @editable
     Destination&lt;public&gt; : transform = transform{}
4. If you run this code and drag your **objective_coordinator_device** into your level, you will see the two properties in the **Details** panel.
5. The `TeleportTo[]` method is what actually moves the prop. Call it within an [if expression](https://dev.epicgames.com/documentation/fortnite/verse-glossary#if-expression) and use [square brackets](https://dev.epicgames.com/documentation/fortnite/verse-glossary#brackets) instead of parentheses because `TeleportTo[]` is a failable expression. The `if` creates a [failure context](https://dev.epicgames.com/documentation/fortnite/verse-glossary#failure-context).

   Verse

   ```
        if(RootProp.TeleportTo[Destination.Translation, Destination.Rotation]):
            Print("Prop move successful")
        else:
            Print("Prop move failed")
   ```

    if(RootProp.TeleportTo[Destination.Translation, Destination.Rotation]):
   Print(&quot;Prop move successful&quot;)
   else:
   Print(&quot;Prop move failed&quot;)
6. The arguments for `TeleportTo[]` are **Translation** and **Rotation**. Both of these come from your **Destination** property.
7. Back in the editor, drag in a prop from **Fortnite > Galleries > Props** in the **Content Browser**. The one used in this guide is called **Coastal Buoy 02B**, but anything from the Props folder should work.
8. Select your **objective coordinator device** in the **Outliner**. In the **Details** panel, set **RootProp** to your prop. In this example, RootProp is set to Coastal Buoy 02B.

   [![Select visible prop](https://dev.epicgames.com/community/api/documentation/image/fbe38511-551d-40a7-a111-2986489f4d66?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/fbe38511-551d-40a7-a111-2986489f4d66?resizing_type=fit)
9. In the **Details** panel, expand **Destination**. Because **Destination** is of type `transform`, it is made up of a **Scale**, **Rotation**, and **Translation**. To move the prop, you only need to change **Translation**, so expand that. Set the field that ends with X to **5000.0**.

   [![Enter 5000 for X Translation](https://dev.epicgames.com/community/api/documentation/image/2e3dc0d4-4d3c-4186-a359-ff915993dd1a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2e3dc0d4-4d3c-4186-a359-ff915993dd1a?resizing_type=fit)

   When testing code, it is a good idea to make big changes to values so that the effects are obvious. Small changes can make it hard to tell if your code is doing what you expect.

   Verse

   ```
    using { /Verse.org/Simulation }
    using { /Fortnite.com/Devices }
    using { /UnrealEngine.com/Temporary/SpatialMath }

    objective_coordinator_device<public> := class<concrete>(creative_device):

        @editable
        RootProp<public> : creative_prop = creative_prop{}

        # Where the marker will be moved to
   ```
10. Click **Verse**, then **Build Verse Code**, then click **Launch Session**. Finally, click **Start Game**. You should see your prop move.

### Parent and Structs

You now have a prop moving around in your level, but the real goal is moving a Map Indicator device so players can use it as a waypoint. Follow these steps to add a Building Prop and Map Indicator device to your level and attach it to the Building Prop.

You already know how to [create a device using Verse](https://dev.epicgames.com/documentation/fortnite/create-your-own-device-using-verse-in-unreal-editor-for-fortnite), but you can also create Verse files that do not have their own devices.

### Extension Methods and Named Arguments

[Declare](https://dev.epicgames.com/documentation/fortnite/verse-glossary) a single method, `MoveMarker`, that will move the `RootProp` member and its attached Map Indicator device. This method introduces two language features: extension methods and named arguments.

Verse

```
(Marker : objective_marker).MoveMarker<public>(Transform : transform, ?OverTime : float)<suspends> : void =
```

(Marker : objective_marker).MoveMarker<public>(Transform : transform, ?OverTime : float)<suspends> : void =

- **Extension methods:** You are adding the `MoveMarker()` method to the `objective_marker` struct. An extension method is declared using parentheses surrounding an identifier and type separated by a colon. In this case: `(Marker : objective_marker)`.
- **Named arguments:** The second argument `?OverTime` uses the `?` to indicate that it must be named in the `MoveMarker` function call. This helps any developer reading or writing a call to `MoveMarker` understand what the `float` argument is doing.

`MoveMarker()` will call one of two methods from the Prop API: `TeleportTo[]`, which you used earlier, or `MoveTo()`. Create an `if..else` block to test if the parameter `OverTime` is greater than `0.0`. If it is, call `MoveTo()`. This will make your objective move to its next location over period of time you specify, instead of instantly teleporting.

Verse

```
(Marker : objective_marker).MoveMarker<public>(Transform : transform, ?OverTime : float)<suspends> : void =

 if (OverTime > 0.0):
        Marker.RootProp.MoveTo(Transform.Translation, Transform.Rotation, OverTime)
    else:
        if:
            Marker.RootProp.TeleportTo[Transform.Translation, Transform.Rotation]
```

(Marker : objective_marker).MoveMarker<public>(Transform : transform, ?OverTime : float)<suspends> : void =
if (OverTime > 0.0):
Marker.RootProp.MoveTo(Transform.Translation, Transform.Rotation, OverTime)
else:
if:
Marker.RootProp.TeleportTo[Transform.Translation, Transform.Rotation]

If you compile the code now, it should succeed, but you should not see a new device in the **CreativeDevices** folder in the Content Browser. This is because **objective_marker** is a `struct`, not a class that inherits from `creative_device`.

### Updating Objective Coordinator Device

Now that you have a new type to reference, you need to update the **objective_coordinator_device** to reference it.

Compile this code and check the Details of the objective coordinator device. You should see the PickupMarker and MoveTime properties, and PickupMarker should contain RootProp and MapIndicator.

### GetPlayers() and ActivateObjectivePulse()

There is a way to give your players a little extra help getting to their next objective. It’s called an **objective pulse** and when active it shows a dotted line that moves from the player toward the **Map Indicator Device**. Follow the instructions below to add an objective pulse to your objective coordinator device.

[![Objective pulse pointing from player to objective](https://dev.epicgames.com/community/api/documentation/image/497d01d3-9b32-43fa-b0a7-9256986950a7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/497d01d3-9b32-43fa-b0a7-9256986950a7?resizing_type=fit)

The method you need to activate the objective pulse is called `ActivateObjectivePulse()` and it requires one argument of type `agent`. Start by creating the method to get the instance of `agent` representing your player character.

Back in the `OnBegin()` function, you need to make two more changes:

If you run your code now, you should see the objective pulse pointing from your character to the location of the objective marker in the level!

## Complete Scripts

### Objective_marker.verse

Verse

```
using { /Verse.org/Simulation }
using { /Fortnite.com/Devices }
using { /UnrealEngine.com/Temporary/SpatialMath }
using { /Fortnite.com/Devices/CreativeAnimation }

objective_marker<public> := struct<concrete>:

    # The prop that will be moved
    @editable
    RootProp<public> : creative_prop = creative_prop{}
```

### Objective_coordinator_device.verse

Verse

```
using { /Verse.org/Simulation }
using { /Fortnite.com/Devices }
using { /Fortnite.com/Playspaces }
using { /UnrealEngine.com/Temporary/SpatialMath }

objective_coordinator_device<public> := class<concrete>(creative_device):

    var PlayerOpt<private> : ?player = false

    @editable
```

## On Your Own

Remember that the movement code you wrote here works for any prop. If you can make a movable prop the parent of a device, that device will move with it. Try moving other props and devices, and see if you can think of other games that could make use of them.

## Next Steps

If you are using this guide to build the Pickup / Delivery game, your next step is to learn how to create the Countdown Timer feature.
