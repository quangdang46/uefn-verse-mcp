## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_prop

# creative_prop class

Learn technical details about the creative_prop class.

A Fortnite prop that has been placed or spawned in the island.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Fortnite.com/Devices }` |

## Inheritance Hierarchy

This class is derived from `creative_object`.

| Name | Description |
| --- | --- |
| [`creative_object`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object) | Base class for creative devices and props. |

## Exposed Interfaces

This class exposes the following interfaces:

| Name | Description |
| --- | --- |
| [`invalidatable`](https://dev.epicgames.com/documentation/fortnite/verse-api/versedotorg/verse/invalidatable) | Implemented by classes whose instances can become invalid at runtime. |

## Members

This class has both data members and functions.

### Data

| Data Member Name | Type | Description |
| --- | --- | --- |
| `CanBeDamaged` | `?logic` | Enable/disable whether this prop can be damaged. If disabled, the creative prop will not take damage from attacks. |

### Functions

| Function Name | Description |
| --- | --- |
| [`ApplyAngularImpulse`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_prop/applyangularimpulse) | Apply an angular impulse to a ‘creative_prop’ with units in Newton*meter*seconds. Will not do anything if physics is disabled. |
| [`ApplyForce`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_prop/applyforce) | Apply a force to a ‘creative_prop’ with units in Newtons. Will not do anything if physics is disabled. |
| [`ApplyLinearImpulse`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_prop/applylinearimpulse) | Apply a linear impulse to a ‘creative_prop’ with units in Newton*seconds. Will not do anything if physics is disabled. |
| [`ApplyTorque`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_prop/applytorque) | Apply a torque to a ‘creative_prop’ with units in Newton*meters. Will not do anything if physics is disabled. |
| [`Dispose`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_prop/dispose) | Destroys the `creative_prop` and remove it from the island. |
| [`GetAngularVelocity`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_prop/getangularvelocity) | Returns a ‘creative_prop’s angular velocity in radians/second. |
| [`GetDynamic`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_prop/getdynamic) | Get whether a ‘creative_prop’ is dynamic (affected by physics functions). |
| [`GetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) | Gets the global transform of this object. |
| [`GetLinearVelocity`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_prop/getlinearvelocity) | Returns a ‘creative_prop’s linear velocity in meters/second. |
| [`GetMass`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_prop/getmass) | Returns a ‘creative_prop’s mass in kilograms. |
| [`GetTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) | Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| [`Hide`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_prop/hide) | Hides the `creative_prop` in the world and disable collisions. |
| [`IsDisposed`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_prop/isdisposed) | Succeeds if this object has been disposed of either via `Dispose()` or through an external system. |
| [`IsValid`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_prop/isvalid) | Succeeds if this object has not been disposed of either via `Dispose()` or through an external system. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) | Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) | Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) | Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state. |
| [`SetAngularVelocity`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_prop/setangularvelocity) | Set a ‘creative_prop’s angular velocity in radians/seconds. Will not do anything if physics is disabled. |
| [`SetDynamic`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_prop/setdynamic) | Set whether a ‘creative_prop’ is dynamic (affected by physics functions). Will not do anything if physics is disabled OR the prop does not have a FortPhysicsComponent. |
| [`SetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) | Sets the global transform of this object. |
| [`SetLinearVelocity`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_prop/setlinearvelocity) | Set a ‘creative_prop’s linear velocity in meters/second. Will not do anything if physics is disabled. |
| [`SetMaterial`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_prop/setmaterial) | Changes the Material of the Mesh used by this instance. Optionally can specify which Mesh element index to apply the material to, otherwise defaults to the 0 (default) Mesh element |
| [`SetMesh`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_prop/setmesh) | Changes the Mesh used by this instance. |
| [`Show`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_prop/show) | Shows the `creative_prop` in the world and enable collisions. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) | Teleports the `creative_object` to the specified `Position` and `Rotation`. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) | Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) | Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly. |
