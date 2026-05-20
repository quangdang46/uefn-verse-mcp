## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/physics_boulder_device

# physics_boulder_device class

Learn technical details about the physics_boulder_device class.

Physics boulder that can be dislodged and damage `agent`s, vehicles, creatures, and structures.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Fortnite.com/Devices }` |

## Inheritance Hierarchy

This class is derived from the following hierarchy, starting with `creative_object`:

| Name | Description |
| --- | --- |
| [`creative_object`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object) | Base class for creative devices and props. |
| [`creative_device_base`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_device_base) | Base class for creative_device. |
| [`prop_spawner_base_device`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/prop_spawner_base_device) | Base class for devices that spawn a prop object. |
| [`physics_object_base_device`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/physics_object_base_device) | Base class for various physics-based gameplay elements (e.g. boulders/trees). |

## Members

This class has both data members and functions.

### Data

| Data Member Name | Type | Description |
| --- | --- | --- |
| `BalancedBoulderDestroyedEvent` | `listenable(payload)` | Signaled when the balanced boulder is destroyed. |
| `BalancedBoulderSpawnedEvent` | `listenable(payload)` | Signaled when the balanced boulder is spawned on the base. |
| `BaseDestroyedEvent` | `listenable(payload)` | Signaled when the base of the boulder is destroyed. |
| `RollingBoulderDestroyedEvent` | `listenable(payload)` | Signaled when the rolling boulder is destroyed. |

### Functions

| Function Name | Description |
| --- | --- |
| [`DestroyAllSpawnedObjects`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/prop_spawner_base_device/destroyallspawnedobjects) | Destroys all props spawned from this device. |
| [`DestroyBase`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/physics_boulder_device/destroybase) | Destroys the boulder's base. |
| [`DestroyRollingBoulder`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/physics_boulder_device/destroyrollingboulder) | Destroys the current rolling boulder. |
| [`Disable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/prop_spawner_base_device/disable) | Disables this device. |
| [`Enable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/prop_spawner_base_device/enable) | Enables this device. |
| [`GetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) | Gets the global transform of this object. |
| [`GetTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) | Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) | Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) | Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) | Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state. |
| [`ReleaseRollingBoulder`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/physics_boulder_device/releaserollingboulder) | Releases the boulder sitting on the base, if there is one. |
| [`SetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) | Sets the global transform of this object. |
| [`SpawnObject`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/prop_spawner_base_device/spawnobject) | Spawns the prop associated with this device. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) | Teleports the `creative_object` to the specified `Position` and `Rotation`. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) | Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) | Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly. |
