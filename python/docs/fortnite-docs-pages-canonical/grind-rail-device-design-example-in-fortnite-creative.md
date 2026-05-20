## https://dev.epicgames.com/documentation/en-us/fortnite/grind-rail-device-design-example-in-fortnite-creative

# Grind Rail Device Design Example

Make a mini-game where players earn points by staying on the rails!

![Grind Rail Device Design Example](https://dev.epicgames.com/community/api/documentation/image/6468abec-62d7-4acd-b03e-30182f7a37ce?resizing_type=fill&width=1920&height=335)

Use the **Grind Rail** device to add fun to any island where players can jump on a rail and grind along.

## Grind Park Mini-Game

This design example shows you how to create a unique mini-game based on grinding the rails for points.

You'll also get some tips and tricks for ways to use this device.

### Devices Used

- Several [Grind Rail](using-grind-rail-devices-in-fortnite-creative) devices
- 3 x [Pulse Trigger](https://dev.epicgames.com/documentation/fortnite/using-pulse-trigger-devices-in-fortnite-creative) devices
- 4 x [Timer](https://dev.epicgames.com/documentation/fortnite/using-timer-devices-in-fortnite-creative) devices
- 1 x [Player Spawner](https://dev.epicgames.com/documentation/fortnite/using-player-spawn-pad-devices-in-fortnite-creative) device

### Build Your Own

This game is made up of grind rails placed on props of varying heights. The higher the rail, the more points a player can score by riding it for as long as possible!

To build the basic game mechanics, you will set up your rails, assemble them into a sliding playground, then add supporting props to hold them above the ground and move the rails on the props. Finally, you will add pulse triggers that inflict damage to players who don't avoid them.

[![](https://dev.epicgames.com/community/api/documentation/image/00d36f25-1c99-46be-9c36-e269853d576d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/00d36f25-1c99-46be-9c36-e269853d576d?resizing_type=fit)

### Add a Player Spawner

You can start the player wherever you want, but a good place to start is near the lowest rail. This is where the player will spawn initially as well as respawning after any eliminations. You can add it now, or wait and add it after the layout is done.

### Add the Grind Rails

1. Add a **Grind Rail** device.

   The arrows on the control points indicate the direction a player will move on the rail.
2. Rename the rail to **White Grind Rail**, then customize it:

   [![](https://dev.epicgames.com/community/api/documentation/image/18d6faeb-41a6-4ba4-af56-9878aa216c5e?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/18d6faeb-41a6-4ba4-af56-9878aa216c5e?resizing_type=fit)

   | Option | Value | Description |
   | --- | --- | --- |
   | **Rail Color** | White | This sets the color of the rail. |
   | **Allow Sprinting** | Off | Prevents a player from sprinting while on the rail. |
   | **Apply Fall Damage Immunity** | Off | Players can receive damage if they fall off the rail while grinding. Ouch. |

   Selecting the rail directly (not on either control point at the end of a rail) is how you can move or copy the rail.

   [![](https://dev.epicgames.com/community/api/documentation/image/3456d436-16b4-4ee3-b036-1a593ffdd180?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/3456d436-16b4-4ee3-b036-1a593ffdd180?resizing_type=fit)
3. Use the **control points** at either end of a rail to lengthen or shorten the rails.
4. You can only customize the **tangent intensity** on a control point.

   [![](https://dev.epicgames.com/community/api/documentation/image/b89a0da6-f2a0-4006-8490-5ea2f6d1fb02?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b89a0da6-f2a0-4006-8490-5ea2f6d1fb02?resizing_type=fit)

   Tangent intensity determines how sharp or rounded a curve on the rail is — the higher the number, the more rounded the curve.
5. Copy these points and place to add more points to a rail, then shape the rail by changing the tangent intensity in the control point settings or dragging the control points to change the rail shape.

   For more on adjusting the shapes of rails, see [**Grind Rail Devices**](using-grind-rail-devices-in-fortnite-creative) under **Shaping the Grind Rail**.
6. Adjust the length of each rail as described in the Grind Rail Devices doc by grabbing a control point at the end of the rail.
7. Copy and place the rail several more times, changing the color for each new rail and renaming it based on the color you select.

   [![](https://dev.epicgames.com/community/api/documentation/image/ab970129-c0ac-48a4-a8c2-a01b4aa7ef8c?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ab970129-c0ac-48a4-a8c2-a01b4aa7ef8c?resizing_type=fit)
8. Add turns and curves to each rail by adding and moving control points along the rail.

   It's easier to add more points from the end of the rail than from the start — otherwise you might get a bunch of control points piled up on each other!

   Any adjustments you make to a rail can be readjusted later if you change your mind about how to lay them out.

### Add Rail Supports

The next step is to add and customize rail support props.

Take a minute to work out which rails are going to be higher and harder to reach. This will inform both the support props you use and the score values you will assign to each rail. The higher rails will be harder for a player to reach and so should grant more points.

1. From the **Content** tab, select the **Galleries** category, then use the **search box** to filter for **primitive**.
2. Double-click the gallery to see the contents, then equip any individual props you want to use.

   [![](https://dev.epicgames.com/community/api/documentation/image/31a1f9ef-beef-4325-a007-edf748846877?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/31a1f9ef-beef-4325-a007-edf748846877?resizing_type=fit)
3. Once you place a primitive shape prop, you can change the color of the prop the same way you would customize a device. Note that **color** is the only thing you can customize for these props.

   [![](https://dev.epicgames.com/community/api/documentation/image/8bbfa2b3-5876-4f83-ac5b-f7b6c99608c0?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/8bbfa2b3-5876-4f83-ac5b-f7b6c99608c0?resizing_type=fit)
4. Color your props, or leave them all the original color.

   [![](https://dev.epicgames.com/community/api/documentation/image/ecafd898-5343-4a2b-a2f8-e34f110148d2?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/ecafd898-5343-4a2b-a2f8-e34f110148d2?resizing_type=fit)
5. Position the support props where you want them, then place the rails on them by grabbing a control point and placing it on top of the post.

   [![](https://dev.epicgames.com/community/api/documentation/image/cf4564c0-2a37-4f59-aeed-8725b08af698?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cf4564c0-2a37-4f59-aeed-8725b08af698?resizing_type=fit)

   Pay attention to which way the arrows on the Grind Rail are pointing, because the next step is much easier if you extend the rail in the direction that the arrows flow!
6. Place more support props where you want them, then copy the end control point of your grind rail and place it on top of the new support. The rail will automatically extend to reach the new control point you created. You can even move the new point up or down and the rail will adjust automatically.
7. Players will find it easier to jump to railings that are perpendicular to the rail they are sliding on, so where possible, create intersections that will challenge players to jump to a higher rail!

   [![](https://dev.epicgames.com/community/api/documentation/image/9a48b4b8-b605-46dd-b056-1222c2926717?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/9a48b4b8-b605-46dd-b056-1222c2926717?resizing_type=fit)
8. Position your rails at different heights.
9. Also add several large primitive boxes like the red ones above, making sure to place them next to your highest rail paths. You will use these when you're ready to add moving obstacles.

### Add the Timers

Adding a **Timer** device for each rail makes it possible to assign different award amounts for each second a player successfully slides along a rail.

### Bind Rails and Timers

[Direct event binding](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#direct-event-binding) is how devices communicate with each other. You will need to bind the rails to their timers.

Use your color naming to make sure each rail matches the right timer.

### Add Pulse Triggers

Remember those large primitive boxes you placed earlier? Each of these will be the base for a **pulse trigger** that makes riding the highest rails even more challenging!

The Pulse Trigger device sends a **damage pulse** through a custom volume. You can set these up to present moving obstacles, or volumes, that the player must avoid while riding the rails they overlap.

The player can navigate around the pulses to earn more points.

### Configure the Island Settings

The final step for this mini-game is to modify the **Island Settings**.

And there you have it — a simple but impressive mini-game that players will love!

## Design Tip

For more fun, try adding weapons or items to your map for an even wilder time riding the rails!
