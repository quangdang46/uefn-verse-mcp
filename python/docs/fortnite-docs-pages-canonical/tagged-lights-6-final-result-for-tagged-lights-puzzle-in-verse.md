## https://dev.epicgames.com/documentation/en-us/fortnite/tagged-lights-6-final-result-for-tagged-lights-puzzle-in-verse

# 6. Tagged Lights Final Result

Create a puzzle where the player has to find the right combination of lights on and off to spawn an item, using a device created with Verse.

![6. Tagged Lights Final Result](https://dev.epicgames.com/community/api/documentation/image/c4c72c38-af49-4233-9aa8-3540c17f113b?resizing_type=fill&width=1920&height=335)

###### Prerequisite topics

In order to understand and use the content on this page, make sure you are familiar with the following topics:

- [5. Detecting When the Puzzle Is Solved](https://dev.epicgames.com/documentation/fortnite/tagged-lights-5-detecting-when-the-puzzle-is-solved-in-verse)

In this last step of the [Tagged Lights Puzzle](https://dev.epicgames.com/documentation/en-us/uefn/tagged-lights-puzzle-in-verse) tutorial, you'll find the [complete script](https://dev.epicgames.com/documentation/fortnite/tagged-lights-6-final-result-for-tagged-lights-puzzle-in-verse) for the puzzle and [ideas](https://dev.epicgames.com/documentation/fortnite/tagged-lights-6-final-result-for-tagged-lights-puzzle-in-verse) to further change the example.

## Complete Script

The following code is the complete script for a reusable puzzle that requires the player to find the right combination of lights by toggling their state with buttons.

Verse

```
using { /Fortnite.com/Devices }
using { /Verse.org/Native }
using { /UnrealEngine.com/Temporary/Diagnostics }
using { /Verse.org/Simulation/Tags }
using { /Verse.org/Simulation }

# Derive from the `tag` class in the Verse.org/Simulation/Tags module to create a new Gameplay Tag.
puzzle_light := class(tag){}

log_tagged_lights_puzzle := class(log_channel){}
```

## On Your Own

By completing this tutorial, you’ve learned how to create a reusable puzzle using Verse that requires the player to find the right combination of lights by toggling their state with buttons.

Using what you’ve learned, try the following:

- Create more tags and use them to control the lights with a deterministic visual order.
- Use different initial conditions and solutions and add more buttons and lights to create more puzzles with the same setup.
- Control multiple types of devices with multiple types of user-interactable devices.
