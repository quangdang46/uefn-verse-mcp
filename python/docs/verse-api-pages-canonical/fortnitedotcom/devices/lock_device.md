## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/lock_device

# lock_device class
Learn technical details about the lock_device class.
Used to customize the state and accessibility of doors. `lock_device` only works with assets that have a door attached.
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
This class has functions, but no data members.
### Functions
Function Name | Description
---|---
[`Close`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/lock_device/close) |  Closes the door. `Agent` is the instigator of the action.
[`GetGlobalTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) |  Gets the global transform of this object.
[`GetTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) |  Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result.
[`Lock`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/lock_device/lock) |  Locks the door. `Agent` is the instigator of the action.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) |  Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) |  Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) |  Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state.
[`Open`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/lock_device/open) |  Opens the door. `Agent` is the instigator of the action.
[`SetGlobalTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) |  Sets the global transform of this object.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) |  Teleports the `creative_object` to the specified `Position` and `Rotation`.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) |  Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) |  Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
[`ToggleLocked`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/lock_device/togglelocked) |  Toggles between `Lock` and `Unlock`. `Agent` is the instigator of the action.
[`ToggleOpened`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/lock_device/toggleopened) |  Toggles between `Open` and `Close`. `Agent` is the instigator of the action.
[`Unlock`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/lock_device/unlock) |  Unlocks the door. `Agent` is the instigator of the action.
