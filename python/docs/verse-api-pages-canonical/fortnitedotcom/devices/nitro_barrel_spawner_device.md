## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/nitro_barrel_spawner_device

# nitro_barrel_spawner_device class
Learn technical details about the nitro_barrel_spawner_device class.
Used to create an environmental prop that applies Nitro to those around it when it is destroyed.
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
`ExplodedEvent` | `listenable(payload)` |  Triggers when the barrel explodes after being launched. Sends the launching `agent`.If the launcher is a non-agent, sends `false`.
`LaunchedEvent` | `listenable(payload)` |  Triggers when an `agent` launches the barrel. Sends the launching `agent`.If the launcher is a non-agent, sends `false`.
### Functions
Function Name | Description
---|---
[`AllowRespawn`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/nitro_barrel_spawner_device/allowrespawn) |  Allows the barrel to respawn after it explodes, waiting _RespawnDelay_ seconds.
[`Disable`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/nitro_barrel_spawner_device/disable) |  Disables and hides the barrel.Disabling the device will remove an existing barrel and reset the respawn delay.
[`DisallowRespawn`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/nitro_barrel_spawner_device/disallowrespawn) |  Prevents the barrel from respawning.The _RespawnDelay_ countdown will not start. If the countdown has already started, the barrel will not respawn when it ends.
[`Enable`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/nitro_barrel_spawner_device/enable) |  Enables and shows the barrel.Enabling the device when it's disabled will spawn a new barrel.
[`GetGlobalTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) |  Gets the global transform of this object.
[`GetLaunchForceMultiplier`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/nitro_barrel_spawner_device/getlaunchforcemultiplier) |  Returns the force multiplier to launch the barrel.
[`GetRespawnDelay`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/nitro_barrel_spawner_device/getrespawndelay) |  Returns the delay between exploding and respawning (if allowed), in seconds.
[`GetTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) |  Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result.
[`IsEnabled`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/nitro_barrel_spawner_device/isenabled) |  Succeeds if the barrel is enabled and visible.
[`IsRespawnAllowed`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/nitro_barrel_spawner_device/isrespawnallowed) |  Succeeds if the barrel has respawn allowed.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) |  Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) |  Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) |  Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state.
[`SetGlobalTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) |  Sets the global transform of this object.
[`SetLaunchForceMultiplier`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/nitro_barrel_spawner_device/setlaunchforcemultiplier) |  Sets the multiplier applied to the force used when launching.This is clamped between `0.25` and `2.0`.
[`SetRespawnDelay`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/nitro_barrel_spawner_device/setrespawndelay) |  Sets the delay time to respawn the barrel, clamped between `0.0` and `1000.0` seconds.This will override the delay timer if set during the delay countdown.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) |  Teleports the `creative_object` to the specified `Position` and `Rotation`.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) |  Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) |  Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
