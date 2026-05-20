## https://dev.epicgames.com/documentation/en-us/fortnite/verse-api/fortnitedotcom/devices/input_trigger_device

# input_trigger_device class

Learn technical details about the input_trigger_device class.

Used to listen for the player activating or releasing certain inputs.
The input is defined by the *Input* option.
Players can configure the key for the input in the Creative Input Actions section of the Keyboard Settings.

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
| `PressedEvent` | `listenable(payload)` | Signaled when the tracked input is pressed by an `agent`. Sends the `agent` that pressed the input. |
| `ReleasedEvent` | `listenable(payload)` | Signaled when the tracked input is released by an `agent`. Sends the `agent` that released the input. Sends the `float` duration that the input was held. |

### Functions

| Function Name | Description |
| --- | --- |
| [`Disable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/input_trigger_device/disable) | Disables this device. A disabled Input Trigger will not listen for inputs and will never show on the HUD. |
| [`Enable`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/input_trigger_device/enable) | Enables this device. An Input Trigger will listen for inputs from players that meet the device requirements. |
| [`GetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/getglobaltransform) | Gets the global transform of this object. |
| [`GetTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/gettransform) | Returns the transform of the `creative_object` with units in cm. You must check `creative_object.IsValid` before calling this if there is a possibility the object has been disposed or destroyed by gameplay. Otherwise a runtime error will result. |
| [`IsHeld`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/input_trigger_device/isheld) | Succeeds if `Agent` is currently holding the input. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto) | Moves the `creative_object` to the specified `Position` and `Rotation` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-1) | Moves the `creative_object` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_object` it will be stopped and put into the `AnimationNotSet` state. |
| [`MoveTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/moveto-2) | Moves the `creative_device` to the specified `Transform` over the specified time, in seconds. If an animation is currently playing on the `creative_device` it will be stopped and put into the `AnimationNotSet` state. |
| [`Register`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/input_trigger_device/register) | Adds `Agent` to the registered player list. *Registered Player Behavior* determines whether registered players meet the device requirements. |
| [`SetGlobalTransform`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/setglobaltransform) | Sets the global transform of this object. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto) | Teleports the `creative_object` to the specified `Position` and `Rotation`. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-1) | Teleports the `creative_object` to the specified location defined by `Transform`, also applies rotation and scale accordingly. |
| [`TeleportTo`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/creative_object/teleportto-2) | Teleports the `creative_device` to the specified location defined by `Transform`, also applies rotation and scale accordingly. |
| [`Unregister`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/input_trigger_device/unregister) | Removes `Agent` from the registered player list. *Registered Player Behavior* determines whether registered players meet the device requirements. |
| [`UnregisterAll`](https://dev.epicgames.com/documentation/fortnite/verse-api/fortnitedotcom/devices/input_trigger_device/unregisterall) | Clears the list of registered players. *Registered Player Behavior* determines whether registered players meet the device requirements. |
