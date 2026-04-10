## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/damage_volume_device

# damage_volume_device class
Learn technical details about the damage_volume_device class.
Used to specify an area volume which can damage `agent`s, vehicles, and creatures.
|
---|---
Verse `using` statement | `using { /Fortnite.com/Devices }`
## Inheritance Hierarchy
This class is derived from the following hierarchy, starting with `creative_object`:
Name | Description
---|---
[`creative_object`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object) |  Base class for creative devices and props.
[`creative_device_base`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_device_base) |  Base class for creative_device.
[`effect_volume_device`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/effect_volume_device) |  Base class for types of volumes with special gameplay properties.
## Members
This class has both data members and functions.
### Data
Data Member Name | Type | Description
---|---|---
`AgentEntersEvent` | `listenable(payload)` |  Signaled when an `agent` enters the volume. Sends the `agent` entering the volume.
`AgentExitsEvent` | `listenable(payload)` |  Signaled when an `agent` exits the volume. Sends the `agent` exiting the volume.
`PropEnterEvent` | `listenable(payload)` |  Signaled when a `creative_prop` enters the device volume.
`PropExitEvent` | `listenable(payload)` |  Signaled when a `creative_prop` exits the device volume.
### Functions
Function Name | Description
---|---
[`Disable`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/effect_volume_device/disable) |  Disables this device.
[`Enable`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/effect_volume_device/enable) |  Enables this device.
[`GetAgentsInVolume`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/damage_volume_device/getagentsinvolume) |  Returns an array of agents that are currently occupying the volume.
[`GetDamage`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/damage_volume_device/getdamage) |  Returns the damage to be applied each tick within the volume.
[`GetGlobalTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) |  Gets the global transform of this object.
[`GetTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) |  Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result.
[`IsInVolume`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/damage_volume_device/isinvolume) |  Is true when `Agent` is in the zone.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) |  Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) |  Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) |  Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state.
[`SetDamage`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/damage_volume_device/setdamage) |  Sets the damage to be applied each tick within the volume. `Damage` is clamped between `1` and `500`.
[`SetGlobalTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) |  Sets the global transform of this object.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) |  Teleports the `creative_object` to the specified `Position` and `Rotation`.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) |  Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) |  Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
[`UpdateSelectedClass`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/damage_volume_device/updateselectedclass) |  Updates _Selected Class_ to `Agent`'s class.
[`UpdateSelectedTeam`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/damage_volume_device/updateselectedteam) |  Updates _Selected Team_ to `Agent`'s team.
