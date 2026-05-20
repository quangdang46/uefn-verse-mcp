## https://dev.epicgames.com/documentation/en-us/fortnite/tagged-lights-5-detecting-when-the-puzzle-is-solved-in-verse

# 5. Detecting When the Puzzle Is Solved

Create a puzzle where the player has to find the right combination of lights on and off to spawn an item, using a device created with Verse.

![5. Detecting When the Puzzle Is Solved](https://dev.epicgames.com/community/api/documentation/image/37a8c981-0d02-4cad-86df-bfbc9893a9b3?resizing_type=fill&width=1920&height=335)

###### Prerequisite topics

In order to understand and use the content on this page, make sure you are familiar with the following topics:

- [4. Toggling Lights with Buttons](https://dev.epicgames.com/documentation/fortnite/tagged-lights-4-toggling-lights-with-buttons-in-verse)

By completing this step in the [Tagged Lights Puzzle](tagged-lights-puzzle-in-verse) tutorial, you'll learn how to detect when the player solves the puzzle so you can spawn an item and prevent further interaction with the puzzle

## Detecting a Solved Puzzle

This section shows how to detect when the player solves the puzzle by finding the right combination of lights. When the puzzle is solved, the Item Spawner device should be enabled so that it can spawn its item.

Follow these steps to detect when the player solves the puzzle:

1. Add an editable `item_spawner_device` field named `ItemSpawner` to the `tagged_lights_puzzle` class, to represent the Item Spawner device.
    `@editable
   ItemSpawner : item_spawner_device = item_spawner_device{}`
2. Next, define what state the lights should be in to solve the puzzle. Since the representation of the lights’ state is a `logic` array, the solved state of the lights should also be a `logic` array to easily compare the two. Create an editable `logic` array field named `SolvedLightsState` to the `tagged_lights_puzzle` class. In this example, the player must turn on all the lights to solve the puzzle, so initialize each element with the value `true` to represent the light being on.
    `@editable
   SolvedLightsState : []logic = array{true, true, true, true}`
3. Save the file in Visual Studio Code.
4. In the UEFN toolbar, click **Build Verse Scripts** to update your Verse device in the level.
5. In the **Outliner**, select the **tagged_lights_puzzle** to open its **Details** panel.
6. In the Details panel, set the **Item Spawner** property to the Item Spawner device that’s in the level.
7. Next, develop the code that checks if the current `LightsState` matches the `SolvedLightsState`. Add a new method named `IsPuzzleSolved()` to the `tagged_lights_puzzle` class. This method should succeed if the puzzle is solved and fail if it’s not, to let its caller know the result of the check. This means the method should be marked as failable with the `decides` specifier. Since the method has the `decides` specifier, it must also have the `transacts` specifier, which means the actions performed by this method can be rolled back (as if the actions were never performed), if there’s a failure anywhere in the method.

   Verse

   ```
        IsPuzzleSolved()<decides><transacts> : void =
            Logger.Print(“Checking if puzzle is solved”)
   ```

    IsPuzzleSolved()&lt;decides&gt;&lt;transacts&gt; : void =
   Logger.Print(“Checking if puzzle is solved”)

   Verse uses success / failure for decision-making. For more details on how Verse uses failure, see Failure.
8. When should the device check if the puzzle has been solved? The best time is whenever the `LightsState` array has just been updated, which happens inside the `ToggleLights()` method. Once the `for` expression finishes updating the `LightsState` array, call the `IsPuzzleSolved[]` method to determine whether the puzzle is solved and so spawn an item (by calling `ItemSpawner.Enable()`). Since `IsPuzzleSolved[]` is a failable expression (which is why the method has the `[]` instead of `()` when you call it) it must be called in a failure context. In this example, the failure context is an if expression so you can conditionally execute expressions based on whether the puzzle is solved.

   Verse

   ```
        ToggleLights(LightIndices : []int) : void =
            for:
                LightIndex : LightIndices
                IsLightOn := LightsState[LightIndex]
                Light := Lights[LightIndex]
            do:
                Logger.Print("Turning light at index {LightIndex} {if (IsLightOn?) then "Off" else "On"}")
                NewLightState :=
                    if (IsLightOn?):
                        Light.TurnOff()
   ```
9. Next, make the `IsPuzzleSolved()` method detect if the puzzle is solved. Since `IsPuzzleSolved()` is a failure context, you can use failable expressions in the method body without needing to use another failure context, like an `if` expression. In this case, you will need to check if the state of every light is the same as the solved puzzle state. To test if two `logic` values are the same, you can use the equals operator `=`, which is a failable expression. The first time two values you’re checking aren’t the same, the expression fails so then the method fails and returns to its caller’s context (in this case, the `if` expression in the `ToggleLights()` method).

   Verse

   ```
        IsPuzzleSolved()<decides><transacts> : void =
            Logger.Print(“Checking if puzzle is solved”)

            for:
                LightIndex -> IsLightOn : LightsState
                IsLightOnInSolution := SolvedLightsState[LightIndex]
            do:
                IsLightOn = IsLightOnInSolution
   ```

    IsPuzzleSolved()&lt;decides&gt;&lt;transacts&gt; : void =
   Logger.Print(“Checking if puzzle is solved”)
   for:
   LightIndex -&gt; IsLightOn : LightsState
   IsLightOnInSolution := SolvedLightsState[LightIndex]
   do:
   IsLightOn = IsLightOnInSolution
10. Save the changes in Visual Studio Code.
11. In the UEFN toolbar, click **Build Verse Scripts** to compile your code.
12. Click **Play** in the UEFN toolbar to playtest the level.

When you playtest your level with the settings shown in this example, interacting with all the buttons once should solve the puzzle and spawn the item.

[![Player interacting with buttons to find the right combination of lights to solve the puzzle and spawn an item](https://dev.epicgames.com/community/api/documentation/image/d99cbf12-2d55-4e70-8bce-486602a444c7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d99cbf12-2d55-4e70-8bce-486602a444c7?resizing_type=fit)

## Removing Button Interaction when Puzzle Is Solved

After the player has completed the puzzle, they shouldn’t be able to interact with the buttons or turn the lights on / off. This section shows how to unsubscribe from an event so your event handler isn’t called anymore when a player interacts with the button.

When you call `Subscribe()` on a device event, the function call has a `cancelable` result. Calling `Cancel()` on a `cancelable` variable unsubscribes the function handling the event, so that the function will no longer be called when the event is dispatched.

Follow these steps to remove button interactions once the puzzle is solved:

With the default properties, interacting with all buttons once should solve the puzzle, spawn the item, and disable further button interactions.

## Next Step

In the [last step](https://dev.epicgames.com/documentation/fortnite/tagged-lights-6-final-result-for-tagged-lights-puzzle-in-verse) of this tutorial, you can see the complete script for this tutorial and ideas to further change the example.
