## https://dev.epicgames.com/documentation/en-us/fortnite/animating-prop-movement-5-scaling-props-in-verse

# 5. Scaling Props

Learn how to manipulate object scales with Verse so they grow and shrink.

![5. Scaling Props](https://dev.epicgames.com/community/api/documentation/image/b022dcba-0b0c-4890-a5b6-5aafe9f613a1?resizing_type=fill&width=1920&height=335)

Sometimes during platformers, you’ll encounter obstacles that change their dimensions. These could be platforms that grow and shrink in size, or get taller or shorter along a certain axis. When an object’s dimensions are modified this way, it’s called modifying its [scale](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#scale).

An object's scale tells you how much to multiply each of its dimensions, relative to itself. Normally, objects have a scale of `{X := 1.0, Y := 1.0, Z := 1.0}`. If you double the `Z` value of an object’s scale, it becomes twice as tall. If you half it, half as tall.

Scale is the final part of the transform puzzle. In this section, you’ll learn how to manipulate scale to create objects that grow and shrink to different sizes.

## Making Props that Scale

Follow these steps to build the code that scales your props:

1. Create a new Verse class named `scaling_prop` that inherits from `movable_prop` using **Verse Explorer**. Add the `<concrete>` specifier to this class to expose its properties to UEFN.

   Verse

   ```
        # A prop that scales toward either a given scale or a Creative prop's scale.
        scaling_prop<public> := class<concrete>(movable_prop):
   ```

    # A prop that scales toward either a given scale or a Creative prop&#39;s scale.
   scaling_prop&lt;public&gt; := class&lt;concrete&gt;(movable_prop):
2. Add the `using { /Fortnite.com/Devices/CreativeAnimation }` and `using { /UnrealEngine.com/Temporary/SpatialMath }` statements to the top of the file to import these modules. You’ll need these to animate your prop. The tooltips used in this section are also included here.

   Verse

   ```
        using { /Fortnite.com/Devices }
        using { /Fortnite.com/Devices/CreativeAnimation }
        using { /Verse.org/Simulation }
        using { /UnrealEngine.com/Temporary/SpatialMath }

        MatchScaleTargetTip<localizes>:message = "The optional position to move to World Space. Use this if you do not want to set a MoveTarget."

        # A prop that scales toward either a given scale or a Creative prop's scale.
        scaling_prop<public> := class<concrete>(movable_prop):
   ```

    using { /Fortnite.com/Devices }
   using { /Fortnite.com/Devices/CreativeAnimation }
   using { /Verse.org/Simulation }
   using { /UnrealEngine.com/Temporary/SpatialMath }
   MatchScaleTargetTip&lt;localizes&gt;:message = &quot;The optional position to move to World Space. Use this if you do not want to set a MoveTarget.&quot;
   # A prop that scales toward either a given scale or a Creative prop&#39;s scale.
   scaling_prop&lt;public&gt; := class&lt;concrete&gt;(movable_prop):
3. At the top of the `scaling_prop` class definition, add the following fields.
4. Your final class definition should look like this:

   Verse

   ```
        using { /Fortnite.com/Devices }
        using { /Fortnite.com/Devices/CreativeAnimation }
        using { /Verse.org/Simulation }
        using { /UnrealEngine.com/Temporary/SpatialMath }

        MatchScaleTargetTip<localizes>:message = "The optional position to move to World Space. Use this if you do not want to set a MoveTarget."

        # A prop that scales towards either a given scale or a creative prop's scale.
        scaling_prop<public> := class<concrete>(movable_prop):
   ```
5. Since you already set up the `Move()` function that moves your prop in `movable_prop`, you can override it in this class. Override the `Move()` function in your `scaling_prop` class. In `Move()`, first, check if the `MatchScaleTarget` is set and save it in a variable `ScaleToMatch`. If so, set the `TargetScale` to the `ScaleToMatch`, then call `MoveToEase()`, passing in the `TargetScale`, the `MoveDuration`, the `MoveEaseType`, and `animation_mode.OneShot`. This is the `MoveToEase()` function you overloaded earlier that only modifies the scale.

   Verse

   ```
        # Scale the RootProp toward the ScaleTarget, or MatchScaleTarget if one is set.
        Move<override>()<suspends>:void=
            # Set the TargetScale to the MatchScaleTarget if it is set.
            if:
                ScaleToMatch := MatchScaleTarget?.GetTransform().Scale
            then:
                set TargetScale = ScaleToMatch

                # Call MoveToEase to start scaling the prop. The OneShot animation mode will play the animation once.
                RootProp.MoveToEase(MoveDuration, TargetScale, MoveEaseType, animation_mode.OneShot)
   ```

    # Scale the RootProp toward the ScaleTarget, or MatchScaleTarget if one is set.
   Move&lt;override&gt;()&lt;suspends&gt;:void=
   # Set the TargetScale to the MatchScaleTarget if it is set.
   if:
   ScaleToMatch := MatchScaleTarget?.GetTransform().Scale
   then:
   set TargetScale = ScaleToMatch
   # Call MoveToEase to start scaling the prop. The OneShot animation mode will play the animation once.
   RootProp.MoveToEase(MoveDuration, TargetScale, MoveEaseType, animation_mode.OneShot)
6. If you didn’t set a `MatchScaleTarget`, then you need to iterate through your `ScaleTargets` array. In a `for` expression, iterate through each `ScaleTarget` in `ScaleTargets` and set the `TargetScale` to the `ScaleTarget`. Then call `MoveToEase()`, passing the same values as before. Your complete `Move()` function should look like this:

   Verse

   ```
        # Scale the RootProp toward the ScaleTarget, or MatchScaleTarget if one is set.
        Move<override>()<suspends>:void=

            # Set the TargetScale to the MatchScaleTarget if it is set.
            if:
                ScaleToMatch := MatchScaleTarget?.GetTransform().Scale
            then:
                set TargetScale = ScaleToMatch

                # Call MoveToEase to start scaling the prop. The OneShot animation mode will play the animation once.
   ```
7. In your `prop_animator` device class, add a new editable array of `scaling_prop` named `ScalingProps`. Add another `for` expression to `OnBegin()` that loops through all the scaling props and calls `Setup()` on them. Your updated `prop_animator` class should look like this:

   Verse

   ```
        using { /Fortnite.com/Devices }
        using { /Verse.org/Simulation }
        using { /UnrealEngine.com/Temporary/Diagnostics }

        TranslatingPropsTip<localizes>:message = "The props that translate (move) using animation."
        RotatingPropsTip<localizes>:message = "The props that rotate using animation."
        ScalingPropsTip<localizes>:message = "The props that scale using animation."

        # Coordinates moving props through animation by calling each prop's Setup() method.
        prop_animator := class(creative_device):
   ```
8. Save your code and compile it.

## Linking Props to Devices

Back in the editor, delete some of the props after the rotating props section but before the raised blocks to create another gap. Add a **FG01 Punch Glove** to your level. Name the glove **ScalingGlove**. Position the glove in the middle of the gap, and rotate it so that it’s facing up.

[![The puncing glove prop that scales up and down](https://dev.epicgames.com/community/api/documentation/image/6d6f5603-11a0-4eae-8821-6b8fb61615b5?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6d6f5603-11a0-4eae-8821-6b8fb61615b5?resizing_type=fit)

*Setup of the punching glove. The glove scales up to create an elevator to raise players.*

Select your **prop animator** in the **Outliner**, and add an array element to `ScalingProps` for your glove. Assign the prop with the following values:

| Option | Value | Explanation |
| --- | --- | --- |
| **ScaleTargets** | {1.0, 2.0, 1.0}, {1.0, 1.0, 1.0} | This prop will scale to twice its dimensions on the Y-axis, then scale back to its starting dimensions. Note that since the prop is rotated, the Y-axis now the local "up" of the prop. |
| **RootProp** | Assign to prop you’re animating. | This is the prop you’re animating. |

Push your changes, then check out your props! Try varying the different scales to get different dimensions, and try scaling other props to create different scenarios!

## Next Up

In the next section, you’ll combine movement, rotation, and scale to create props that can do all three!

- [![6. Combining Movement, Rotation, and Scale](https://dev.epicgames.com/community/api/documentation/image/d6d62e48-faeb-4c2c-9813-430e0dbf9c23?resizing_type=fit&width=640&height=640)

  6. Combining Movement, Rotation, and Scale

  Time to combine different aspects of your moving props with Verse to build a Fall Guys obstacle course.](https://dev.epicgames.com/documentation/fortnite/animating-prop-movement-6-combining-movement-rotation-and-scale-in-verse)

## Complete Code

Here is the complete code built in this section:

### scaling_prop.verse

Verse

```
using { /Fortnite.com/Devices }
using { /Fortnite.com/Devices/CreativeAnimation }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/SpatialMath }

MatchScaleTargetTip<localizes>:message = "The optional position to move to World Space. Use this if you do not want to set a MoveTarget."

# A prop that scales towards either a given scale or a creative prop's scale.
scaling_prop<public> := class<concrete>(movable_prop):
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

# Coordinates moving props through animation by calling each prop's Setup() method.
prop_animator := class(creative_device):
```
