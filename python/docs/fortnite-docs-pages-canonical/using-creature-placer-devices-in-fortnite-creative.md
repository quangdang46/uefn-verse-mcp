## https://dev.epicgames.com/documentation/en-us/fortnite/using-creature-placer-devices-in-fortnite-creative

# Creature Placer Devices

Place creatures at the exact location where you want them.

![Creature Placer Devices](https://dev.epicgames.com/community/api/documentation/image/2a3bd2c5-8288-48a7-b801-d6d300762fde?resizing_type=fill&width=1920&height=335)

The **Creature Placer** device does exactly what you'd expect it to do—it provides a way to set an exact location for where a creature will [spawn](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary). You can also specify which type of creature will spawn, when it will spawn, and when it will despawn.

**Looking for more inspiration?** See **[D-Launcher Device Design Examples](https://dev.epicgames.com/documentation/fortnite/dlauncher-device-design-examples-in-fortnite-creative)** to kick off your imagination!

For help finding the **Creature Placer** device, see [Using Devices](https://dev.epicgames.com/documentation/fortnite/using-devices-in-fortnite).

## Device Options

In its [default](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) state, when you place a Creature Placer on your island, a fiend will spawn immediately at game start. When the fiend is eliminated, a new fiend will not spawn.

You can configure this device with the following options.

Default values are **bold**.

| Option | Value | Description |
| --- | --- | --- |
| **Creature Type** | **Fiend**, Pick a creature | Determines the type of creature that will spawn. |
| **Activation Range** | **7 tiles**, Pick or enter an amount | Determines how close a player has to be to this device for it to activate. |
| **Spawn Effects Visibility** | **On**, Off | Determines whether device-related effects are played while spawning. |
| **Enable on Game Phase** | Never, Game Countdown, **Game Start** | Determines which [game phase](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) the device activates in. |
| **Despawn Type** | **Distance To Enemy**, Distance To Spawner, Do Not Despawn | Whether creatures should despawn when far away from the spawner, or when far away from any player. |
| **Despawn Range** | **9 tiles**, Pick a distance | Determines how far away (distance in tiles) creatures need to be to despawn, based on the Despawn Type. |
| **Spawn Only If Needed** | **On**, Off | Determines whether the spawner will wait for a previous spawned creature to be destroyed before spawning another one. |
| **Restore Player Shield on Elimination** | **On**, Off | Determines whether a player's shield is restored when that player eliminates a creature spawned by this device. |

## Direct Event Binding

Following are the [direct event binding](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) options for this device.

### Functions

A [function](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) listens for an event on a device then performs an action.

| Option | Description |
| --- | --- |
| **Enable When Receiving From** | This function enables the device when an event occurs. |
| **Disable When Receiving From** | This function disables the device when an event occurs. |

### Events

An [event](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) tells another device when to perform a function.

| Option | Description |
| --- | --- |
| **On Eliminated Send Event To** | When a creature is eliminated, an event is sent to the selected device, which triggers the selected function. |
| **On Spawned Send Event To** | When a creature is spawned, an event is sent to the selected device, which triggers the selected function. |

## Gameplay Examples Using Creature Placer

- [5 Rounds Of Econ Lessons](https://dev.epicgames.com/documentation/fortnite/5-rounds-of-econ-lessons-gameplay-example-in-fortnite-creative)
- [Dungeon Crawler](https://dev.epicgames.com/documentation/fortnite/dungeon-crawler-gameplay-example-in-fortnite-creative)
- [End of Round Team Swapping](https://dev.epicgames.com/documentation/fortnite/end-of-round-team-swapping-in-fortnite-creative)
- [Spawner 123](https://dev.epicgames.com/documentation/fortnite/spawner-123-in-fortnite-creative)
- [Top Scorer In Class](https://dev.epicgames.com/documentation/fortnite/top-scorer-in-class-in-fortnite-creative)
