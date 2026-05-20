## https://dev.epicgames.com/documentation/en-us/fortnite/tagged-lights-2-setting-up-the-level-in-verse

# 2. Setting Up the Level

Create a puzzle where the player has to find the right combination of lights on and off to spawn an item, using a device created with Verse.

![2. Setting Up the Level](https://dev.epicgames.com/community/api/documentation/image/dee6f8c9-6c39-4d23-be20-b3fe110b891b?resizing_type=fill&width=1920&height=335)

###### Prerequisite topics

In order to understand and use the content on this page, make sure you are familiar with the following topics:

- [1. Creating the Algorithm](https://dev.epicgames.com/documentation/fortnite/tagged-lights-1-creating-the-algorithm-in-verse)

By completing this step in the [Tagged Lights Puzzle](https://dev.epicgames.com/documentation/fortnite/tagged-lights-puzzle-in-verse) tutorial, you'll have set up your level with all the props and devices you'll need to create a puzzle where the player must find the right combination of lights on or off to solve.

This example uses the following props and devices.

- 1 x [Player Spawn Pad device](https://dev.epicgames.com/documentation/fortnite/using-player-spawn-pad-devices-in-fortnite-creative): This device defines where the player spawns at the start of the game.
- 4 x [Customizable Light devices](https://dev.epicgames.com/documentation/fortnite/using-customizable-light-devices-in-fortnite-creative): These are the lights used as the visual representation of the internal game state of the Verse-authored device. The device script will turn them on and off.
- 4 x [Button devices](https://dev.epicgames.com/documentation/fortnite/using-button-devices-in-fortnite-creative): The player uses the buttons to toggle sets of lights. The Verse-authored device listens to the buttons’ `InteractedWithEvent` to update the game state accordingly.
- 1 x [Item Spawner device](https://dev.epicgames.com/documentation/fortnite/using-item-spawner-devices-in-fortnite-creative): This is used to reward the player when the puzzle is solved.
- Props for walls, floors, and ceilings to create a dark room. This example uses pieces from the **Haunted** gallery, which you can find in the **Content Browser** under **Fortnite > Props > Haunted**.

Follow these steps to set up your level:

1. Create an enclosed area using walls, floors, and ceilings. Ensure the room is dark enough for lights to be easily visible.

   [![Create an enclosed area using the walls, floors, and ceilings](https://dev.epicgames.com/community/api/documentation/image/6bd7b946-8d5b-4275-8770-006f77230b83?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6bd7b946-8d5b-4275-8770-006f77230b83?resizing_type=fit)
2. Add 4 **Button devices** side by side in the enclosed area.
3. Add the **Player Spawn Pad device** for the player to spawn close to the buttons.
4. Add 4 **Customizable Light devices** pointing at a wall or a part of the room where the player can easily see them while interacting with the buttons.
5. Select each light in the **Outliner** to open its **Details** panel.
6. In the **Details** panel for each Customizable Light device:
7. Add the **Item Spawner device** in a spot that’s visible to the player when they solve the puzzle.
8. Select the Item Spawner device in the **Outliner** to open its **Details** panel.
9. In the **Details** panel for the Item Spawner device, under **User Options**:

   [![Modify the settings for the Item Spawner Device to only spawn an item when the device is enabled later](https://dev.epicgames.com/community/api/documentation/image/efbf5b8f-d307-434e-9eac-3700cd18b909?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/efbf5b8f-d307-434e-9eac-3700cd18b909?resizing_type=fit)
10. Create a new Verse device named **tagged_lights_puzzle** using [Verse Explorer](https://dev.epicgames.com/documentation/fortnite/verse-explorer-user-interface-reference-in-unreal-editor-for-fortnite), and drag the device into the level. (For steps on how to create a new device in Verse, see [Create Your Own Device Using Verse](https://dev.epicgames.com/documentation/fortnite/create-your-own-device-using-verse-in-unreal-editor-for-fortnite).)

    [![Create a new Verse device named tagged_lights_puzzle](https://dev.epicgames.com/community/api/documentation/image/2436c536-b0d1-4ec3-a3ef-fee48a9bbb01?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/2436c536-b0d1-4ec3-a3ef-fee48a9bbb01?resizing_type=fit)

Your level should look similar to this setup:

[![Complete level setup with devices and props](https://dev.epicgames.com/community/api/documentation/image/ef12cb0c-681f-45b6-b5a0-6726a05a5df3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ef12cb0c-681f-45b6-b5a0-6726a05a5df3?resizing_type=fit)

## Next Step

In the [next step](https://dev.epicgames.com/documentation/fortnite/tagged-lights-3-finding-the-lights-at-runtime-with-gameplay-tags-in-verse) of this tutorial, you’ll create a custom Verse tag and assign it to the lights to be able to find them all without having to set up references in the Editor.
