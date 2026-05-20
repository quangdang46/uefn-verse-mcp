## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/advanced_storm_controller_device

# advanced_storm_controller_device class

Learn technical details about the advanced_storm_controller_device class.

Used to control a Battle Royale-style storm with up to 50 phases.

Like `basic_storm_controller_device`s, you can use this storm to keep players inside a playable area, but unlike the `basic_storm_controller_device`, this device generates multiple storm phases. When used in conjunction with `advanced_storm_beacon_device`s, you can customize each phase of the storm by applying one or more beacons and setting customization options for the specific phase you assign to that beacon.

|  |  |
| --- | --- |
| Verse `using` statement | `using { /Fortnite.com/Devices }` |

## Inheritance Hierarchy

This class is derived from the following hierarchy, starting with `creative_object`:

| Name | Description |
| --- | --- |
| [`creative_object`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object) | Base class for creative devices and props. |
| [`creative_device_base`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_device_base) | Base class for creative_device. |
| [`storm_controller_device`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/storm_controller_device) | Base class for various specialized storm devices. See also:  *`basic_storm_controller_device`*  `advanced_storm_controller_device` |

## Members

This class has both data members and functions.

### Data

| Data Member Name | Type | Description |
| --- | --- | --- |
| `PhaseEndedEvent` | `listenable(payload)` | Signaled when storm resizing ends. Use this with the *On Finish Behavior* option for better controls. |

### Functions

| Function Name | Description |
| --- | --- |
| [`DestroyStorm`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/storm_controller_device/destroystorm) | Destroys the storm. |
| [`GenerateStorm`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/storm_controller_device/generatestorm) | Generates the storm. *Generate Storm On Game Start* must be set to *No* if you choose to use `GenerateStorm`. |
| [`GetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) | Gets the global transform of this object. |
| [`GetTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) | Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/storm_controller_device/moveto) | Moves the `storm_controller_device` to the specified `Position` and `Rotation` over the specified time, in seconds. Existing storms will not target the new location, but newly generated storms will. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/storm_controller_device/moveto-1) | Moves the `storm_controller_device` to the specified `Transform` over the specified time, in seconds. Existing storms will not target the new location, but newly generated storms will. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) | Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) | Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) | Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state. |
| [`SetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) | Sets the global transform of this object. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/storm_controller_device/teleportto) | Teleports the `storm_controller_device` to the specified `Position` and `Rotation`. Existing storms will not target the new location, but newly generated storms will. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/storm_controller_device/teleportto-1) | Teleports the `storm_controller_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly. Existing storms will not target the new location, but newly generated storms will. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) | Teleports the `creative_object` to the specified `Position` and `Rotation`. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) | Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) | Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly. |
