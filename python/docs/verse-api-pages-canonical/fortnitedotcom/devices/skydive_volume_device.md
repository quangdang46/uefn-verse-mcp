## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/skydive_volume_device

# skydive_volume_device class

Learn technical details about the skydive_volume_device class.

Used to create a zone where players are put into a skydive state. Can customize the amount of force used to push the player, and how fast players are launched into the air. The direction of the push is in relation to the device, so you can rotate and overlap several devices, then use variable speeds to create pneumatic tubes that propel players in different directions. You can even create unique traversal (traveling) options, where players can use these zones to reach places on your island they couldn't reach any other way.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Fortnite.com/Devices }` |

## Inheritance Hierarchy

This class is derived from the following hierarchy, starting with `creative_object`:

| Name | Description |
| --- | --- |
| [`creative_object`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object) | Base class for creative devices and props. |
| [`creative_device_base`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_device_base) | Base class for creative_device. |
| [`effect_volume_device`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/effect_volume_device) | Base class for types of volumes with special gameplay properties. |

## Members

This class has both data members and functions.

### Data

| Data Member Name | Type | Description |
| --- | --- | --- |
| `AgentEntersEvent` | `listenable(payload)` | Signaled when an `agent` enters the volume. Sends the `agent` that entered the volume. |
| `AgentExitsEvent` | `listenable(payload)` | Signaled when an `agent` exits the volume. Sends the `agent` that exited the volume. |
| `ZoneEmptiedEvent` | `listenable(payload)` | Signaled when the zone changes from occupied to empty. Sends the `agent` that last left the volume. |
| `ZoneOccupiedEvent` | `listenable(payload)` | Signaled when the zone changes from empty to occupied. Sends the `agent` that entered the volume. |

### Functions

| Function Name | Description |
| --- | --- |
| [`Disable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/effect_volume_device/disable) | Disables this device. |
| [`DisableVolumeLocking`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/skydive_volume_device/disablevolumelocking) | Disables volume locking which prevents users from leaving the volume once they've entered. |
| [`Enable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/effect_volume_device/enable) | Enables this device. |
| [`EnableVolumeLocking`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/skydive_volume_device/enablevolumelocking) | Enables volume locking which prevents users from leaving the volume once they've entered. |
| [`GetAgentsInVolume`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/skydive_volume_device/getagentsinvolume) | Returns an array of agents that are currently occupying the volume. |
| [`GetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) | Gets the global transform of this object. |
| [`GetTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) | Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| [`IsInVolume`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/skydive_volume_device/isinvolume) | Is true when `Agent` is in the volume. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) | Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) | Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) | Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state. |
| [`SetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) | Sets the global transform of this object. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) | Teleports the `creative_object` to the specified `Position` and `Rotation`. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) | Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) | Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly. |
