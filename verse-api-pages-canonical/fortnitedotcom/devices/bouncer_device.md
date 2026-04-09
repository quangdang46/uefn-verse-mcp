## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/bouncer_device

# automated_turret_device class
Learn technical details about the automated_turret_device class.
Used to create a customizable turret that can search for nearby targets.
|
---|---
Verse `using` statement | `using { /Fortnite.com/Devices }`
## Inheritance Hierarchy
This class is derived from the following hierarchy, starting with `creative_object`:
Name | Description
---|---
[`creative_object`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object) |  Base class for creative devices and props.
[`creative_device_base`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_device_base) |  Base class for creative_device.
## Exposed Interfaces
This class exposes the following interfaces:
Name | Description
---|---
[`healthful`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/game/healthful) |  Implemented by Fortnite objects that have health state and can be eliminated.
[`healable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/game/healable) |  Implemented by Fortnite objects that can be healed.
## Members
This class has both data members and functions.
### Data
Data Member Name | Type | Description
---|---|---
`ActivatedEvent` | `listenable(payload)` |  Triggers when someone enters the activation radius while nobody else is there. Sends the activating `agent`. If the activator is a non-agent then `false` is returned.
`DamagedEvent` | `listenable(payload)` |  Triggers when the turret is damaged. Sends the triggering `agent`. If the activator is a non-agent then `false` is returned.
`DestroyedEvent` | `listenable(payload)` |  Triggers when the turret is destroyed. Sends the triggering `agent`. If the activator is a non-agent then `false` is returned.
`TargetFoundEvent` | `listenable(payload)` |  Triggers when the turret finds a target. Sends the `agent` that was found.
`TargetLostEvent` | `listenable(payload)` |  Triggers when the turret loses a target. Sends the `agent` that was lost.
### Functions
Function Name | Description
---|---
[`ClearTarget`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/automated_turret_device/cleartarget) |  Clears the turret's current target and returns the turret to searching for targets.
  * If the current target is still in range, it'll likely be the best target, and will be reacquired.
  * Combine with disabled targeting for best results.

[`Disable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/automated_turret_device/disable) |  Disables the turret, causing it to close and ignore its activation radius.
[`Enable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/automated_turret_device/enable) |  Enables the turret to rotate, target, and track.
[`GetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) |  Gets the global transform of this object.
[`GetHealth`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/automated_turret_device/gethealth) |
[`GetMaxHealth`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/automated_turret_device/getmaxhealth) |
[`GetTarget`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/automated_turret_device/gettarget) |  Returns the `agent` currently targeted by the device.
[`GetTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) |  Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result.
[`Heal`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/automated_turret_device/heal) |
[`Heal`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/automated_turret_device/heal-1) |
[`HealedEvent`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/automated_turret_device/healedevent) |
[`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) |  Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) |  Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) |  Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state.
[`SetActivationRange`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/automated_turret_device/setactivationrange) |  Sets the range in meters at which the turret will activate to `Range`. This is clamped between `2.0` and `100.0` meters.
[`SetDamage`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/automated_turret_device/setdamage) |  Sets the amount of damage the turret will do per shot to targets to `Damage`.
[`SetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) |  Sets the global transform of this object.
[`SetHealth`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/automated_turret_device/sethealth) |
[`SetMaxHealth`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/automated_turret_device/setmaxhealth) |
[`SetTarget`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/automated_turret_device/settarget) |  Set the supplied `Agent` as the turret's target.
  * The target will only change if `Agent` is within the activation radius, has direct line-of-sight to the turret, is on a targetable team as determined by `Possible Targets`, and is not Down But Not Out.

[`SetTargetRange`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/automated_turret_device/settargetrange) |  Sets the range in meters at which the turret will target to `Range`. This is clamped between `2.0` and `100.0` meters. Setting it lower than 2m will disable Targeting.
[`SetTeam`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/automated_turret_device/setteam) |  Set the turret to the same team as the supplied `Agent`.
  * Only usable if `Possible Targets` is not set to `Everyone`.

[`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) |  Teleports the `creative_object` to the specified `Position` and `Rotation`.
[`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) |  Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
[`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) |  Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
[`UseDefaultTeam`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/automated_turret_device/usedefaultteam) |  Set the turret to the Default Team.
  * Only usable if `Possible Targets` is not set to `Everyone`.

[`UseTeamWildlifeAndCreatures`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/automated_turret_device/useteamwildlifeandcreatures) |  Set the turret to the Wildlife & Creatures team.
  * Only usable if `Possible Targets` is not set to `Everyone`.
