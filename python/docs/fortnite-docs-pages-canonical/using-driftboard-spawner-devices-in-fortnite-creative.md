## https://dev.epicgames.com/documentation/en-us/fortnite/using-driftboard-spawner-devices-in-fortnite-creative

# Driftboard Spawner Devices

Race through the air on a Driftboard!

![Driftboard Spawner Devices](https://dev.epicgames.com/community/api/documentation/image/4369de60-d0cf-4241-acc2-bdf7a36e3b4d?resizing_type=fill&width=1920&height=335)

A **Driftboard Spawner** is a device that [spawns](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) a [Driftboard](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) vehicle at the spawner's location and orientation.

- Use Driftboard Spawner devices in combination with the [Race Checkpoint Device](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) to design a racing game.
- Place a player directly on the Driftboard using [event binding](https://dev.epicgames.com/documentation/fortnite/using-driftboard-spawner-devices-in-fortnite-creative).

  To find the Driftboard Spawner device, see [Using Devices](https://dev.epicgames.com/documentation/fortnite/using-devices-in-fortnite).

If you're using multiple copies of a device on an island, it can be helpful to [rename](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) them. Choosing names that relate to a device's purpose makes it easier to remember what each one does, and easier to find a specific device when using the [Event Browser](https://dev.epicgames.com/documentation/fortnite/event-browser-in-fortnite-creative).

## Contextual Filtering

Some devices are affected by a feature called **contextual filtering**. This feature hides or displays options depending on the values selected for certain related options. This reduces clutter in the Customize panel and makes options easier to manage and navigate. To help identify them, values that trigger contextual filtering are in *italic*.

All options are listed, including those affected by contextual filtering; if they are hidden or displayed based on a specific option's value, there will be a note about it in the Description field for that option.

## Device Options

This device has some basic functionality, like whether it is visible in game, or whether it supports [wraps](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary). Additionally, there are some advanced options, like which [class](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) and team can use the vehicle, whether it plays audio, and whether [enabling](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) or disabling the device spawns or [despawns](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) the vehicle.

Default values are **bold**. Values that trigger contextual filtering are *italic*.

You can configure this device with the following options.

| Option | Value | Description |
| --- | --- | --- |
| **Enabled During Phase** | **Always**, None, Pre-Game Only, Gameplay Only | Determines the game [phases](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) during which the device will be enabled. Pre-Game includes all phases prior to the Game starting (the waiting for players lobby on Featured Islands and the Game Start Countdown). |
| **Enable Respawn** | **On**, *Off* | Determines if the vehicle will respawn after being destroyed. When you select **Off**, the **Respawn Time** option is hidden. |
| **Respawn Time** | **Instant**, Never, Pick a time | Respawns a vehicle that's been destroyed after a selected delay. This option only shows when **Enable Respawn** is set to **On**. |
| **Respawn Vehicle when Enabled** | **Yes**, No, Only If Needed | If this is set to **Yes**, a vehicle will spawn when the device is enabled. Choosing **Only If Needed** will not reset an existing vehicle. |
| **Destroy Vehicle When Disabled** | **On**, Off | Destroys a spawned vehicle when the spawner is disabled. |
| **Activating Team** | **Any**, Pick a Team | The team this device belongs to. |
| **Allowed Class** | **All**, No, Any, Pick a Class | [INCLUDE#class] |
| **Visible During Game** | **On**, Off | Determines whether the device is visible during the game. This does affect its [collision](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) properties. |
| **Supports Wraps** | **On**, Off | Determines whether the vehicle supports [wraps](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary).This option allows players to use wraps they have equipped. |
| **Vehicle Indestructible** | **Off**, *On* | Determines if the vehicle can be destroyed by damage. If set to On, the **Vehicle Health** option is hidden. |
| **Vehicle Health** | **300**, Indestructible, Pick a number | Determines how much damage the vehicle can take before it is destroyed. This option only shows if **Vehicle Indestructible** is set to **Off**. |
| **Play Audio** | **Plays Audio**, No Audio | Determines whether the spawned vehicle plays audio. |
| **Destroy When Stuck Under Water** | **On**, *Off* | Determines if the vehicle will destroy itself when it’s stuck under water. If set to Off, the **Water Destruction Timer** option is hidden. |
| **Water Destruction Timer** | Pick a time | When the vehicle becomes too deep in water to drive, destroy it after the set amount of time has passed. This option only shows If **Destroy When Stuck Under Water** is set to **On**. |

## Direct Event Binding

Following are the [direct event binding](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) options for this device.

### Functions

A [function](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) listens for an event on a device then performs an action.

| Option Description |  |
| --- | --- |
| **Enable When Receiving From** | Enables the device when an event occurs. |
| **Disable When Receiving From** | Disables the device when an event occurs. |
| **Respawn Vehicle When Receiving From** | Spawns a new vehicle when an event occurs. |
| **Destroy Vehicle When Receiving From** | Destroys the vehicle when an event occurs. |
| **Assigns Driver When Receiving From** | Assigns a driver when an event occurs. |
| **Apply Off Road Tires When Receiving From** | Does not apply to this vehicle.. |
| **Remove Tire Modification When Receiving From** | Does not apply to this vehicle.. |
| **Pop All Tires When Receiving From** | Does not apply to this vehicle.. |
| **Repair All Tires When Receiving From** | Does not apply to this vehicle.. |
| **Repair Vehicle When Receiving From** | Restores the vehicle to full health when an event occurs. |

### Events

An [event](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) tells another device when to perform a function.

| Option | Description |
| --- | --- |
| **On Player Enters Vehicle Send Event To** | Sends an event to a linked device when the player mounts the vehicle. |
| **On Player Exits Vehicle Send Event To** | Sends an event to a linked device when the player exits the vehicle. |
| **On Vehicle Spawn Send Event To** | Sends an event to a linked device when the vehicle spawns. |
| **On Vehicle is Destroyed Send Event To** | Sends an event to a linked device when the vehicle is destroyed. |
