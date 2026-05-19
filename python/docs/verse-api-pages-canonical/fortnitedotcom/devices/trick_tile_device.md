## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/trick_tile_device

# trick_tile_device class
Learn technical details about the trick_tile_device class.
A trap device that destroys the tile it's placed on when activated.
|
---|---
Verse `using` statement | `using { /Fortnite.com/Devices }`
## Inheritance Hierarchy
This class is derived from the following hierarchy, starting with `creative_object`:
Name | Description
---|---
[`creative_object`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object) |  Base class for creative devices and props.
[`creative_device_base`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_device_base) |  Base class for creative_device.
## Members
This class has both data members and functions.
### Data
Data Member Name | Type | Description
---|---|---
`ActivatedEvent` | `listenable(payload)` |  Signaled when the tile this device is attached to is removed. This may occur later than `TriggeredEvent` if _Activation Delay_ is set on the device. Sends the `agent` that activated this device.
`TriggeredEvent` | `listenable(payload)` |  Signaled when this device is triggered. Sends the `agent` that triggered this device.
### Functions
Function Name | Description
---|---
[`Disable`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/trick_tile_device/disable) |  Disables this device. While disabled this device will not react to incoming events.
[`DisableAgentContactTrigger`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/trick_tile_device/disableagentcontacttrigger) |  Disables this device from triggering when an `agent` makes contact with the device.
[`Enable`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/trick_tile_device/enable) |  Enables this device.
[`EnableAgentContactTrigger`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/trick_tile_device/enableagentcontacttrigger) |  Enables this device to trigger when an `agent` makes contact with the device.
[`GetGlobalTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) |  Gets the global transform of this object.
[`GetTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) |  Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/trick_tile_device/moveto) |  Moves the `trick_tile_device` to the specified `Position` and `Rotation` over the specified time, in seconds. Only the trigger will move, the target buildings will not change.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/trick_tile_device/moveto-1) |  Moves the `trick_tile_device` to the specified `Transform` over the specified time, in seconds. Only the trigger will move, the target buildings will not change.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) |  Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) |  Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) |  Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state.
[`Reset`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/trick_tile_device/reset) |  Restores the tile removed when this device was triggered.
[`SetGlobalTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) |  Sets the global transform of this object.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/trick_tile_device/teleportto) |  Teleports the `trick_tile_device` to the specified `Position` and `Rotation`. Only the trigger will teleport, the target buildings will not change.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/trick_tile_device/teleportto-1) |  Teleports the `trick_tile_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly. Only the trigger will teleport, the target buildings will not change.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) |  Teleports the `creative_object` to the specified `Position` and `Rotation`.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) |  Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) |  Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
[`ToggleAgentContactTrigger`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/trick_tile_device/toggleagentcontacttrigger) |  Flips the device between `EnableAgentContactTrigger` and `DisableAgentContactTrigger.
[`ToggleEnabled`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/trick_tile_device/toggleenabled) |  Flips the device between `Enabled` and `Disable`.
[`Trigger`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/trick_tile_device/trigger) |  Triggers the device, removing the associated tile.
