## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/objective_device

# objective_device class
Learn technical details about the objective_device class.
Provides a collection of destructible devices that you can select from to use as objectives in your game.
|
---|---
Verse `using` statement | `using { /Fortnite.com/Devices }`
## Inheritance Hierarchy
This class is derived from the following hierarchy, starting with `creative_object`:
Name | Description
---|---
[`creative_object`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object) |  Base class for creative devices and props.
[`creative_device_base`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_device_base) |  Base class for creative_device.
## Exposed Interfaces
This class exposes the following interfaces:
Name | Description
---|---
[`healthful`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/game/healthful) |  Implemented by Fortnite objects that have health state and can be eliminated.
[`damageable`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/game/damageable) |  Implemented by Fortnite objects that can be damaged.
[`healable`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/game/healable) |  Implemented by Fortnite objects that can be healed.
## Members
This class has both data members and functions.
### Data
Data Member Name | Type | Description
---|---|---
`DestroyedEvent` | `listenable(payload)` |  Signaled when this device has been destroyed by an `agent`. Sends the `agent` that destroyed this device.
### Functions
Function Name | Description
---|---
[`ActivateObjectivePulse`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/objective_device/activateobjectivepulse) |  Activates an objective pulse at `Agent`'s location pointing toward this device.
[`Damage`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/objective_device/damage) |
[`Damage`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/objective_device/damage-1) |
[`DamagedEvent`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/objective_device/damagedevent) |
[`DeactivateObjectivePulse`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/objective_device/deactivateobjectivepulse) |  Deactivates the objective pulse at `Agent`'s location.
[`Destroy`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/objective_device/destroy) |  Destroys the objective item. This is done regardless of the visibility or health of the item.
[`GetGlobalTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) |  Gets the global transform of this object.
[`GetHealth`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/objective_device/gethealth) |
[`GetMaxHealth`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/objective_device/getmaxhealth) |
[`GetTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) |  Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result.
[`Heal`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/objective_device/heal) |
[`Heal`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/objective_device/heal-1) |
[`HealedEvent`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/objective_device/healedevent) |
[`Hide`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/objective_device/hide) |  Hides this device from the world.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) |  Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) |  Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) |  Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state.
[`SetGlobalTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) |  Sets the global transform of this object.
[`SetHealth`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/objective_device/sethealth) |
[`SetInvulnerable`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/objective_device/setinvulnerable) |  Sets the device either invulnerable or damageable
[`SetMaxHealth`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/objective_device/setmaxhealth) |
[`Show`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/objective_device/show) |  Shows this device in the world.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) |  Teleports the `creative_object` to the specified `Position` and `Rotation`.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) |  Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) |  Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
