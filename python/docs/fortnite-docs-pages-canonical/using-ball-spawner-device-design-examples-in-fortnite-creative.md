## https://dev.epicgames.com/documentation/en-us/fortnite/using-ball-spawner-device-design-examples-in-fortnite-creative

# Ball Spawner Device Design Examples

Learn how to create dodgeball- or soccer-type mini-games.

![Ball Spawner Device Design Examples](https://dev.epicgames.com/community/api/documentation/image/ce9422aa-f6cd-4035-a8c7-6c46daa479af?resizing_type=fill&width=1920&height=335)

The **Ball Spawner** device spawns a ball that can be knocked around by players or objects. A player can shove it, shoot it, or hit it with a pickaxe to knock it in a specific direction.

Keep going for a couple of examples of how you can use this device:

- [Dodgeball Last Player Standing](https://dev.epicgames.com/documentation/fortnite/using-ball-spawner-device-design-examples-in-fortnite-creative)
- [Soccer Score Mini-Game](https://dev.epicgames.com/documentation/fortnite/using-ball-spawner-device-design-examples-in-fortnite-creative)

## Dodgeball Last Player Standing

Did you know that the balls spawned by the Ball Spawner can be used to eliminate other players?

In this design example, you’ll learn how to create a four-player game where players bounce the ball to eliminate each other, and the last player standing wins!

### Devices Used

- 4 x [Player Spawner devices](https://dev.epicgames.com/documentation/fortnite/using-player-spawn-pad-devices-in-fortnite-creative)
- 1 x **Ball Spawner** device
- 1 x [**Damage Volume** device](using-damage-volume-devices-in-fortnite-creative)

### Build Your Own

Start by making a simple arena for the action, which will help keep the players focused on the ball.

[![](https://dev.epicgames.com/community/api/documentation/image/39bc748c-9d98-412b-8305-15581a9b86dd?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/39bc748c-9d98-412b-8305-15581a9b86dd?resizing_type=fit)

In this example, the walls of the game space are made from sloped pieces that roll the ball back into play, but you could make your walls any shape you choose!

### Add Player Spawners

Place a player spawner on one of the raised platforms at the corners of the arena.

[![](https://dev.epicgames.com/community/api/documentation/image/98d4a214-9217-40d4-bd00-f9b13027109d?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/98d4a214-9217-40d4-bd00-f9b13027109d?resizing_type=fit)

### Add the Ball Spawner

Add the Ball Spawner device over the center of the arena.

[![](https://dev.epicgames.com/community/api/documentation/image/314f1213-5a76-42aa-82f9-43b5ab427bcf?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/314f1213-5a76-42aa-82f9-43b5ab427bcf?resizing_type=fit)

In this example, the ball spawner is visible during gameplay so players have a reference point for where the ball will fall from. It is also turned upside down to allow the ball to fall freely.

A player has to use their pickaxe to propel the ball into another player, but if they don't time their swing well, the ball will touch them, and they are eliminated!

### Add a Damage Volume

To encourage players to jump into the arena and start bouncing the ball at their rivals, add a Damage Volume device that covers the player spawners.

The **Damage Volume** device is to encourage players to jump into the game. If they don't the damage volume will eliminate them. You can spell this out for the players in [onboarding](onboarding-players-in-fortnite-creative), or let them learn the hard way!

[![](https://dev.epicgames.com/community/api/documentation/image/353cf258-c2fc-42a4-a0c7-31d8d9a9bf6f?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/353cf258-c2fc-42a4-a0c7-31d8d9a9bf6f?resizing_type=fit)

### Configure the Island Settings

You have created your own dodgeball-style mini-game!

Try changing the Island Settings to see how you can adjust the gameplay, or add weapons into the arena for even more fun!

## Soccer Score Mini-Game

Ready for another simple ball-based game?

This soccer-style mini-game features a scoring system where the first team to earn five goals wins.

### Devices Used

- 4 x [Player Spawner devices](https://dev.epicgames.com/documentation/fortnite/using-player-spawn-pad-devices-in-fortnite-creative)
- 1 x **Ball Spawner** device
- 2 x [**Capture Area** devices](using-capture-area-devices-in-fortnite-creative)

### Build Your Own

Build a simple playing field that's big enough to allow player movement, but that will constrain player actions to the area.

In this example, the arena walls are made from sloped pieces that roll the ball back into play, but feel free to get creative when you shape your soccer field!

[![](https://dev.epicgames.com/community/api/documentation/image/1a932164-dcf7-42e7-86b1-1948e2e88163?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/1a932164-dcf7-42e7-86b1-1948e2e88163?resizing_type=fit)

Add a [**soccer goal prop**](using-prefabs-and-galleries-in-fortnite-creative) to each end of the field.

For a more authentic look, use the goal object from the **Sports Gallery** set in the **Pleasant Park** gallery.

[![](https://dev.epicgames.com/community/api/documentation/image/7c6efff5-c34a-4197-bdad-388a4b0e423a?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/7c6efff5-c34a-4197-bdad-388a4b0e423a?resizing_type=fit)

### Add Player Spawner Devices

### Add the Ball Spawner

### Add Capture Areas

Adding a capture area for each goal makes it possible for players to score by knocking the ball into the goal. Each team will have its own capture area (goal).

[![](https://dev.epicgames.com/community/api/documentation/image/b519e362-b5f1-4b61-8f1a-f57074a0c036?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/b519e362-b5f1-4b61-8f1a-f57074a0c036?resizing_type=fit)

*The goal for the blue team sits between the red team player spawners.*

[![](https://dev.epicgames.com/community/api/documentation/image/dd8290fd-42a9-4ae4-b559-5c11cd4d81f7?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/dd8290fd-42a9-4ae4-b559-5c11cd4d81f7?resizing_type=fit)

*The goal for the red team sits between the blue team player spawners.*

### Configure Island Settings

The final step in setting up this mini-game is to configure the Island Settings.

You have created your own soccer-style mini-game! Try changing the Island Settings to see how you can adjust the gameplay, or add weapons into the arena for more fun.
