## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/teleporter_device

# teleporter_device class

Learn technical details about the teleporter_device class.

Customizable rift that allows `agent`s to move instantly between locations. You can use this to move players around your island, or create multi-island experiences with teleporters that take players from one island to another.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Fortnite.com/Devices }` |

## Inheritance Hierarchy

This class is derived from the following hierarchy, starting with `creative_object`:

| Name | Description |
| --- | --- |
| [`creative_object`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object) | Base class for creative devices and props. |
| [`creative_device_base`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_device_base) | Base class for creative_device. |

## Members

This class has both data members and functions.

### Data

| Data Member Name | Type | Description |
| --- | --- | --- |
| `EnterEvent` | `listenable(payload)` | Signaled when an `agent` enters this device. Sends the `agent` that entered this device. |
| `TeleportedEvent` | `listenable(payload)` | Signaled when an `agent` emerges from this device. Sends the `agent` that emerged from this device. |

### Functions

| Function Name | Description |
| --- | --- |
| [`Activate`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/teleporter_device/activate) | Teleport `Agent` to the target group using this device. |
| [`ActivateLinkToTarget`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/teleporter_device/activatelinktotarget) | When a link is activated, the current destination teleporter will be able to bring the `agent` back to this origin teleporter. Both origin and destination teleporters need to have this activated to work as expected. |
| [`DeactivateLinkToTarget`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/teleporter_device/deactivatelinktotarget) | Deactivates any currently active Link. The current destination teleporter will no longer be able to return the agent to this origin teleporter. |
| [`Disable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/teleporter_device/disable) | Disables this device. |
| [`Enable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/teleporter_device/enable) | Enables this device. |
| [`GetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) | Gets the global transform of this object. |
| [`GetTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) | Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) | Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) | Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) | Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state. |
| [`ResetLinkToTarget`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/teleporter_device/resetlinktotarget) | Resets the currently selected destination teleporter, and selects an eligible destination. If the target is a *Teleporter Group*, this may be another randomly chosen `teleporter_device` from that group. |
| [`SetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) | Sets the global transform of this object. |
| [`Teleport`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/teleporter_device/teleport) | Teleport `Agent` to this device. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) | Teleports the `creative_object` to the specified `Position` and `Rotation`. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) | Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) | Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly. |
