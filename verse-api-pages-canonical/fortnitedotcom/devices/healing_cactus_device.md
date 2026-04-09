## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/healing_cactus_device

# healing_cactus_device class
Learn technical details about the healing_cactus_device class.
Use to create a cactus with healing fruits that can be burst to heal nearby players.
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
`BurstEvent` | `listenable(payload)` |  Triggers when the plant bursts, passing in the triggering `agent`.
`GrowEvent` | `listenable(payload)` |  Triggers when the plant grows.
### Functions
Function Name | Description
---|---
[`Burst`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/healing_cactus_device/burst) |  Burst the plant if the device is enabled, passing in the triggering `agent`. If there is no triggering `agent`, players will only be healed if `Heal Targets` is set to `Everyone`.
[`Burst`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/healing_cactus_device/burst-1) |  Burst the plant if the device is enabled, passing in the triggering `agent`. If there is no triggering `agent`, players will only be healed if `Heal Targets` is set to `Everyone`.
[`Disable`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/healing_cactus_device/disable) |  Disables the device to prevent interaction and growth.
[`Enable`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/healing_cactus_device/enable) |  Enables the device to allow interaction and let it grow.
[`GetGlobalTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) |  Gets the global transform of this object.
[`GetTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) |  Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result.
[`Grow`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/healing_cactus_device/grow) |  Grows the plant if the device is enabled. If `Infinite Regrowths` is `false`, this is limited by `Maximum Regrowths`. If someone is too close, the plant won't grow until they move away.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) |  Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) |  Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) |  Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state.
[`SetGlobalTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) |  Sets the global transform of this object.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) |  Teleports the `creative_object` to the specified `Position` and `Rotation`.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) |  Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) |  Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
