## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/radio_device

# radio_device class
Learn technical details about the radio_device class.
Used to play curated music from the device or one or more registered `agent`s.
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
[`GetGlobalTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) |  Gets the global transform of this object.
[`GetTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) |  Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result.
[`Hide`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/radio_device/hide) |  Hides this device from the world.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) |  Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) |  Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) |  Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state.
[`Play`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/radio_device/play) |  Starts playing audio from this device.
[`Register`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/radio_device/register) |  Adds the specified agent as a target for the Radio to play audio from
[`SetGlobalTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) |  Sets the global transform of this object.
[`Show`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/radio_device/show) |  Shows this device in the world.
[`Stop`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/radio_device/stop) |  Stops playing audio from this device.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) |  Teleports the `creative_object` to the specified `Position` and `Rotation`.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) |  Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) |  Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
[`Unregister`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/radio_device/unregister) |  Removes the specified agent as a target for the Radio to play audio from if previously Registered
[`UnregisterAll`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/radio_device/unregisterall) |  Removes all previously registered agents as targets for the Radio to play audio from
