## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/firefly_spawner_device

# player_marker_device class
Learn technical details about the player_marker_device class.
Used to mark an `agent`'s position on the minimap and configure the information shown for marked `agent`s.
Example configuration options:
  * Health and shield bars for marked players.
  * Distance to a marked player.

Example marker appearance options:
  * Customized text label displayed on marked players.
  * Alternative minimap icon and icon color.

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
`FirstItemValueChangedEvent` | `listenable(payload)` |  Signaled when the first item type monitored on marked agents has changed. Sends the marked `agent`.
`FirstItemValueReachedEvent` | `listenable(payload)` |  Signaled when a marked `agent` meets the quantity condition for the first monitored item type (e.g. Fewer Than, Equal To, More Than X). Sends the marked `agent`.
`SecondItemValueChangedEvent` | `listenable(payload)` |  Signaled when the second item type monitored on marked agents has changed. Sends the marked `agent`.
`SecondItemValueReachedEvent` | `listenable(payload)` |  Signaled when a marked `agent` meets the quantity condition for the second monitored item type (e.g. Fewer Than, Equal To, More Than X). Sends the marked `agent`.
### Functions
Function Name | Description
---|---
[`Attach`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/player_marker_device/attach) |  Attaches a marker to `Agent`.
[`Detach`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/player_marker_device/detach) |  Detaches a marker from `Agent`.
[`DetachFromAll`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/player_marker_device/detachfromall) |  Detaches markers from all marked `agent`s.
[`Disable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/player_marker_device/disable) |  Disables this device.
[`Enable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/player_marker_device/enable) |  Enables this device.
[`GetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) |  Gets the global transform of this object.
[`GetTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) |  Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result.
[`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) |  Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) |  Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) |  Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state.
[`SetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) |  Sets the global transform of this object.
[`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) |  Teleports the `creative_object` to the specified `Position` and `Rotation`.
[`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) |  Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
[`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) |  Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
