## https://dev.epicgames.com/documentation/en-us/fortnite-creative/using-player-spawn-pad-devices-in-fortnite-creative

# Player Spawner Devices

Use Player Spawn Pad Devices to spawn players onto your island.

![Player Spawner Devices](https://dev.epicgames.com/community/api/documentation/image/eed2e11a-e865-4f73-907a-67c6898ae017?resizing_type=fill&width=1920&height=335)

The **Player Spawner** device spawns the player at any location on their island.his device can only spawn one player. You will need to place individual spawners for islands with multiple players. Otherwise, they will always fall from the sky and have to parachute down.For help on how to find the **Player Spawner** device, see **[Using Devices](https://dev.epicgames.com/documentation/fortnite/using-devices-in-fortnite)**.

If you're using multiple copies of a device on an island, it can be helpful to [rename](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#rename-a-device) them. You can choose names that relate to each device's purpose, so it's easier to remember what each one does.

## Device Options

You can configure this device with the following options.

Default values are **bold**.

| Option | Value | Description |
| --- | --- | --- |
| **Player Team** | None, **Any**, Pick a team | Determines which team [spawns](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#spawning) on this pad. |
| **Visible in Game** | **On**, Off | Determines whether the spawner is visible during games. |
| **Use as Island Start** | **On**, Off | Determines whether or not a spawner can be used when players are spawning in to the island during the [Pre-Game phase](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#pre-game-phase). |
| **Enabled During Phase** | **Always**, None, Create Only, Pre-Game Only, Gameplay Only | Determines the [game phases](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#game-phase) during which this device will be [enabled](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) during which the device will be enabled. |
| **Player Class** | **Any**, No Class, Pick a team | Determines which class can activate the device. |
| **Priority Group** | **Don't Override**, Pick a number | Determines the priority in which spawners will be used. Use the arrows to pick a number, or click in the field and type in a number. If all Primary spawners are unavailable, players will spawn on Secondary spawners and the Tertiary. |
| **Play Audio** | **No**, Yes, Only If Visible | Determines whether the device should play audio effects. |
| **Enemy Range Check** | **None**, Pick a range | If an enemy is within this radius, you can prefer not to spawn at this location. If no other locations are suitable, the player may still spawn here. |
| **Display Enemy Range** | Off, On, **When Near** | Visualizes the **Enemy Range Check** option value. The location sphere will never show while playing, only during Create mode. |
| **Respawn Alive Players** | **Yes**, No | If a **Respawn at Player Spawner** function is triggered, this determines if players who are alive are also respawned. |

### User Options

You can configure these options for this device under the **User Options** category.

| Option | Value | Description |
| --- | --- | --- |
| **Player Team** | **Any**, None, Team Index | Only players on this team can spawn from this pad. |
| **User as Island Start** | **On**, Off | Determines whether or not a spawner can be used when players are spawning into the island during the Pre-Game phase. |
| **Visible in Game** | **On**, Off | Determines whether the spawner is visible during games. |
| Advanced |  |  |
| --- | --- | --- |
| **Enabled During Phase** | **Always**, Pre-Game Only, Gameplay Only, Create Only. | Determines the game phases during which the device will be enabled. |
| **Player Class** | **Any**, Class Slot, No Class | Only players on this class can spawn from this spawner. |
| **Priority Group** | **Don't Override**, Enter a priority number. | Determines the priority in which spawners will be used. The lower the better. |
| **Play Audio** | **No**, Yes, Only if Visible | Determines whether the device should play audio effects. |
| **Enemy Range Check** | Enter a range in meters | If the enemy is within this radius, prefer to not spawn at this location. If no other locations are suitable, players may still spawn here. |
| **Display Enemy Players** | **When Near**, Off, On | This is a debug feature to visualize the **Enemy Range Check** option. The sphere will never show while player and only appears during **Edit** mode. |
| **Respawn Alive Players** | **On**, off | Determines whether or not we respawn players that are alive when the **Respawn at Player** spawner is called. |

## Direct Event Binding

Following are the [direct event binding](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#direct-event-binding) options for this device.

### Functions

A [function](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#function) listens for an event on a device then performs an action.

| Option | Description |
| --- | --- |
| **Enable When Receiving From** | Enables the device when an event occurs. |
| **Disable When Receiving From** | Disables the device when an event occurs. |
| **Spawn Player When Receiving From** | Spawns a player at this spawner, or respawns an existing player, when an event occurs. |

### Events

An [event](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#event) tells another device when to perform a function.

| Option | Description |
| --- | --- |
| **On Player Spawned Send Event To** | When a player spawns or respawns from this spawner, this sends an event to the selected device, which triggers the selected function. |
| **On Spawn Failed Send Event To** | When a player would spawn or respawn from this spawner, but the spawner is invalid or ineligible for spawning, this sends an event to the selected device, which triggers the selected function. |

## Gameplay Examples

- [Loadout Lobby](loadout-lobby-in-fortnite-creative)
- [Tug of War](tug-of-war-in-fortnite-creative)
