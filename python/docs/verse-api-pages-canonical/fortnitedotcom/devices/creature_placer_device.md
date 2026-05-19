## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creature_placer_device

# creature_placer_device class
Learn technical details about the creature_placer_device class.
Used to spawn a creature at a specified location.
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
`EliminatedEvent` | `listenable(payload)` |  Signaled when the creature is eliminated.
  * Sends the `agent` that eliminated the creature.
  * Sends `false` if the creature was eliminated by something other than an `agent` (e.g. a vehicle).

`SpawnedEvent` | `listenable(payload)` |  Signaled when a creature is spawned. Sends the `agent` creature who was spawned.
### Functions
Function Name | Description
---|---
[`Despawn`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creature_placer_device/despawn) |  Despawns the creature.
[`GetGlobalTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) |  Gets the global transform of this object.
[`GetTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) |  Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) |  Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) |  Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) |  Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state.
[`SetGlobalTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) |  Sets the global transform of this object.
[`Spawn`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creature_placer_device/spawn) |  Spawns the creature.
[`SpawnAt`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creature_placer_device/spawnat) |  Spawn a creature at the given position. When Rotation is not provided, it will default to the Device’s rotation. Returns the agent spawned or false if the device has reached its maximum spawn count. This function is ‘’ because it takes time to load the creature before it can be returned.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) |  Teleports the `creative_object` to the specified `Position` and `Rotation`.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) |  Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) |  Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
