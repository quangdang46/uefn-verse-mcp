## https://dev.epicgames.com/documentation/en-us/fortnite/make-a-soccer-game

# Make a Soccer Game

Make a soccer game that uses the built-in physics of UEFN.

![Make a Soccer Game](https://dev.epicgames.com/community/api/documentation/image/b1cca7d2-a73c-42d2-8cff-c66112f7cb6c?resizing_type=fill&width=1920&height=335)

Follow the steps below to create your very own physics-enabled soccer game, where players use their pickaxe to get the ball into their opponents' goal:

## Set Up the Project

## Import the Soccer Ball

1. Download a soccer ball asset from your preferred asset marketplace. In this example, a .glb asset is used. It contains a static mesh, texture and material instance.

   [![](https://dev.epicgames.com/community/api/documentation/image/f56bf1de-5518-4f6a-875c-774dd2e614ac?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f56bf1de-5518-4f6a-875c-774dd2e614ac?resizing_type=fit)

   [Soccer Ball](https://sketchfab.com/3d-models/soccer-ball-88590cf1e42e44bfb85ce3b6b1959648) by [tinmanjuggernaut](https://sketchfab.com/tinmanjuggernaut) on Sketchfab, used under the [Sketchfab Standard License](https://sketchfab.com/licenses).
2. Import the ball by dragging the .glb file into your **Content Browser**. You can leave the default settings.

   [![800](https://dev.epicgames.com/community/api/documentation/image/f7cda6f9-6a64-4aab-815c-8eb9ea386e20?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f7cda6f9-6a64-4aab-815c-8eb9ea386e20?resizing_type=fit)
3. Double-click the **static mesh**to open the asset for editing.

   [![](https://dev.epicgames.com/community/api/documentation/image/4fd42d45-dd81-4e24-b4af-028a75ac1037?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/4fd42d45-dd81-4e24-b4af-028a75ac1037?resizing_type=fit)
4. In the viewport, select **Show** and check **Simple Collision**.
5. If there is collision already, delete it.

   [![](https://dev.epicgames.com/community/api/documentation/image/75905301-eb07-4b11-b0ed-0a95948c2905?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/75905301-eb07-4b11-b0ed-0a95948c2905?resizing_type=fit)

   Removing collision from the static mesh
6. From the **Collision** menu in the top ribbon, select **Add Sphere Simplified Collision**.

   [![](https://dev.epicgames.com/community/api/documentation/image/c09042b8-274f-4b97-8629-f9808aa38f7a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/c09042b8-274f-4b97-8629-f9808aa38f7a?resizing_type=fit)
7. In the **Collision** settings of the **Details** panel, set:

   |  |
   | --- |
   | Radius - **102.0** |
   | Collision Preset - **Block All** |
   | Center - **0 on all axes** |
8. The collision should now be visible. Save your static mesh.

   [![](https://dev.epicgames.com/community/api/documentation/image/87af1bcd-d5b2-42e9-99df-80ad8360381a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/87af1bcd-d5b2-42e9-99df-80ad8360381a?resizing_type=fit)

## Create the Soccer Ball Prop

## Add Soccer Game Elements

## Set Up Devices

Currently, the devices that work with **Physics** are all located in the **Fortnite > Devices > !Experimental** folder.

## Make a Game Manager Using Verse

Using Verse is the quickest and simplest way to manage your game, so let's create a Game Manager! For more information on how to create a Verse device, check out [Create Your Own Device Using Verse](https://dev.epicgames.com/documentation/uefn/create-your-own-device-using-verse-in-unreal-editor-for-fortnite).

Create a new Verse file and name it **game_manager.verse**. Double-click the file to open it in VS Code.

Add the following code to the file:

Verse

```
using { /Fortnite.com/Devices }
using { /Verse.org/Simulation }
using { /UnrealEngine.com/Temporary/Diagnostics }
using { /UnrealEngine.com/Temporary/SpatialMath }

# A Verse-authored creative device that can be placed in a level
game_manager := class(creative_device):
```

Compile the code and save your project.

You may need to tweak the positions of hiding and resetting the ball.

In UEFN, place the Verse device you just created in the scene and connect all the editable variables to your devices.

[![](https://dev.epicgames.com/community/api/documentation/image/eed61d9d-6211-4034-a520-fbfa4f81f33d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/eed61d9d-6211-4034-a520-fbfa4f81f33d?resizing_type=fit)

Start a session or push all changes to the Live Edit session and verify:

- The ball is moving when you push into it or hit it with the pickaxe.
- When you push the ball into the goal, a HUD message pops up, the score changes, and the ball resets to the center of the field.

Enjoy your new soccer game!

Experiment by adding more balls, more devices, changing the scale, etc.! Here's an example of a modified soccer game:

[![](https://dev.epicgames.com/community/api/documentation/image/d80d1f83-3ac8-4bef-b146-c86bfc123cfd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d80d1f83-3ac8-4bef-b146-c86bfc123cfd?resizing_type=fit)
