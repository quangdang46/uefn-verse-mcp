## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/audio_player_device

# audio_player_device class
Learn technical details about the audio_player_device class.
Used to configure and play audio from the device location or from registered `agent`s.
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
[`Disable`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/audio_player_device/disable) |  Disables this device. No longer allows this device to be triggered from other linked devices (i.e. triggers) and will stop any currently playing audio.
[`Enable`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/audio_player_device/enable) |  Enables this device. Allows this device to be triggered from other linked devices (i.e. triggers) and allow calls to `Play` to succeed.
[`GetGlobalTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) |  Gets the global transform of this object.
[`GetTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) |  Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result.
[`Hide`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/audio_player_device/hide) |  Hides this device from the world.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) |  Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) |  Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) |  Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state.
[`Play`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/audio_player_device/play) |  Starts playing audio from this device for `Agent`. This can only be used when the device is set to be _Heard by Instigator_.
[`Play`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/audio_player_device/play-1) |  Starts playing audio from this device.
[`Register`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/audio_player_device/register) |  Adds `Agent` as a target to play audio from when activated.
[`SetGlobalTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) |  Sets the global transform of this object.
[`Show`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/audio_player_device/show) |  Shows this device in the world.
[`Stop`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/audio_player_device/stop) |  Stops any audio playing from this device for `Agent`. This can only be used when the device is set to be _Heard by Instigator_.
[`Stop`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/audio_player_device/stop-1) |  Stops any audio playing from this device.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) |  Teleports the `creative_object` to the specified `Position` and `Rotation`.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) |  Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) |  Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
[`Unregister`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/audio_player_device/unregister) |  Removes `Agent` as a target to play audio from when activated.
[`UnregisterAll`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/audio_player_device/unregisterall) |  Removes all previously registered `agent`s as valid targets to play audio from when activated.
