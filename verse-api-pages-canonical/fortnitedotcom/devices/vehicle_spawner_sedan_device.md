## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/vehicle_spawner_sedan_device

# down_but_not_out_device class
Learn technical details about the down_but_not_out_device class.
Used to customize (or prevent) the 'down but not out' player state between 'healthy' and 'removed from game'.
|
---|---
Verse `using` statement | `using { /Fortnite.com/Devices }`
## Inheritance Hierarchy
This class is derived from the following hierarchy, starting with `creative_object`:
Name | Description
---|---
[`creative_object`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object) |  Base class for creative devices and props.
[`creative_device_base`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_device_base) |  Base class for creative_device.
## Members
This class has both data members and functions.
### Data
Data Member Name | Type | Description
---|---|---
`AgentDownedEvent` | `listenable(payload)` |  Signaled when an `agent` is set to the `down but not out` player state. Sends the `agent` that was downed.
`AgentDroppedEvent` | `listenable(payload)` |  Signaled when an `agent` in the `down but not out` player state is dropped. Sends the `agent` that was dropped.
`AgentPickedUpEvent` | `listenable(payload)` |  Signaled when an `agent` in the `down but not out` player state is picked up. Sends the `agent` that was picked up.
`AgentRevivedEvent` | `listenable(payload)` |  Signaled when an `agent` in the `down but not out` player state is revived. Sends the `agent` that was revived.
`AgentThrownEvent` | `listenable(payload)` |  Signaled when an `agent` in the `down but not out` player state is thrown. Sends the `agent` that was thrown.
`ShakeDownEvent` | `listenable(payload)` |  Signaled when an `agent` is the aggressor of a shake down. Sends the `agent` that is the aggressor.
`ShakenDownEvent` | `listenable(payload)` |  Signaled when an `agent` is the victim of a shake down. Sends the `agent` that is the victim.
### Functions
Function Name | Description
---|---
[`Disable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/down_but_not_out_device/disable) |  Disables this device.
[`Down`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/down_but_not_out_device/down) |  Sets the `Agent` to the `down but not out` player state.
[`Enable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/down_but_not_out_device/enable) |  Enables this device.
[`GetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) |  Gets the global transform of this object.
[`GetTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) |  Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result.
[`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) |  Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) |  Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) |  Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state.
[`Revive`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/down_but_not_out_device/revive) |  Sets the `Agent` to the `healthy` player state if they are in the `down but not out` player state.
[`SetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) |  Sets the global transform of this object.
[`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) |  Teleports the `creative_object` to the specified `Position` and `Rotation`.
[`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) |  Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
[`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) |  Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
