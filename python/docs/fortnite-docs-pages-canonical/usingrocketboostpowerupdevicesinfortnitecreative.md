## https://dev.epicgames.com/documentation/en-us/fortnite/usingrocketboostpowerupdevicesinfortnitecreative

# Rocket Boost Powerup Devices

Use this to fuel up the Boost in your Octane vehicles.

![Rocket Boost Powerup Devices](https://dev.epicgames.com/community/api/documentation/image/06bbff2f-9675-401f-8c62-0c4edec66f16?resizing_type=fill&width=1920&height=335)

The **Rocket Boost powerup** provides a way to refill an [Octane](using-octane-spawner-devices-in-fortnite-creative) vehicle's **Boost Meter**. **Boost** is a unique resource that powers the Octane vehicle's ability to reach supersonic speeds and even fly.

You can control the amount of [boost](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#boost) that is refilled by the pickup, and the [cooldown](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary#cooldown) time. With customized Rocket Boost pickups, you can create games with limited boost that require more strategy, or high-speed chaotic games that have plenty of Rocket Boost powerups.

The Rocket Boost pickup appears as a flat pad when restoring a small amount of boost, and a pill when restoring a large amount!

For help on how to find the **Rocket Boost Powerup** device, see [Using Devices](https://dev.epicgames.com/documentation/fortnite/using-devices-in-fortnite).

If you're using multiple copies of a device on an island, it can be useful to rename them. Choosing names that relate to a device's purpose makes it easier to remember what each one does, and easier to find a specific device when using the [Event Browser](https://dev.epicgames.com/documentation/fortnite/event-browser-in-fortnite-creative).

## Contextual Filtering

Some devices are affected by a feature called **contextual filtering**. This feature hides or displays options depending on the values selected for certain related options. This feature will reduce clutter in the Customize panel and make options easier to manage and navigate.

However, it may not be easy to recognize which options or values trigger contextual filtering. To help you identify them, in our device docs we use *italic* for any values that trigger contextual filtering. All options will be listed, including those affected by contextual filtering; if they are hidden or displayed based on a specific option's value, there will be a note about that in the Description field for that option.

## Device Options

This device has some basic functionality, like choosing the Boost Type. Additionally, there are some advanced options, like customizing the Boost amount and which teams can activate the device.

You can configure this device with the following options.

Default values are **bold**. Values that trigger contextual filtering are *italic*.

### Basic Options

| Option | Value | Description |
| --- | --- | --- |
| **Boost Type** | Small, **Large**, *Custom* | How much rocket boost this powerup adds to the Octane's boost meter. **Small** restores **12 Boost**, with a five-second cooldown. **Large** restores **100 Boost**, with a ten-second cooldown. If you choose **Custom**, two additional options are displayed in the All Options list. |

### All Options (Additional)

| Option | Value | Description |
| --- | --- | --- |
| **Enabled During Phase** | None, **All**, Pre-Game Only, Gameplay Only | Determines the game phases during which the device will be enabled. Pre-Game Only includes all phases prior to the start of the game. |
| **Activating Team** | **Any**, Pick a team number | Determines which team can activate the device. |
| **Boost Regeneration Amount** | **100**, Pick a number | This option only displays if the **Boost Type** option is set to **Custom**. Determines the amount of boost the pickup will regenerate, as a percentage. |
| **Respawn Time** | **10**, Pick a number | This option only displays if the **Boost Type** option is set to **Custom**. Determines the cooldown (in seconds) of the pickup before it can be consumed again. |

## Direct Event Binding

Following are the [direct event binding](https://dev.epicgames.com/documentation/fortnite/direct-event-binding) options for this device.

### Functions

A [function](https://dev.epicgames.com/documentation/fortnite/function) listens for an event on a device then performs an action.

| Option | Description |
| --- | --- |
| Enable When Receiving From | This function enables the device when an event occurs. |
| Disable When Receiving From | This function disables the device when an event occurs. |
| Restock When Receiving From | This function restocks the Rocket Boost Powerup in the device when an event occurs. |

### Events

An [event](https://dev.epicgames.com/documentation/fortnite/event) tells another device when to perform a function.

| Option | Description |
| --- | --- |
| Boost Picked Up Send Event To | When a boost has been picked up, transmit. |
