## https://dev.epicgames.com/documentation/en-us/fortnite/using-player-checkpoint-devices-in-fortnite-creative

# Player Checkpoint Devices

This device sets a player's spawn point when activated, and can also be used to clear player inventories.

![Player Checkpoint Devices](https://dev.epicgames.com/community/api/documentation/image/f2a04700-1ae3-4c76-9beb-e386c3897857?resizing_type=fill&width=1920&height=335)

The **Player Checkpoint Pad** sets a player's spawn point when activated and can also be used to clear player inventories.

  For help on how to find the Player Checkpoint device, see [Using Devices](https://dev.epicgames.com/documentation/fortnite/using-devices-in-fortnite).

## Device Options

This device has some basic functionality, like playing sound effects and resetting inventories.

The default values are bold.

You can configure this device with the following options.

| Option | Value | Description |
| --- | --- | --- |
| **Visible in Game** | **On**, Off | Determines whether the device is visible during the game. This does affect its collision properties. |
| Reset Inventory | Yes, No | Determines whether the player's inventory is reset when they activate the checkpoint. |
| **Enabled During Phase** | None, **All**, Create Only, Game Countdown Only, Gameplay Only | Determines the game phases during which the device will be enabled. |
| **Activating Team** | **Any**, Pick a team | Determines which team can activate the device. |
| **Play Activate FX** | **On**, Off | Determines whether the device plays VFX and SFX when stepped on. |
| **Allowed Class** | No Class, **Any**, Pick a class | Determines which class can activate the device. |

## Direct Event Binding

### Functions

A [function](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#function) listens for an event on a device then performs an action.

| Option | Description |
| --- | --- |
| **Enable When Receiving From** | Enables the device when an event occurs. |
| **Disable When Receiving From** | Disables the device when an event occurs. |
| **Activate When Receiving From** | Registers this checkpoint to the activating player when an event occurs. |

### Events

An [event](https://dev.epicgames.com/documentation/en-us/fortnite-creative/fortnite-creative-glossary#event) tells another device when to perform a function.

| Option | Description |
| --- | --- |
| **On First Activation Per Player Transmit On** | Sends an event each time a new player activates the checkpoint for the first time. |
| **On First Activation Transmit On** | Sends an event the first time the checkpoint is activated by any player. |
