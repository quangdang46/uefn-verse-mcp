## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creature_manager_device

# creature_manager_device class
Learn technical details about the creature_manager_device class.
Used to customize one creature type at a time. Place multiple `creature_manager_device`s for each type of creature on your island. Changing properties will respect the `Affected Creatures` property of the device. If `Affected Creatures` is set to `New Pawns Only`, only new spawns will get the changed property values. If set to `New and Existing Pawns`, all creatures spawned from this device and new ones will have the new properties.
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
`AllowWeaponKnockback` | `?logic` |  Determines if the selected Creature type can be knocked back by weapon impacts.
`DamageToEnvironment` | `??float` |  If a value is given, the `DamageToEnvironment` value of the creature is overridden. If an override is not specified, the default `DamageToEnvironment` of the creature is used. This value is clamped between 0 and 500.
`DamageToPlayer` | `??float` |  If a value is given, the `DamageToPlayer` value of the creature is overridden. If an override is not specified, the default `DamageToPlayer` of the creature is used. This value is clamped between 0 and 500.
`MatchingCreatureTypeEliminatedEvent` | `listenable(payload)` |  Signaled when a creature of the selected _Creature Type_ is eliminated. Sends the `agent` that eliminated the creature.
`MaxHealth` | `??int` |  If set, the health value of the creature is overridden. If an override is not specified, the default Health of the creature is used. This value is clamped between 1 and 10000.
`MovementSpeed` | `??float` |  If a value is given, the `SpeedMultiplier` value is applied to the default speed of the creature. If an override is not specified, the creature moves at its default speed. This value is clamped between 0.0 and 2.0.
`Score` | `??int` |  If a value is given, the `Score` value of the creature is overridden. If an override is not specified, the default `Score` of the creature is used. This value is clamped between 0 and 100.
### Functions
Function Name | Description
---|---
[`Disable`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creature_manager_device/disable) |  Disables this device.
[`Enable`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creature_manager_device/enable) |  Enables this device.
[`GetGlobalTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) |  Gets the global transform of this object.
[`GetTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) |  Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) |  Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) |  Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) |  Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state.
[`SetGlobalTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) |  Sets the global transform of this object.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) |  Teleports the `creative_object` to the specified `Position` and `Rotation`.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) |  Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) |  Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
