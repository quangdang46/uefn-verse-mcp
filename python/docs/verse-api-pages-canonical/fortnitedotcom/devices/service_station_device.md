## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/service_station_device

# service_station_device class
Learn technical details about the service_station_device class.
A one stop automated refueling and repairing station for your vehicles.
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
[`enableable`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/versedotorg/verse/enableable) |  Implemented by classes whose instances can be enabled and disabled.
## Members
This class has both data members and functions.
### Data
Data Member Name | Type | Description
---|---|---
`VehicleEnteredEvent` | `listenable(payload)` |  Fires when a vehicle enters the service station, returns the vehicle that entered.
`VehicleExitedEvent` | `listenable(payload)` |  Fires when a vehicle leaves the service station, returns the vehicle that exited.
`VehicleFuelingBeginEvent` | `listenable(payload)` |  Fires on the first tick of a vehicle refueling, returns the refueled vehicle.
`VehicleFuelingEndEvent` | `listenable(payload)` |  Fires when a vehicle is at full fuel, returns the refueled vehicle.
`VehicleRepairBeginEvent` | `listenable(payload)` |  Fires when a vehicle starts repairing, returns the repaired vehicle.
`VehicleRepairEndEvent` | `listenable(payload)` |  Fires when a vehicle is at full health, returns the repaired vehicle.
### Functions
Function Name | Description
---|---
[`Damage`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/service_station_device/damage) |  Damage the `damageable` object anonymously by `Amount`. Setting `Amount` to less than 0 will cause no damage. Use `Damage(:damage_args):void` when damage is being applied from a known instigator and source.
[`Damage`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/service_station_device/damage-1) |  Damage the `damageable` object by `Args.Amount`. Setting `Amount` to less than 0 will cause no damage.
[`DamagedEvent`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/service_station_device/damagedevent) |  Signaled when damage is applied to the `damageable` object.
[`Disable`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/service_station_device/disable) |  Disable this object.
[`Enable`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/service_station_device/enable) |  Enable this object.
[`GetGlobalTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) |  Gets the global transform of this object.
[`GetHealth`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/service_station_device/gethealth) |  Returns the health state of the object. This value will between 0.0 and `GetMaxHealth`
[`GetMaxHealth`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/service_station_device/getmaxhealth) |  Returns the maximum health of the object. This value will be between 1.0 and Inf.
[`GetTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) |  Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result.
[`IsAnyVehicleInside`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/service_station_device/isanyvehicleinside) |  Check if any vehicle is inside the service station.
[`IsEnabled`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/service_station_device/isenabled) |  Succeeds if the object is enabled, fails if it's disabled.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) |  Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) |  Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state.
[`MoveTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) |  Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state.
[`SetGlobalTransform`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) |  Sets the global transform of this object.
[`SetHealth`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/service_station_device/sethealth) |  Sets the health state of the object to `Health`.
  * Health state will be clamped between 1.0 and `GetMaxHealth`.
  * Health state cannot be directly set to 0.0. To eliminate `healthful` objects use the `damageable.Damage` functions instead.

[`SetMaxHealth`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/service_station_device/setmaxhealth) |  Sets the maximum health state of the object.
  * MaxHealth will be clamped between 1.0 and Inf.
  * Current health state will be scaled up or down based on the scale difference between the old and new MaxHealth state.

[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) |  Teleports the `creative_object` to the specified `Position` and `Rotation`.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) |  Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
[`TeleportTo`](https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) |  Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly.
