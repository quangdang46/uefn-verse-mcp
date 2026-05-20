## https://dev.epicgames.com/documentation/en-us/fortnite/using-creator-profile-link-devices-in-fortnite-creative

# Developer Profile Devices

Use this device to display a QR code that links to your profile in Creator Portal.

![Developer Profile Devices](https://dev.epicgames.com/community/api/documentation/image/098104a2-b6b3-403f-928a-7c35e7a3fafe?resizing_type=fill&width=1920&height=335)

The **Developer Profile** device displays a QR code that links to your profile page in the Creator Portal. This provides an easy way for players to get to your profile and find more of your islands!

For help on how to find the **Developer Profile** device, see [Using Devices](https://dev.epicgames.com/documentation/fortnite/using-devices-in-fortnite).

## Device Options

Default values are **bold**.

You can configure this device with the following options.

| Option | Value | Description |
| --- | --- | --- |
| **Enabled During Phase** | None, **Always**, Pre-Game Only, Gameplay Only, Create Only | Determines in which phases the device is enabled. |
| **Face Camera** | On, **Off** | When this is set to **On**, the QR code will always be facing the player's camera. |
| **Two-Sided** | **On**, Off | Determines if the QR code is displayed on both sides of the display area. |

## Direct Event Binding

Following are the [direct event binding](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) options for this device.

### Functions

A [function](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) listens for an event on a device then performs an action.

| Option | Description |
| --- | --- |
| **Enable When Receiving From** | Enables the device when an event occurs. |
| **Disable When Receiving From** | Disables the device when an event occurs. |

### Events

An [event](https://dev.epicgames.com/documentation/fortnite/fortnite-glossary) tells another device when to perform a function.

| Option | Description |
| --- | --- |
| **Enabled Sent Event To** | When the device is enabled, an event is sent to the selected device, which triggers the selected function. |
| **Disabled Send Event To** | When the device is disabled, an event is sent to the selected device, which triggers the selected function. |
