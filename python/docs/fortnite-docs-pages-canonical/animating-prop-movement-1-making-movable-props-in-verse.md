## https://dev.epicgames.com/documentation/en-us/fortnite/animating-prop-movement-1-making-movable-props-in-verse

# 1. Making Movable Props With Verse

Learn how to use Verse to animate prop movement with Verse to build a Fall Guys obstacle course.

![1. Making Movable Props With Verse](https://dev.epicgames.com/community/api/documentation/image/4e26f0f0-a30a-4d70-94c8-f619440cc163?resizing_type=fill&width=1920&height=335)

## Setting Up The Level

To get started, initialize a new project from the **Fall Guys Starter** island template. This starter island contains a ready-made course for you to navigate through, and you’ll customize it with movement in this tutorial.

[![Initialize a level from the Fall Guys starter Template](https://dev.epicgames.com/community/api/documentation/image/3fe4fbae-4946-4ded-bccd-0ecccc385a5e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3fe4fbae-4946-4ded-bccd-0ecccc385a5e?resizing_type=fit)

### Defining Props that Move

Before you can start moving your props, you need to define what a movable prop is. You could use a Verse device to move a prop directly, but this might get tricky if you wanted to move multiple props at once. Instead, you’ll define an abstract `movable_prop` class. This will contain the prop you want to move and several other values that you’ll use to customize the logic and timing of your movement.

Follow the steps below to define your movable prop:

1. Create a new Verse class named `movable_prop` using **Verse Explorer**. Because this is a Verse class and not a device, create this file using **Create Empty**. And since this will be the abstract class that you’ll subclass different types of movable props from, add the `<abstract>` specifier to this class. To learn how to create a new class in Verse, see [Modify and Run Your First Verse Program](https://dev.epicgames.com/documentation/fortnite/modify-and-run-your-first-verse-program-in-unreal-editor-for-fortnite).

   Verse

   ```
        # Defines a Creative prop that moves to a target or location using animation.
        movable_prop<public> := class<abstract>():
   ```

    # Defines a Creative prop that moves to a target or location using animation.
   movable_prop&lt;public&gt; := class&lt;abstract&gt;():
2. Add the `using { /Fortnite.com/Devices }`, `using { /Verse.org/Simulation }`, and `using { /UnrealEngine.com/Temporary/SpatialMath }` import paths to the top of your file. You’ll need to import these module to handle the math that makes your props move.
3. Each of the fields in this class will also include a `ToolTip`. Adding a `ToolTip` message to your editable fields displays a tooltip when you mouse over the field in UEFN. All the tooltips used in this class are included below. You can copy and paste these tooltips, or define your own.

   Verse

   ```
        using { /Fortnite.com/Devices }
        using { /Verse.org/Simulation }
        using { /UnrealEngine.com/Temporary/SpatialMath }
   		
        MoveDurationTip<localizes>:message = "The amount of time the prop takes to move to its destination."
        MoveEaseTypeTip<localizes>:message = "The animation easing applied to the movement."
        MoveEndDelayTip<localizes>:message = "The delay after the movement finishes."
        MoveOnceAndStopTip<localizes>:message = "Whether the RootProp should stop in place after it finishes moving."
        MoveStartDelayTip<localizes>:message = "The delay before the movement starts."
        MoveTargetsTip<localizes>:message = "The array of CreativeProp to move toward. These targets can be children of the RootProp."
   ```
4. Define the fields each movable prop needs. To your `movable_prop` class definition, add the following fields:

   1. An editable `creative_prop` named `RootProp`. This is the Creative prop you’ll move around during gameplay.

      Verse

      ```
                               # The Creative prop associated with this class.
                               # This should be the root prop of the object you want to move.
                               @editable {ToolTip := RootPropTip}
                               RootProp:creative_prop = creative_prop{}
      ```

       # The Creative prop associated with this class.
      # This should be the root prop of the object you want to move.
      @editable {ToolTip := RootPropTip}
      RootProp:creative_prop = creative_prop{}
   2. An editable `float` named `MoveDuration`. This is the amount of time the prop takes to reach its destination.

      Verse

      ```
       # The duration in seconds it takes for the prop to move to its destination.
       @editable {ToolTip := MoveDurationTip}
       MoveDuration:float = 3.0
      ```

       # The duration in seconds it takes for the prop to move to its destination.
      @editable {ToolTip := MoveDurationTip}
      MoveDuration:float = 3.0
   3. An editable `float` named `MoveStartDelay`. This is the time in seconds the prop waits before moving.

      Verse

      ```
       # The duration in seconds to wait before movement begins.
       @editable {ToolTip := MoveStartDelayTip}
       MoveStartDelay:float = 0.0
      ```

       # The duration in seconds to wait before movement begins.
      @editable {ToolTip := MoveStartDelayTip}
      MoveStartDelay:float = 0.0
   4. An editable `float` named `MoveEndDelay`. This is the time in seconds the prop waits after moving.

      Verse

      ```
       # The duration in seconds to wait after movement ends.
       @editable {ToolTip := MoveEndDelayTip}
       MoveEndDelay:float = 0.0
      ```

       # The duration in seconds to wait after movement ends.
      @editable {ToolTip := MoveEndDelayTip}
      MoveEndDelay:float = 0.0
   5. An editable `logic` named `MoveOnceAndStop`. This controls whether your prop only moves once, or repeats movement after it finishes.

      Verse

      ```
       # Whether the RootProp should stop in place when it finishes moving.
       @editable {ToolTip := MoveOnceAndStopTip}
       MoveOnceAndStop:logic = false
      ```

       # Whether the RootProp should stop in place when it finishes moving.
      @editable {ToolTip := MoveOnceAndStopTip}
      MoveOnceAndStop:logic = false
   6. An editable `logic` named `ShouldReset`. This controls whether your prop resets to its original position after it finishes moving.

      Verse

      ```
       # Whether the RootProp should reset back to the starting position when it
       # finishes moving.
       @editable {ToolTip := ShouldResetTip}
       ShouldReset:logic = false
      ```

       # Whether the RootProp should reset back to the starting position when it
      # finishes moving.
      @editable {ToolTip := ShouldResetTip}
      ShouldReset:logic = false
   7. A variable [transform](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#transform) named `StartingTransform`. This is the transform the `RootProp` is at when it starts movement.

      Verse

      ```
       # The starting transform of the RootProp.
       var StartingTransform:transform = transform{}
      ```

       # The starting transform of the RootProp.
      var StartingTransform:transform = transform{}
5. Your final class definition should look like this:

   Verse

   ```
        using { /Fortnite.com/Devices }
        using { /Fortnite.com/Devices/CreativeAnimation }
        using { /Verse.org/Simulation }
        using { /UnrealEngine.com/Temporary/SpatialMath }    
   		
        MoveDurationTip<localizes>:message = "The amount of time in seconds the prop takes to move to its destination."
        MoveEaseTypeTip<localizes>:message = "The animation easing applied to the movement."
        MoveEndDelayTip<localizes>:message = "The delay after the movement finishes."
        MoveOnceAndStopTip<localizes>:message = "Whether the RootProp should stop in place after it finishes moving."
        MoveStartDelayTip<localizes>:message = "The delay before the movement starts."
   ```
6. Before your prop moves, it needs to know where it’s moving from. To do this, you’ll define a new function to set the `StartingTransform` before movement:
7. To start moving your prop, you’ll define a new function `Move()`:
8. If you want your prop to reset when it finishes moving, you need to teleport it back to its starting position. To handle this, add a new method `Reset()` to your `movable_prop` class definition:
9. You’ve defined a lot of functions, and now it’s time to tie them all together. To manage all the different movement functions, add a new method, `ManageMovement()`, to your `movable_prop` class definition. Add the `<suspends>` modifier to let this function run asynchronously.

   Verse

   ```
        # Loops moving the RootProp to its target by calling Move(), and handles
        # any logic when the movement begins and ends.
        ManageMovement()<suspends>:void=
   ```

   # Loops moving the RootProp to its target by calling Move(), and handles
   # any logic when the movement begins and ends.
   ManageMovement()&lt;suspends&gt;:void=
10. In `ManageMovement()`, create a `loop` expression that manages the movement. Inside the loop, first `Sleep()` for `MoveStartDelay` seconds, then call `Move()`.

    Verse

    ```
         # Loops moving the RootProp to its target by calling Move(), and handles
         # any logic when the movement begins and ends.
         ManageMovement()<suspends>:void=
             loop:
                 Sleep(MoveStartDelay)
    		
                 Move()
    ```

     # Loops moving the RootProp to its target by calling Move(), and handles
    # any logic when the movement begins and ends.
    ManageMovement()&lt;suspends&gt;:void=
    loop:
    Sleep(MoveStartDelay)
    Move()
11. When your platform finishes moving, it needs to keep going, reset its position, or stop in place. To handle stopping, in an `if` expression, check if `MoveOnceAndStop` is true. If so, `break` out of the loop. After movement stops, `Sleep()` for `MoveEndDelay` seconds. Finally, in another `if` expression, check if `ShouldReset` is true and call `Reset[]` if so. Your complete `ManageMovement()` function should look like this:

    Verse

    ```
         # Loops moving the RootProp to its target by calling Move(), and handles
         # any logic when the movement begins and ends.
         ManageMovement()<suspends>:void=
             loop:
                 Sleep(MoveStartDelay)

                 Move()

                 # If the prop should only move once and stop, then exit the loop.
                 if:
    ```
12. Since there’s no `OnBegin()` function in this class, you need a way for other classes to call `ManageMovement()` to start moving your platform. Add a new function `Setup()` to your `movable_prop` class definition. Inside `Setup()`, first call `SetStartingTransform()`, then spawn a `ManageMovement()` function to get your platform going.
    Your complete `Setup()` function should look like this

    Verse

    ```
     # Set the StartingTransform, then begin movement by spawning ManageMovement.
     Setup():void=
         SetStartingTransform()
         spawn{ManageMovement()}
    ```

     # Set the StartingTransform, then begin movement by spawning ManageMovement.
    Setup():void=
    SetStartingTransform()
    spawn{ManageMovement()}

## Next Up

With your abstract class complete, in the next step, you’ll figure out how to get them moving through animation!

- [![2. Moving Props with Animations](https://dev.epicgames.com/community/api/documentation/image/eef23c78-e1f2-4438-97ff-0d44e347cde6?resizing_type=fit&width=640&height=640)

  2. Moving Props with Animations

  Learn how to use this powerful tool to build your own animations and get your props moving!](https://dev.epicgames.com/documentation/fortnite/animating-prop-movement-2-moving-props-with-animations-in-verse)

## Complete Code

Here is the complete code built in this section:

### movable_prop.verse

Verse

```
using { /Fortnite.com/Devices }
using { /Fortnite.com/Devices/CreativeAnimation }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/SpatialMath }

MoveDurationTip<localizes>:message = "The amount of time in seconds the prop takes to move to its destination."
MoveEaseTypeTip<localizes>:message = "The animation easing applied to the movement."
MoveEndDelayTip<localizes>:message = "The delay after the movement finishes."
MoveOnceAndStopTip<localizes>:message = "Whether the RootProp should stop in place after it finishes moving."
MoveStartDelayTip<localizes>:message = "The delay before the movement starts."
```
