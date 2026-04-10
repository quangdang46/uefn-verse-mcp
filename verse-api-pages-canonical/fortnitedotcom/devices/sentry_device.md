## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/sentry_device

# sentry_device class
Learn technical details about the sentry_device class.
Generates an AI bot that spawns in a location and usually attacks players when they come in range.
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
`AlertedEvent` | `listenable(payload)` |  Signaled when the sentry is alerted to an `agent`. Sends the `agent` who alerted the sentry.
`AttackingEvent` | `listenable(payload)` |  Signaled when a sentry attacks an `agent`. Sends the `agent` who is being attacked.
`EliminatedEvent` | `listenable(payload)` |  Signaled when a sentry is eliminated. Sends the `agent` that eliminated the sentry. If the sentry was eliminated by a non-agent then `false` is returned.
`EliminatingACreatureEvent` | `listenable(payload)` |  Signaled when the sentry eliminates a creature.
`EliminatingAgentEvent` | `listenable(payload)` |  Signaled when a sentry eliminates an `agent`. Sends the `agent` who was eliminated by the sentry.
`EntersAlertCooldownEvent` | `listenable(payload)` |  Signaled when the sentry enters the alert state.
`ExitsAlertEvent` | `listenable(payload)` |  Signaled when the sentry exists the alert state.
### Functions
Function Name | Description
---|---
[`DestroySentry`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/sentry_device/destroysentry) |  Destroys the current sentry.
[`Disable`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/sentry_device/disable) |  Disables this device.
[`Enable`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/sentry_device/enable) |  Enables this device.
[`EnableAlert`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/sentry_device/enablealert) |  Puts the sentry into the alert state.
[`GetGlobalTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) |  Gets the global transform of this object.
[`GetTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) |  Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result.
[`JoinTeam`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/sentry_device/jointeam) |  Sets the sentry to the same team `Agent` is on.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) |  Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) |  Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) |  Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state.
[`Pacify`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/sentry_device/pacify) |  Puts the sentry into the pacify state, preventing from entering the alert (attacking) state.
[`ResetAlertCooldown`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/sentry_device/resetalertcooldown) |  Resets the alert state.
[`ResetTeam`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/sentry_device/resetteam) |  Resets the sentry to the original team designated in the device options.
[`SetGlobalTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) |  Sets the global transform of this object.
[`Spawn`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/sentry_device/spawn) |  Spawns the sentry.
[`Target`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/sentry_device/target) |  Sets the sentry to target `Agent`. The sentry will not target agents on the same team as the sentry.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) |  Teleports the `creative_object` to the specified `Position` and `Rotation`.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) |  Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) |  Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
