## https://dev.epicgames.com/documentation/en-us/fortnite/using-air-vent-device-design-examples-in-fortnite-creative

# Air Vent Device Design Examples

Find some suggestions for how to build Air Vent devices into your gameplay.

![Air Vent Device Design Examples](https://dev.epicgames.com/community/api/documentation/image/0c80ffa7-8bb0-4e97-a34f-d08f3065b10c?resizing_type=fill&width=1920&height=335)

The **Air Vent** device tosses players or vehicles into the air, adding a whole new dimension to to gameplay. Keep going for a couple of examples of how you can use this device:

- [Bounce for Points Mini-Game](https://dev.epicgames.com/documentation/fortnite/using-air-vent-device-design-examples-in-fortnite-creative)
- [Vehicle Big Air Competition](https://dev.epicgames.com/documentation/fortnite/using-air-vent-device-design-examples-in-fortnite-creative)

## Bounce for Points Mini-Game

The goal in this mini-game is for players to earn as many points as possible before time runs out by grabbing the collectible objects that appear in the play space.
Varying settings on the air vents, along with unexpected placements, will pack the game with entertaining surprises.

### Devices Used

You will need the following devices:

- 8 x [Player Spawner devices](https://dev.epicgames.com/documentation/fortnite/using-player-spawn-pad-devices-in-fortnite-creative)
- 13 x **Air Vent** devices
- 3 x [**Collectible Object** devices](using-collectible-object-devices-in-fortnite-creative)
- 3 x [Timer devices](https://dev.epicgames.com/documentation/fortnite/using-timer-devices-in-fortnite-creative)*

### Build It Yourself

Start by building a simple arena that includes:

- A ground area where you can place Air Vent devices.
- An elevated area surrounding the ground area where players can spawn in. This encourages them to literally jump into the game.
- Angled areas under the spawning points where you can place additional air vents. This makes their start a little more fun!

[![Start with a simple arena.](https://dev.epicgames.com/community/api/documentation/image/6bffedb7-c939-43ec-8789-02b763e6cff9?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/6bffedb7-c939-43ec-8789-02b763e6cff9?resizing_type=fit)

### Add Air Vents

You can use the default values for the air vents, or you can adjust movement settings, such as **Knockup Force Multiplier**, to add more variety or make the higher value coins more challenging to reach.

[![Vary settings from air vent to air vent.](https://dev.epicgames.com/community/api/documentation/image/d2a3a39e-8464-4022-af41-fa7019292858?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/d2a3a39e-8464-4022-af41-fa7019292858?resizing_type=fit)

### Add Player Spawners

Place **Player Spawner** devices above the arena. There are eight player spawners in this example. Use enough spawners to accommodate the number of players you want to support.

### Add Collectible Objects

This example uses three **Collectible Object** devices — a Bronze Coin, a Silver Coin, and a Gold Coin — with higher points awarded for each coin type. The objects are suspended above the air vents so that players have to use the vent boosts to reach them.

Play with the points awarded from each device to get the results you like!

You will also use three **Timer** devices later, and bind each collectible to a separate timer.

### Add Timers

### Bind Timers and Coins

Each collectible object is linked to its own timer, which is set to start a countdown when the object is collected. When the timer completes the countdown, it sends an event back to the Collectible Object device telling it to respawn the coin.

To make the play more challenging, you can vary the respawn time for different coins, with longer respawns on the higher-value coins. This encourages players to go for lower-value objectives while they wait for the bigger prizes to respawn!

You will need to [bind](https://dev.epicgames.com/documentation/fortnite/getting-started-with-direct-event-binding-in-fortnite-creative) each coin device to a timer, then bind the timers to the coins.

### Modify Island Settings

The last step is to modify the [Island Settings](https://dev.epicgames.com/documentation/fortnite/understanding-island-settings-in-fortnite-creative).

1. Go to the **Islands Settings** tab.
2. Select the **Round** category, then the **End Condition** subcategory.
3. Set the **Time Limit** setting to **2 minutes**.

   [![Location of the Time Limit setting](https://dev.epicgames.com/community/api/documentation/image/11fe5894-9b3c-42b0-abd1-dcee2e182999?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/11fe5894-9b3c-42b0-abd1-dcee2e182999?resizing_type=fit)
4. Select the **Mode** category, then the **Victory Condition** subcategory.
5. Set the **Game Win Condition** setting to **Most Score Wins**. The player with the highest score wins the game.

   [![Location of the Game Win Condition setting](https://dev.epicgames.com/community/api/documentation/image/cc1320f3-fb8f-4f03-aed3-7d4530391534?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/cc1320f3-fb8f-4f03-aed3-7d4530391534?resizing_type=fit)
6. Select the **User Interface** category, then the **Scoreboard** subcategory.
7. Set the **First Scoreboard Column** setting to **Score**. This shows players their scores in the first column of the Scoreboard.

   [![](https://dev.epicgames.com/community/api/documentation/image/35d1ba0d-e692-483d-b865-0e278df0fde3?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/35d1ba0d-e692-483d-b865-0e278df0fde3?resizing_type=fit)

You've created the basic functionality for a mini-game based on the Air Vent device!

Try changing the Island Settings to customize how your mini-game plays, or experiment with adding weapons for even more fun!

## Vehicle Big Air Competition

An Air Vent device can also be used to **catapult vehicles** high into the air!

This mini-game example shows how you can use an air vent in combination with a few simple island settings to create a vehicle-jumping mini-game of your own. Create a dedicated vehicle-jumping game, or include these mechanics in your other island designs.

### Construct a Vehicle Jump

In this example, an Air Vent device is embedded into the ground so that vehicles can easily drive over it.

[![Set the air vent into the ground or road.](https://dev.epicgames.com/community/api/documentation/image/f3bc2303-ace4-4f55-a277-6a6dde2df38b?resizing_type=fit)](https://dev.epicgames.com/community/api/documentation/image/f3bc2303-ace4-4f55-a277-6a6dde2df38b?resizing_type=fit)

### Modify Island Settings

With this simple setup, you can pull off aerial tricks with a surprising number of vehicles. Try using different vehicle types to see what kinds of tricks your players can potentially do!
