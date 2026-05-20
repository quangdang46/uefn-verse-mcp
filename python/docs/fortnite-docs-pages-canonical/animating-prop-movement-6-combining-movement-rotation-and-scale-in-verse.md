## https://dev.epicgames.com/documentation/en-us/fortnite/animating-prop-movement-6-combining-movement-rotation-and-scale-in-verse

# 6. Combining Movement, Rotation, and Scale

Time to combine different aspects of your moving props with Verse to build a Fall Guys obstacle course.

![6. Combining Movement, Rotation, and Scale](https://dev.epicgames.com/community/api/documentation/image/c0ad0006-5ec4-42ee-b8cc-50bd6c4af6ba?resizing_type=fill&width=1920&height=335)

The step above objects that move, rotate, or scale is doing all three concurrently. However, there are some important challenges to consider when building animations for props that move in multiple ways at the same time.

Since the animation controller can only play one animation at a time, you can’t do moving, rotating, and scaling in separate animations. These animations also need multiple keyframes, since you may want to rotate a prop multiple times per animation. Because you need to build all the keyframes ahead of time, you also need to calculate the position, rotation, and scale at each point in the prop’s journey. What happens if your prop doesn’t make an even amount of rotations? How do you handle half a rotation?

There’s a lot of math involved in this next section, but by the end, you’ll be able to move, rotate, and scale props to multiple points, and create complex, dynamic, and (most important!) fun platforming challenges to make the Fall Guys course of your dreams.

## Building Animations that Move, Rotate, and Scale

Follow these steps to start putting things together:

1. Create a new Verse class named `animating_prop` that inherits from `movable_prop` using **Verse Explorer**. Add the `<concrete>` specifier to this class to expose its properties to UEFN.

   Verse

   ```
        # A prop that translates, rotates, and scales to a destination using animation.
        animating_prop<public> := class<concrete>(movable_prop):
   ```

    # A prop that translates, rotates, and scales to a destination using animation.
   animating_prop&lt;public&gt; := class&lt;concrete&gt;(movable_prop):
2. Add the `using { /Fortnite.com/Devices/CreativeAnimation }` and `using { /UnrealEngine.com/Temporary/SpatialMath }` statements to the top of the file to import these modules. You’ll need these to animate your prop. The tooltips used in this section are also included here.

   Verse

   ```
        using { /Fortnite.com/Devices }
        using { /Fortnite.com/Devices/CreativeAnimation }
        using { /Verse.org/Simulation }
        using { /UnrealEngine.com/Temporary/SpatialMath }

        RotationRateTip<localizes>:message := "The time it takes to make one AdditionalRotation in seconds."
        UseEasePerKeyframeTip<localizes>:message := "Whether this prop should use the MoveEaseType for each keyframe. False will use the Linear ease type on each frame."

        # A prop that translates, rotates, and scales to a destination using animation.
        animating_prop<public> := class<concrete>(movable_prop):
   ```

    using { /Fortnite.com/Devices }
   using { /Fortnite.com/Devices/CreativeAnimation }
   using { /Verse.org/Simulation }
   using { /UnrealEngine.com/Temporary/SpatialMath }
   RotationRateTip&lt;localizes&gt;:message := &quot;The time it takes to make one AdditionalRotation in seconds.&quot;
   UseEasePerKeyframeTip&lt;localizes&gt;:message := &quot;Whether this prop should use the MoveEaseType for each keyframe. False will use the Linear ease type on each frame.&quot;
   # A prop that translates, rotates, and scales to a destination using animation.
   animating_prop&lt;public&gt; := class&lt;concrete&gt;(movable_prop):
3. At the top of the `animating_prop` class definition, add the following fields:
4. Your class definition should look like this:

   Verse

   ```
        using { /Fortnite.com/Devices }
        using { /Fortnite.com/Devices/CreativeAnimation }
        using { /Verse.org/Simulation }
        using { /UnrealEngine.com/Temporary/SpatialMath }

        RotationRateTip<localizes>:message := "The time it takes to make one AdditionalRotation in seconds."
        UseEasePerKeyframeTip<localizes>:message := "Whether this prop should use the MoveEaseType for each keyframe. False will use the Linear ease type on each frame."

        # A prop that translates, rotates, and scales to a destination using animation.
        animating_prop<public> := class<concrete>(movable_prop):
   ```
5. Override the `Move()` function in your `animating_prop` class. Then in a `for` expression, iterate through each `MoveTarget` in the `MoveTargets` array. Check if each `MoveTarget` is valid, and if so set the `TargetTransform` to the transform of the `MoveTarget`.

   Verse

   ```
        # Move and rotate the RootProp toward the MoveTarget, or MoveTransform if one is set.
        Move<override>()<suspends>:void=

            # Move to each target in the MoveTargets array.
            for:
                MoveTarget:MoveTargets
            do:

                # Set the TargetTransformto the MoveTarget if the
                # MoveTarget is set. Otherwise set it to the MoveTransform.
   ```
6. Back in your `movement_behaviors` file, add a new method named `BuildMovingAnimationKeyframes()`. This function will build and return an array of keyframes that animate a prop moving and rotating to a target transform. This function takes several parameters from `animating_prop` — the `MoveDuration`, `RotationRate`, `AdditionalRotation`, the `OriginalTransform` (the starting transform of the prop), the `TargetTransform`, the `MoveEaseType`, and a new `logic` value called `UseEasePerKeyframe`. This determines whether you use the `MoveEaseType` for each keyframe. Your function signature should look like this:

   Verse

   ```
        # Builds an array of keyframes that animate movement and rotation from the OriginalTransform to the TargetTransform.
        BuildMovingAnimationKeyframes(MoveDuration:float, RotationRate:float, AdditionalRotation:rotation, OriginalTransform:transform, TargetTransform:transform,MoveEaseType:move_to_ease_type, UseEasePerKeyframe:logic):[]keyframe_delta=
   ```

    # Builds an array of keyframes that animate movement and rotation from the OriginalTransform to the TargetTransform.
   BuildMovingAnimationKeyframes(MoveDuration:float, RotationRate:float, AdditionalRotation:rotation, OriginalTransform:transform, TargetTransform:transform,MoveEaseType:move_to_ease_type, UseEasePerKeyframe:logic):[]keyframe_delta=
7. In `BuildMovingAnimationKeyframes()`, initialize the following variables:

   1. A variable array of `keyframe_delta` named `Keyframes`. This is the array you’ll return at the end.

      Verse

      ```
       # The array of keyframes to return.
       var KeyFrames:[]keyframe_delta = array{}
      ```

       # The array of keyframes to return.
      var KeyFrames:[]keyframe_delta = array{}
   2. A variable `float` named `TotalTime`. This is the total amount of time spent animating so far.

      Verse

      ```
       # The total amount of time spent animating.
       var TotalTime:float = 0.0
      ```

       # The total amount of time spent animating.
      var TotalTime:float = 0.0
   3. Two `transform` variables named `StartTransform` and `EndTransform`. These are the starting and ending transforms of the prop at the start and end of each keyframe. Initialize both to the `OriginalTransform`.

      Verse

      ```
       # The starting transform for building keyframes. This is the
       # transform of the RootProp at the start of each keyframe.
       var StartTransform:transform = OriginalTransform

       # The ending transform for building keyframes. This is the
       # transform of the RootProp at the end of each keyframe.
       var EndTransform:transform = OriginalTransform
      ```

       # The starting transform for building keyframes. This is the
      # transform of the RootProp at the start of each keyframe.
      var StartTransform:transform = OriginalTransform
      # The ending transform for building keyframes. This is the
      # transform of the RootProp at the end of each keyframe.
      var EndTransform:transform = OriginalTransform
   4. A variable `rotation` named `RotationToApply`, initialized to the `AdditionalRotation`. This is the actual rotation you’ll apply to the prop for each keyframe. Usually, this will be the `AdditionalRotation`, but if you need to make a fractional rotation you’ll change this value.

      Verse

      ```
       # The actual rotation to apply to the RootProp. Usually this is the
       # AdditionalRotation, but will change in cases with fractional rotations.
       var RotationToApply:rotation = AdditionalRotation
      ```

       # The actual rotation to apply to the RootProp. Usually this is the
      # AdditionalRotation, but will change in cases with fractional rotations.
      var RotationToApply:rotation = AdditionalRotation
   5. A variable `float` named `AnimationTime`. This is the amount of time in seconds each keyframe takes. Initialize this to `1.0 / RotationRate`, since the RootProp needs to make a `RotationRate` number of rotations per second.

      Verse

      ```
       # The time it takes for each keyframe of animation to complete.
       # This is initialized to 1.0/Rotation rate since the RootProp needs to make a
       # RotationRate number of rotations per second.
       var AnimationTime:float = 1.0 / RotationRate
      ```

       # The time it takes for each keyframe of animation to complete.
      # This is initialized to 1.0/Rotation rate since the RootProp needs to make a
      # RotationRate number of rotations per second.
      var AnimationTime:float = 1.0 / RotationRate
   6. A `float` value named `TotalRotations`. This is the total number of rotations to make across the entire animation, and is initialized to `MoveDuration * RotationRate`. The reason this is a `float` and not an `int` is to deal with situations where you don’t need to make a full rotation, such as at the end of an animation.

      Verse

      ```
       # The total number of rotations to make.
       TotalRotations:float = MoveDuration * RotationRate
      ```

       # The total number of rotations to make.
      TotalRotations:float = MoveDuration * RotationRate
   7. A `float` value named `TimePerRotation`. This is the amount of time in seconds it takes one rotation to complete. Your function should now look like this.

      Verse

      ```
       # Builds an array of keyframes that animate movement and rotation from the OriginalTransform to the TargetTransform.
       BuildMovingAnimationKeyframes(MoveDuration:float, RotationRate:float, AdditionalRotation:rotation, OriginalTransform:transform, TargetTransform:transform,MoveEaseType:move_to_ease_type, UseEasePerKeyframe:logic):[]keyframe_delta=

           # The array of keyframes to return.
           var KeyFrames:[]keyframe_delta = array{}

           # The total amount of time spent animating.
           var TotalTime:float = 0.0

           # The starting transform for building keyframes. This is the
      ```

That’s a lot of values to keep track of, so let’s do an example calculation, using `2.5` as the `RotationRate` and `5.0` as the `MoveDuration`.

Verse

```
    Rotation Rate = 2.5 rotations/second

    Move Duration = 5.0 seconds

    Animation Time = 
        1.0 seconds/Rotation Rate = 
        1.0/2.5 = 0.4 seconds

    Total Rotations = 
        Move Duration /Rotation Rate =
```

With a `RotationRate` of `2.5` and a `MoveDuration` of `5.0`, you’ll make `12.5` rotations in total, with each rotation taking `0.4` seconds. This means you’ll have to make an extra half-rotation at the end of the animation. You might also notice that the animation time and time per rotation are the same. This is almost always the case, except when you need to make less than a full rotation. Even though they’re initially the same value, you’ll need to keep track of both variables to handle some later math.

## Building Keyframes on a Loop

It’s time to get building! Follow the steps below to set up the loop that builds your keyframes.

1. Add a `loop` expression to `BuildMovingAnimationKeyframes()`. On each iteration of the loop, you’ll build a new keyframe and add it to the keyframes array. At the start of the loop, update the `TotalTime` with the `TimePerRotation`.

   Verse

   ```
        # Build each keyframe of animation and add it to the Keyframes array.
        # The loop breaks when the TotalTime goes past the MoveDuration.
        loop:
            # Add the TimePerRotation to the TotalTime.
            set TotalTime += TimePerRotation
   ```

    # Build each keyframe of animation and add it to the Keyframes array.
   # The loop breaks when the TotalTime goes past the MoveDuration.
   loop:
   # Add the TimePerRotation to the TotalTime.
   set TotalTime += TimePerRotation
2. Build the `EndTransform`, which is where the prop should be at the end of this keyframe. Set the `EndTransform` to a new transform with the following parameters:
3. With your end transform set, it’s time to build a keyframe! This is largely the same process you did for your `MoveToEase()` function. Create a new `keyframe_delta` variable named `KeyFrame`. Set the `DeltaLocation` to the difference between the end and start transform translations. Set the `DeltaRotation` to the end transform’s rotation. Since you need to calculate the change in scale, set the `DeltaScale` to the result of dividing the end transform’s scale by the starting transform’s scale. The `Time` should be the `AnimationTime`, and the `InterpolationType` should be the result of an `if` expression. If `UseEasePerKeyframe` is true, use the `MoveEaseType`. Otherwise, use the linear type. Your keyframe expression should look like this:

   Verse

   ```
        # Build the animation keyframe to animate the RootProp.
        Keyframe := keyframe_delta:
            DeltaLocation := EndTransform.Translation - StartTransform.Translation,
            DeltaRotation := EndTransform.Rotation,
            DeltaScale := EndTransform.Scale/StartTransform.Scale,
            Time := AnimationTime,
            # Use the MoveEaseType for interpolation if UseEasePerKeyframe is true,
            # otherwise use the Linear movement type.
            Interpolation :=
                if:
   ```
4. With your keyframe built, now you can add it to the `Keyframes` array. Then set the `StartTransform` to the `EndTransform` to update it for the next keyframe. Finally, if the `TotalTime` is now greater than the `MoveDuration`, break out of the loop.

   Verse

   ```
        # Add the new keyframe to the KeyFrames array, and set the
        # StartTransform to the EndTransform.
        set Keyframes += array{Keyframe}
        set StartTransform = EndTransform
        # Break out of the loop if the TotalTime passes the MoveDuration.
        if:
            TotalTime &gt;= MoveDuration
        then:
            break
   ```

    # Add the new keyframe to the KeyFrames array, and set the
   # StartTransform to the EndTransform.
   set Keyframes += array{Keyframe}
   set StartTransform = EndTransform
   # Break out of the loop if the TotalTime passes the MoveDuration.
   if:
   TotalTime &amp;gt;= MoveDuration
   then:
   break
5. There’s an important edge case to consider: what happens when you need to make less than a full rotation? Since you’re adding the `TimePerRotation` to the `TotalTime`, this means the `TotalTime`could be higher than the `MoveDuration` at the start of the loop. In this situation, you need to handle the leftover time and make less than full rotation, with a shorter animation time to account for the difference. Follow these steps to account for this situation:
6. At the very end of your function, after the loop, return the `Keyframes` array. Your complete `BuildMovingAnimationKeyframes()` function should look like this:

   Verse

   ```
        # Builds an array of keyframes that animate movement and rotation from the OriginalTransform to the TargetTransform.
        BuildMovingAnimationKeyframes(MoveDuration:float, RotationRate:float, AdditionalRotation:rotation, OriginalTransform:transform, TargetTransform:transform,MoveEaseType:move_to_ease_type, UseEasePerKeyframe:logic):[]keyframe_delta=
   		
            # The array of keyframes to return.
            var Keyframes:[]keyframe_delta = array{}
   		
            # The total amount of time spent animating.
            var TotalTime:float = 0.0
   		
            # The starting transform for building keyframes. This is the
   ```
7. Now that you’ve defined the logic to build your keyframes, it’s time to animate them. You’ll use a separate function to build and call your animation. Add a new function `BuildAndPlayAnimation()` to your `animating_prop` class. Add the `<suspends>` modifier to this function to allow it to call other asynchronous functions.

   Verse

   ```
        # Builds an animation from an array of keyframes, then calls MoveToEase()
        # to animate the prop.
        BuildAndPlayAnimation()<suspends>:void=
   ```

    # Builds an animation from an array of keyframes, then calls MoveToEase()
   # to animate the prop.
   BuildAndPlayAnimation()&lt;suspends&gt;:void=
8. In `BuildAndPlayAnimation()`, initialize a new `keyframe_delta` array named `Keyframes`. Then set `Keyframes` to the result of calling `BuildMovingAnimationKeyframes()`. Use `RootProp.GetTransform()` as the starting transform since the prop’s position will change between `Move()` calls. Initialize an `animation_mode` variable to `animation_mode.OneShot`, and call `MoveToEase()`, passing the `Keyframes` array and the `AnimationMode`.

   Your complete `BuildAndPlayAnimation()` function should look like this:

   Verse

   ```
    # Builds an animation from an array of keyframes, then calls MoveToEase()
    # to animate the prop.
    BuildAndPlayAnimation()<suspends>:void=
        var Keyframes:[]keyframe_delta = array{}

        # Build the animation, using the RootProp as the target transform.
        set Keyframes = BuildMovingAnimationKeyframes(MoveDuration, RotationRate, AdditionalRotation, RootProp.GetTransform(), TargetTransform, MoveEaseType, UseEasePerKeyframe)

        # Set the animation mode to OneShot.
        var AnimationMode:animation_mode := animation_mode.OneShot
   ```
9. Back in `Move()`, call `BuildAndPlayAnimation()` after you set the `TargetTransform` to the move targets transform.

   Verse

   ```
        # Move to each target in the MoveTargets array.
        for:
            MoveTarget:MoveTargets
        do:
            # Set the TargetTransform to the MoveTarget if the
            # MoveTarget is set. Otherwise set it to the MoveTransform.
            if:
                MoveTarget.IsValid[]
            then:
                set TargetTransform = MoveTarget.GetTransform()
   ```

There’s one more case to consider. What should happen if you don’t set any move targets? In this situation, your prop should continue to rotate in place, without moving to a new destination. To handle this, add an `if` expression to the top of your `Move()` function. In the `if`, check if `MoveTargets.Length = 0`, and if so set the `TargetTransform` to the root prop’s transform. Then call `BuildAndPlayAnimation()`. This way, your prop will continue to animate even if you didn’t set a move target. Your complete `Move()` animation should look like this:

Verse

```
    # Move and rotate the RootProp toward the MoveTarget, or MoveTransform if one is set.
    Move<override>()<suspends>:void=
        # If there are no targets to move to, this prop will rotate in place.
        if:
            MoveTargets.Length = 0
        then:
            set TargetTransform = RootProp.GetTransform()

            # Build and play the animation.
            BuildAndPlayAnimation()
```

Now you need to reference `animating_prop` in your `prop_animator` class. In `prop_animator`, add an editable array of `animating_prop` named `MoveAndRotateProps`. In `OnBegin()`, in another `for` expression, initialize each prop in `MoveAndRotateProps` by calling `Setup()`. Your complete `prop_animator` class should look like this:

Verse

```
    using { /Fortnite.com/Devices }
    using { /Verse.org/Simulation }
    using { /UnrealEngine.com/Temporary/Diagnostics }

    TranslatingPropsTip<localizes>:message = "The props that translate (move) using animation."
    RotatingPropsTip<localizes>:message = "The props that rotate using animation."
    ScalingPropsTip<localizes>:message = "The props that scale using animation."
    AnimatingPropsTip<localizes>:message = "The props that both move and rotate using animation."

    # Coordinates moving props through animation by calling each movable_prop's Setup() method.
```

Save your code and compile it.

Congratulations, that’s all the code out of the way! Now it’s time to get everything linked together.

The `animating_prop` class you just created can move, rotate, and scale props. However, it is still reliant on the `moveable_prop` class because it needs to inherit several functions such as `ManageMovement()`. Given that the `animating_prop` class can perform all three types of movement, you may find it useful to refactor `animating_prop` to include all the logic of `moveable_prop` so that the class can stand alone. An example refactor is included here, which merges `animating_prop` and `moveable_prop` into a single file. It also includes the `prop_animator` verse device class. You will still need the functionality from `movement_behaviors` for your code to run, but this refactor reduces the number of files needed from five to two. This code is also included in the [Complete Code section](https://dev.epicgames.com/documentation/fortnite/animating-prop-movement-6-combining-movement-rotation-and-scale-in-verse#complete-code).

Verse

```
using { /Fortnite.com/Devices }
using { /Fortnite.com/Devices/CreativeAnimation }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/SpatialMath }

EasingCategory<localizes>:message := "These control the type of movement easing applied to the prop."
LogicCategory<localizes>:message := "These control different aspects of the prop's logic."
PropsCategory<localizes>:message := "These are the props that move associated with this device."
RotationCategory<localizes>:message := "These control how the prop rotates."
TimingCategory<localizes>:message := "These control the timing of parts of the prop's movmement."
```

## Linking Props to Devices

Back in the editor, delete a section of the course after the rotating props section to create a gap before the end goal. Add another **FG01 SpinningBar Double S** and **FG01 Hover Platform M** to your level. Name them **SpinningMovingBar** and **TranslatingPlatform**, then add several **FG01 Button Bulb** props, which will be the targets each prop will move to. Name these **PlatformTarget**. Place the platforms and bar over the gap, and make sure to place the targets where you want the platforms to move. In this example, the spinning bar moves side-to-side, while the platform moves back and forth.

[![The setup of the props that move rotate and scale](https://dev.epicgames.com/community/api/documentation/image/da64be19-2dfd-431d-9cf1-bdf70bd30f94?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/da64be19-2dfd-431d-9cf1-bdf70bd30f94?resizing_type=fit)

*Setup of the spinning bar and moving platform. The arrows indicate in what directions each prop moves. Both the spinning bar and the platform move back and forth, and the spinning bar spins as it moves.*

Select your **prop animator** in the **Outliner**. Add an array element to `AnimatingProps` for your spinning bar. Set each value to the following:

| Option | Value | Explanation |
| --- | --- | --- |
| **Additional Rotation** | 90.0 | This prop will make a 90-degree rotation each time. |
| **Rotation Rate** | 1.5 | This prop will make a rotation every `1.5` seconds. Combined with the move duration, this means the prop will rotate `4.5` times each animation. |
| **Use Ease Per Keyframe** | false | This will use the Linear easing type on each keyframe to move and rotate the prop at a consistent speed. |
| **MoveTargets** | 2 elements, assigned to platform targets. | These are the targets you want the bar to move to. |
| **RootProp** | SpinningMovingBar | This is the prop you’re animating. |

Add another array element to `TranslatingProps` for your moving platform. Assign the `MoveTargets` to your platform targets, and the `RootProp` to your `TranslatingPlatform`.

Hit **Launch Session** and try running through your complete obstacle course!

## On Your Own

And that’s it! Now you’ve got everything you need to make your own Fall Guys obstacle course using Verse!

You can use the code here to animate Creative props in any of your experiences, and even beyond Fall Guys projects!

Using what you’ve learned, try the following:

- Make obstacles that rotate in a variety of directions, or rotate randomly across keyframes.
- Make obstacles that activate only when a player stands on them or gets within a certain distance.
- Work out how to make platforms that disappear after a certain duration, or move the player into dangerous positions if they stay on too long.

## Complete Code

Here is the complete code built in this section, including an example refactor for `animating_prop`.

### movable_prop.verse

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

### translating_prop.verse

Verse

```
using { /Fortnite.com/Devices }
using { /Fortnite.com/Devices/CreativeAnimation }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/SpatialMath }

MovePositionTip<localizes>:message = "The optional position to move to World Space. Use this if you do not want to set a MoveTarget."

# A prop that moves (translates) toward either a Creative prop target
# or a position in world space.
translating_prop<public> := class<concrete>(movable_prop):
```

### rotating_prop.verse

Verse

```
using { /Fortnite.com/Devices }
using { /Fortnite.com/Devices/CreativeAnimation }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/SpatialMath }

AdditionalRotationTip<localizes>:message = "The rotation to apply to the RootProp."
ShouldRotateForeverTip<localizes>:message = "Whether the RootProp should rotate forever."
MatchRotationTargetTip<localizes>:message = "The optional prop whose rotation the RootProp should rotate to. Use this if you do not want to set an Additional Rotation."

# A prop that rotates by an additional rotation or rotates to match
```

### scaling_prop.verse

Verse

```
using { /Fortnite.com/Devices }
using { /Fortnite.com/Devices/CreativeAnimation }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/SpatialMath }

MatchScaleTargetTip<localizes>:message = "The optional position to move to World Space. Use this if you do not want to set a MoveTarget."

# A prop that scales toward either a given scale or a Creative prop's scale.
scaling_prop<public> := class<concrete>(movable_prop):
    # The array of vector3 targets for the RootProp to scale to.
```

### animating_prop.verse

Verse

```
using { /Fortnite.com/Devices }
using { /Fortnite.com/Devices/CreativeAnimation }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/SpatialMath }

RotationRateTip<localizes>:message := "The time it takes to make one AdditionalRotation in seconds."
UseEasePerKeyframeTip<localizes>:message := "Whether this prop should use the MoveEaseType for each keyframe. False will use the Linear ease type on each frame."

# A prop that translates, rotates, and scales to a destination using animation.
animating_prop<public> := class<concrete>(movable_prop):
```

### movement_behaviors.verse

Verse

```
# This file stores functions common to animating Creative props using keyframes.
# It also defines the move_to_ease_type enum to help in building animations.

using { /Fortnite.com/Devices }
using { /UnrealEngine.com/Temporary/SpatialMath }
using { /Fortnite.com/Characters}
using { /Fortnite.com/Devices/CreativeAnimation }

# Represents the different movement easing types.
move_to_ease_type<public> := enum {Linear, Ease, EaseIn, EaseOut, EaseInOut}
```

### prop_animator.verse

Verse

```
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }

TranslatingPropsTip<localizes>:message = "The props that translate (move) using animation."
RotatingPropsTip<localizes>:message = "The props that rotate using animation."
ScalingPropsTip<localizes>:message = "The props that scale using animation."
MoveAndRotatePropsTip<localizes>:message = "The props that both move and rotate using animation."

# Coordinates moving props through animation by calling each moveable_prop's Setup() method.
```

### animating_props.verse (example refactor of animating_prop)

Verse

```
using { /Fortnite.com/Devices }
using { /Fortnite.com/Devices/CreativeAnimation }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/SpatialMath }

EasingCategory<localizes>:message := "These control the type of movement easing applied to the prop."
LogicCategory<localizes>:message := "These control different aspects of the prop's logic."
PropsCategory<localizes>:message := "These are the props that move associated with this device."
RotationCategory<localizes>:message := "These control how the prop rotates."
TimingCategory<localizes>:message := "These control the timing of parts of the prop's movmement."
```
