## https://dev.epicgames.com/documentation/en-us/fortnite/animating-prop-movement-2-moving-props-with-animations-in-verse

# 2. Moving Props with Animations

Learn how to use this powerful tool to build your own animations and get your props moving!

![2. Moving Props with Animations](https://dev.epicgames.com/community/api/documentation/image/6a4e3309-2dd4-4553-8702-91a195b252a0?resizing_type=fill&width=1920&height=335)

There are several ways you can move props in UEFN. You can use functions like [TeleportTo[]](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) or [MoveTo()](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) to modify a transform directly or use another device like a prop mover to move a prop on a preset path. However, there’s another useful option in the form of animations.

Each Creative prop has a `play_animation_controller` that you can use to play animations of it. Animations have a couple of benefits over moving the prop’s transform. Animations usually have smoother movement than moving objects with `MoveTo()` or `TeleportTo()` because they avoid the network latency of having to call these functions every [game tick](https://dev.epicgames.com/documentation/fortnite/verse-glossary#simulation-update). Animations also have more consistent collisions with players or other objects, and you have a greater level of control over where and how an objects moves as compared to using a [Prop Mover device](https://dev.epicgames.com/documentation/en-us/fortnite-creative/using-prop-mover-devices-in-fortnite-creative). You can play animations on a loop, or play them back and forth with the ping-pong mode.

Animations also let you choose an interpolation type. The interpolation type determines the type of easing, or animation curve, your animation follows. For instance, the linear interpolation type plays your animation at a constant speed, while the ease-in type starts slow, and then speeds up toward the end. By choosing the right interpolation type for your animation, you can specify at different points whether the prop should slow down, speed up, or move linearly.

By switching between different animations for your obstacles, you can create a variety of different challenges for players by using the same props. In this section, you’ll learn how to use this powerful tool to build your own animations and get your props moving!

## Setting up Animation Controls

Follow the steps below to set up animation controls for your props:

1. Using **Verse Explorer**, create a new Verse file named `movement_behaviors`. This will store the utility functions you need to animate props.
2. Add the `using { /Fortnite.com/Devices }`, `using { /Fortnite.com/Devices/CreativeAnimation }` and `using { /UnrealEngine.com/Temporary/SpatialMath }` statements to the top of the file to import these modules. You’ll need these to animate your prop.
3. In `movement_behaviors`, create a new `enum` named `move_to_ease_type`. The values in this enum correspond to the different animation-easing types. You can view each of these easing types in the [`InterpolationTypes` module](https://dev.epicgames.com/documentation/en-us/uefn/verse-api/fortnitedotcom/devices/creativeanimation/interpolationtypes).

   Verse

   ```
        # This file stores functions common to animating creative props using keyframes.
        # It also defines the move_to_ease_type enum to help in building animations.
        using { /Fortnite.com/Devices }
        using { /UnrealEngine.com/Temporary/SpatialMath }
        using { /Fortnite.com/Devices/CreativeAnimation }

        # Represents the different movement easing types.
        move_to_ease_type<public> := enum {Linear, Ease, EaseIn, EaseOut, EaseInOut}
   ```

    # This file stores functions common to animating creative props using keyframes.
   # It also defines the move_to_ease_type enum to help in building animations.
   using { /Fortnite.com/Devices }
   using { /UnrealEngine.com/Temporary/SpatialMath }
   using { /Fortnite.com/Devices/CreativeAnimation }
   # Represents the different movement easing types.
   move_to_ease_type&lt;public&gt; := enum {Linear, Ease, EaseIn, EaseOut, EaseInOut}
4. Add a new `vector3` type alias named `VectorOnes` that makes a `vector3` where `X`, `Y`, and `Z` are all set to `1.0`. You’ll use this vector later to make some math easier, so defining a type alias for it means you don’t have to write `vector3{X:=1.0, Y:=1.0, Z:=1.0}` repeatedly.

   Verse

   ```
        # Initializes a vector3 with all values set to 1.0.
        VectorOnes<public>:vector3 = vector3{X:=1.0, Y:=1.0, Z:=1.0}
   ```

    # Initializes a vector3 with all values set to 1.0.
   VectorOnes&lt;public&gt;:vector3 = vector3{X:=1.0, Y:=1.0, Z:=1.0}
5. Add a new method `GetCubicBezierForEaseType()` that takes a `move_to_ease_type` and returns a `cubic_bezier_parameters`.

   Verse

   ```
        # Return the cubic_bezier_parameters based on the given move_to_ease_type.
        GetCubicBezierForEaseType(EaseType:move_to_ease_type):cubic_bezier_parameters=
   ```

    # Return the cubic_bezier_parameters based on the given move_to_ease_type.
   GetCubicBezierForEaseType(EaseType:move_to_ease_type):cubic_bezier_parameters=

   The cubic bezier consists of four numbers that define the type of easing function the animation uses. For instance, the parameters for an ease-in curve make the animation slow down at the start and speed up after. The parameters for a linear curve make the animation play at a constant speed. You can define these values yourself to create your own custom animation curves, but you don’t need to in this example since you’ll be using the ones defined in the `InterpolationTypes` module.
6. In `GetCubicBezierForEaseType()`, in a `case()` expression, retrieve the `cubic_bezier_parameters` from the `InterpolationTypes` module based on the `move_to_ease_type`. For instance, `EaseOut` should return `InterpolationTypes.EaseOut`, `Linear` should return `InterpolationTypes.Linear`, and so on. Your complete `GetCubicBezierForEaseType()` function should look like this:

   Verse

   ```
   # Return the cubic_bezier_parameters based on the given move_to_ease_type.     GetCubicBezierForEaseType(EaseType:move_to_ease_type):cubic_bezier_parameters=
            case (EaseType):
                move_to_ease_type.Linear => InterpolationTypes.Linear
                move_to_ease_type.Ease => InterpolationTypes.Ease
                move_to_ease_type.EaseIn => InterpolationTypes.EaseIn
                move_to_ease_type.EaseOut => InterpolationTypes.EaseOut
                move_to_ease_type.EaseInOut => InterpolationTypes.EaseInOut
   ```

   # Return the cubic_bezier_parameters based on the given move_to_ease_type. GetCubicBezierForEaseType(EaseType:move_to_ease_type):cubic_bezier_parameters=
   case (EaseType):
   move_to_ease_type.Linear =&gt; InterpolationTypes.Linear
   move_to_ease_type.Ease =&gt; InterpolationTypes.Ease
   move_to_ease_type.EaseIn =&gt; InterpolationTypes.EaseIn
   move_to_ease_type.EaseOut =&gt; InterpolationTypes.EaseOut
   move_to_ease_type.EaseInOut =&gt; InterpolationTypes.EaseInOut
7. Back in your `movable_prop` class, add a new editable `move_to_ease_type` named `MoveEaseType`. This is the easing type your prop will apply to its animation.

   Verse

   ```
        # The type of animation easing to apply to the RootProp's movement. The easing type
        # changes the speed of the animation based on its animation curve.
        @editable {ToolTip := MoveEaseTypeTip}
        MoveEaseType:move_to_ease_type = move_to_ease_type.EaseInOut
   ```

    # The type of animation easing to apply to the RootProp&#39;s movement. The easing type
   # changes the speed of the animation based on its animation curve.
   @editable {ToolTip := MoveEaseTypeTip}
   MoveEaseType:move_to_ease_type = move_to_ease_type.EaseInOut

## Building an Animation with Keyframes

To build animations in code, you’re going to use [keyframes](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#keyframe). Animations are made from one or more keyframes, and each keyframe specifies an object's values at specific points in the animation. By building an animation using keyframes, you can specify multiple points for your prop to move, rotate, or even scale to.

Keyframes have five values. The `DeltaLocation`, `DeltaRotation`, and `DeltaScale` specify the changes in each value the prop makes from the start to the end of the keyframe. There’s also `Time`, or the amount of time in seconds the animation takes, and `Interpolation`, or the interpolation mode for the keyframe. An example keyframe might look like this:

Verse

```
    # An example keyframe.
    KeyFrame := keyframe_delta:

        # The target position of the `creative_prop`. This is the difference between the starting and ending translation of the prop.
        DeltaLocation := EndTransform.Translation - StartTransform.Translation,

        # The target rotation for the `creative_prop` to rotate to.
        DeltaRotation := EndTransform.Rotation,

        # The target scale for the `creative_prop`. Scale is multiplicative to the starting Scale of the `creative_prop`
```

Follow these steps to build an animation using keyframes:

## Overloading Functions

While the `MoveToEase()` function you wrote is useful, it can be complicated to pass such a large number of variables to the function each time you want to call it. There might be situations where you only want to change one part of the prop’s transform, such as the translation or rotation, and it would be helpful to have a simpler function to call in this case.

To solve this, you can take advantage of [function overloading](https://dev.epicgames.com/documentation/fortnite/verse-glossary#overload). By overloading the `MoveToEase()` function, you can set up multiple methods with the same name to handle different types of inputs. Follow the steps below to set up your overloaded functions.

With your methods set up, it’s time to get moving! In the next section, you’ll translate props to make moving platforms!

- [![3. Translating Props](https://dev.epicgames.com/community/api/documentation/image/a15f96c1-838a-4141-bbbd-c4cabd5a5ebd?resizing_type=fit&width=640&height=640)

  3. Translating Props

  Use translation with Verse to set up obstacles for a Fall Guys course.](https://dev.epicgames.com/documentation/fortnite/animating-prop-movement-3-translating-props-in-verse)

## Complete Code

Here is the complete code built in this section:

### movement_behaviors.verse

Verse

```
# This file stores functions common to animating creative props using keyframes.
# It also defines the move_to_ease_type enum to help in building animations.
using { /Fortnite.com/Devices }
using { /UnrealEngine.com/Temporary/SpatialMath }
using { /Fortnite.com/Characters}
using { /Fortnite.com/Devices/CreativeAnimation }

# Represents the different movement easing types.
move_to_ease_type<public> := enum {Linear, Ease, EaseIn, EaseOut, EaseInOut}
```
